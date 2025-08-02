
# 🚀 DriveAI Assistant

An AI-powered Flask web app that accepts simple commands and interacts with your Google Drive — listing files and summarizing document contents using OpenAI GPT-4o.

---

## ✅ Features

- 🔍 `LIST /FolderName` — lists files in your Google Drive matching the folder name
- 🧠 `SUMMARY /file.pdf` — generates an AI summary of the document contents (PDF, DOCX, or TXT)
- 🗂️ Google Drive API + OpenAI GPT-4o integration
- 📄 Logs each query in a SQLite database
- 💡 Simple web interface (Flask + HTML + CSS)

---

## 🖥️ Tech Stack

- Python 3.x
- Flask
- OpenAI API (GPT-4o / GPT-3.5-turbo)
- Google Drive API
- PyPDF2, python-docx
- SQLite (for logging)

---

## 🛠️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/driveai-assistant.git
cd driveai-assistant
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate  # For Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

> Or install manually:
```bash
pip install flask openai python-dotenv google-api-python-client google-auth-httplib2 google-auth-oauthlib PyPDF2 python-docx
```

---

### 4. Add `.env` File

Create a `.env` file and add your OpenAI key:

```
OPENAI_API_KEY=your-openai-key-here
```

---

### 5. Add Google Credentials

- Visit: https://console.cloud.google.com/
- Create OAuth2 credentials (Application type: Desktop)
- Enable **Google Drive API**
- Download `credentials.json` and place it in the project root

---

### 6. Run the App

```bash
python app.py
```

Then open in browser:
```
http://127.0.0.1:5000
```

---

## 💬 Supported Commands

| Command                 | Description                                  |
|-------------------------|----------------------------------------------|
| `LIST /ProjectX`        | Lists files containing "ProjectX" in name    |
| `SUMMARY /file.docx`    | Summarizes a Word/PDF/Text file using GPT    |

> More commands (`DELETE`, `MOVE`) coming soon.

---

## 📁 Folder Structure

```
driveai-assistant/
├── app.py
├── db.py
├── gdrive_helper.py
├── openai_helper.py
├── requirements.txt
├── .env
├── credentials.json
├── token.json  ← (auto-generated on first run)
├── queries.db  ← (auto-generated)
├── templates/
│   ├── index.html
│   └── result.html
└── static/
    └── style.css
```

---

## 🧪 Demo

🎥 A sample 3-minute demo video is available here:  
[👉 Watch Demo on YouTube](https://www.youtube.com/) ← *(replace with your real link)*

---

## 📌 Notes

- `token.json` and `queries.db` are created automatically after first run.
- Only PDF, DOCX, and TXT are supported for summary.
- File names must exactly match what's in your Google Drive.

---

## ✨ Credits

Built for internship task (Task 2: WhatsApp/Drive AI Assistant)  
Developed by [Your Name]

---

## 📜 License

MIT License — Free for personal and academic use.
