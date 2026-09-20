import sqlite3
import os
from database.schema import CREATE_TABLES

DB_PATH = "database/travelpilot.db"

def get_connection():
    os.makedirs("os.path.dirname(DB_PATH)", exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.executescript(CREATE_TABLES)
    conn.commit()
    conn.close()