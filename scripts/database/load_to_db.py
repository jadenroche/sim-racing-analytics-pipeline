import pandas as pd
import sqlite3
from pathlib import Path

# File Paths
MANUAL_FILE = Path("data/processed/races_manual_v1.csv")
API_FILE = Path("data/processed/races_api_v1.csv")
DB_FILE = Path("database/sim_racing.db")

DB_FILE.parent.mkdir(exist_ok=True)

df = pd.read_csv(MANUAL_FILE)

conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

# Create table with duplicate protection               
cursor.execute("""               
CREATE TABLE IF NOT EXISTS races (
    session_id INTEGER,
    subsession_id INTEGER PRIMARY KEY,
    start_time TEXT,
    end_time TEXT,
    license_category_id INTEGER,
    license_category TEXT,
    num_drivers INTEGER,
    event_average_lap INTEGER,
    event_best_lap_time INTEGER,
    event_laps_complete INTEGER,
    cust_id INTEGER,
    starting_position INTEGER,
    finish_position INTEGER,
    starting_position_in_class INTEGER,
    finish_position_in_class INTEGER,
    laps_complete INTEGER,
    laps_led INTEGER,
    incidents INTEGER,
    car_class_id INTEGER,
    car_id INTEGER,
    car_class_name TEXT,
    car_name TEXT,
    track_id INTEGER,
    track_name TEXT,
    track_config TEXT,
    official_session INTEGER,
    season_id INTEGER,
    season_year INTEGER,
    season_quarter INTEGER,
    event_type INTEGER,
    event_type_name TEXT,
    series_id INTEGER,
    series_name TEXT,
    race_week_num INTEGER,
    event_strength_of_field INTEGER,
    champ_points INTEGER
);
"""
               )

# Insert rows while skipping duplicates
insert_sql = """
INSERT OR IGNORE INTO races (
    session_id,
    subsession_id,
    start_time,
    end_time,
    license_category_id,
    license_category,
    num_drivers,
    event_average_lap,
    event_best_lap_time,
    event_laps_complete,
    cust_id,
    starting_position,
    finish_position,
    starting_position_in_class,
    finish_position_in_class,
    laps_complete,
    laps_led,
    incidents,
    car_class_id,
    car_id,
    car_class_name,
    car_name,
    track_id,
    track_name,
    track_config,
    official_session,
    season_id,
    season_year,
    season_quarter,
    event_type,
    event_type_name,
    series_id,
    series_name,
    race_week_num,
    event_strength_of_field,
    champ_points
)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
"""

rows_before = cursor.execute("SELECT COUNT(*) FROM races;").fetchone()[0]

cursor.executemany(insert_sql, df.where(pd.notnull(df), None).values.tolist())

conn.commit()

rows_after = cursor.execute("SELECT COUNT(*) FROM races;").fetchone()[0]

conn.close()


print("Database load complete.")
print(f"Rows before: {rows_before}")
print(f"Rows after: {rows_after}")
print(f"New rows added: {rows_after - rows_before}")