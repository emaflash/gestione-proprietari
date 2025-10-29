import sqlite3
import os

DB_PATH = "data/database.db"

# Se non esiste la cartella, creala
os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

# Se non esiste il database, crealo e inizializzalo
if not os.path.exists(DB_PATH):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS proprietari (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            cognome TEXT,
            email TEXT,
            telefono TEXT
        )
    """)
    conn.commit()
    conn.close()
