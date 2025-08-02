from flask import Flask, render_template, request
from gdrive_helper import list_files, get_file_text
from openai_helper import summarize_text
from db import init_db, log_query

app = Flask(__name__)
init_db()  # Initialize SQLite logging DB

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['command']
        command_parts = user_input.strip().split(' ', 1)

        if len(command_parts) != 2:
            result = "❌ Invalid format. Use: LIST /folder OR SUMMARY /file"
            return render_template("result.html", command=user_input, result=result)

        command, target = command_parts
        command = command.upper().strip()
        target = target.strip()
        result = ""

        if command == "LIST":
            result = list_files(target)
        elif command == "SUMMARY":
            file_text = get_file_text(target)
            result = summarize_text(file_text)
        else:
            result = "❌ Unsupported command. Try: LIST /folder or SUMMARY /file"

        log_query(user_input, result)
        return render_template("result.html", command=user_input, result=result)

    return render_template("index.html")


if __name__ == "__main__":
    print("🚀 Flask app starting at http://127.0.0.1:5000 ...")
    app.run(debug=True)
