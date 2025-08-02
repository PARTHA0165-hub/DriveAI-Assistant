import os
import io
import mimetypes
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from PyPDF2 import PdfReader
import docx

# Google Drive API scope
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

# Authenticate and return Drive service
def get_drive_service():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('drive', 'v3', credentials=creds)
    return service

# List files by folder or name
def list_files(folder_name):
    try:
        service = get_drive_service()
        query = f"name contains '{folder_name}'"
        results = service.files().list(q=query, pageSize=10, fields="files(id, name)").execute()
        items = results.get('files', [])
        if not items:
            return f"No files found matching '{folder_name}'."
        return "\n".join([f"{item['name']} (ID: {item['id']})" for item in items])
    except Exception as e:
        return f"Error listing files: {str(e)}"

# Get file content and return plain text
def get_file_text(file_name):
    try:
        service = get_drive_service()
        query = f"name = '{file_name}'"
        result = service.files().list(q=query, pageSize=1, fields="files(id, name, mimeType)").execute()
        files = result.get('files', [])
        if not files:
            return "File not found."

        file_id = files[0]['id']
        mime_type = files[0]['mimeType']

        request = service.files().get_media(fileId=file_id)
        fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while not done:
            status, done = downloader.next_chunk()

        fh.seek(0)

        if mime_type == 'application/pdf':
            reader = PdfReader(fh)
            text = ""
            for page in reader.pages:
                text += page.extract_text() or ""
            return text.strip()

        elif mime_type == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document':
            doc = docx.Document(fh)
            return "\n".join([p.text for p in doc.paragraphs])

        elif mime_type.startswith("text/"):
            return fh.read().decode('utf-8')

        else:
            return f"Unsupported file type: {mime_type}"

    except Exception as e:
        return f"Error reading file: {str(e)}"
