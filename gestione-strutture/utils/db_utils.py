import sqlite3
import pandas as pd

DB_PATH = "data/db.sqlite3"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS proprietari (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        email TEXT,
        telefono TEXT,
        note TEXT
    )""")

    cur.execute("""CREATE TABLE IF NOT EXISTS immobili (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        proprietario_id INTEGER,
        nome TEXT,
        indirizzo TEXT,
        capienza INTEGER,
        licenza TEXT,
        note TEXT,
        FOREIGN KEY (proprietario_id) REFERENCES proprietari(id)
    )""")

    cur.execute("""CREATE TABLE IF NOT EXISTS comunicazioni (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        proprietario_id INTEGER,
        data TEXT,
        canale TEXT,
        messaggio TEXT,
        allegato TEXT,
        FOREIGN KEY (proprietario_id) REFERENCES proprietari(id)
    )""")

    conn.commit()
    conn.close()

def get_df(query):
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql(query, conn)
    conn.close()
    return df

def execute(query, params=()):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(query, params)
    conn.commit()
    conn.close()
