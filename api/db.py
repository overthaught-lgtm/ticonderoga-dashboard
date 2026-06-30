import sqlite3, os
DB_PATH = os.environ.get("DB_PATH", "ears.db")

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS hubs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            location TEXT,
            weight REAL DEFAULT 0.0,
            status TEXT DEFAULT 'online',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        CREATE TABLE IF NOT EXISTS ears_events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            hub_id INTEGER REFERENCES hubs(id),
            event_type TEXT,
            velocity REAL,
            dwell REAL,
            acoustic REAL,
            affinity TEXT,
            raw JSON,
            ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        CREATE TABLE IF NOT EXISTS dap_scores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            hub_id INTEGER REFERENCES hubs(id),
            persona TEXT,
            ltv_score REAL,
            signal_index REAL,
            ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        INSERT OR IGNORE INTO hubs (id, name, location, weight, status)
        VALUES
            (1, 'Craig',       'Craig, CO',       0.72, 'online'),
            (2, 'Hayden',      'Hayden, CO',      0.45, 'online'),
            (3, 'Walsenburg',  'Walsenburg, CO',  0.21, 'online');
    """)
    conn.commit()
    conn.close()
