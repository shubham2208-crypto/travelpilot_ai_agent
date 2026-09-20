import json
import os
from database.db import get_connection

def load_json(filename):
    path = os.path.join("data", filename)
    if os.path.exists(path):
        with open(path, "r") as f:
            return json.load(f)
    return []

def seed_database():
    conn = get_connection()
    cursor = conn.cursor()
    # Check if already seeded
    cursor.execute("SELECT count(*) FROM trips")
    if cursor.fetchone()[0] == 0:
        cursor.execute("""
            INSERT INTO trips (destination, start_date, end_date, budget, interests, preferences, status)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, ("Paris", "2026-10-10", "2026-10-15", 1500.0, "Culture,Food,Architecture", "Balanced", "Active"))
        conn.commit()
    conn.close()