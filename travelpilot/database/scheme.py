CREATE TABLE IF NOT EXISTS trips (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    destination TEXT,
    start_date TEXT,
    end_date TEXT,
    budget REAL,
    interests TEXT,
    preferences TEXT,
    status TEXT
);

CREATE TABLE IF NOT EXISTS itineraries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    trip_id INTEGER,
    day_number INTEGER,
    activity_name TEXT,
    start_time TEXT,
    end_time TEXT,
    cost REAL,
    category TEXT,
    status TEXT
);

CREATE TABLE IF NOT EXISTS audit_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    trip_id INTEGER,
    timestamp TEXT,
    message TEXT
);