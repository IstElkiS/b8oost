import sqlite3

def create_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT,
            password TEXT UNIQUE NOT NULL,
            status TEXT
        )
    ''')
    conn.commit()
    conn.close()

create_db()
