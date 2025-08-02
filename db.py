import sqlite3
from datetime import datetime

DB_NAME = 'queries.db'

# Create table if not exists
def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            command TEXT,
            result TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Insert a log record
def log_query(command, result):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO logs (timestamp, command, result) VALUES (?, ?, ?)',
        (datetime.now().isoformat(), command, result)
    )
    conn.commit()
    conn.close()
