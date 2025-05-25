import os

# Define the directory structure
structure = {
    "python-context-async-perations-0x02": [
        "0-databaseconnection.py",
        "1-execute.py",
        "3-concurrent.py"
    ],
    "python-decorators-0x01": [
        "0-log_queries.py",
        "1-with_db_connection.py",
        "2-transactional.py",
        "3-retry_on_failure.py",
        "4-cache_query.py"
    ],
    "python-generators-0x00": [
        ".gitignore",
        "0-main.py",
        "0-stream_users.py",
        "1-batch_processing.py",
        "1-main.py",
        "2-lazy_paginate.py",
        "2-main.py",
        "3-main.py",
        "4-stream_ages.py",
        "README.md",
        "seed.py"
    ]
}

# Create folders and files
for folder, files in structure.items():
    os.makedirs(folder, exist_ok=True)
    for file in files:
        file_path = os.path.join(folder, file)
        with open(file_path, 'w') as f:
            f.write("")  # Creates an empty file

print("✅ All folders and files have been created.")
import sqlite3

class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        return self.conn.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()

if __name__ == "__main__":
 
    with sqlite3.connect("test.db") as conn:
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS users")
        cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
        cursor.execute("INSERT INTO users (name, age) VALUES ('Alice', 30), ('Bob', 25), ('Charlie', 35)")
        conn.commit()

    
    with DatabaseConnection("test.db") as cursor:
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        print(rows)