import json
from pathlib import Path

import pandas as pd


RAW_FILE = Path("data/raw/incoming/search_results_official.json")
OUTPUT_FILE = Path("data/processed/races_api_v1.csv")

OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)


def extract_records(raw_data):
    # Extract race records from the nested iRacing JSON export.
    # Expected shape: [[{record}, {record}, ...]]
    if isinstance(raw_data, list) and raw_data and isinstance(raw_data[0], list):
        return raw_data[0]

    raise ValueError("Unexpected JSON structure. Expected nested list of race records.")


def get_track_name(track):
    if isinstance(track, dict):
        return track.get("track_name")
    return None


def get_track_config(track):
    if isinstance(track, dict):
        return track.get("config_name")
    return None


def get_track_id(track):
    if isinstance(track, dict):
        return track.get("track_id")
    return None


with open(RAW_FILE, "r", encoding="utf-8") as file:
    data = json.load(file)

records = extract_records(data)
df = pd.DataFrame(records)

# Keep official race sessions only
df = df[df["event_type_name"] == "Race"].copy()

# Split nested track field into analysis friendly columns
df["track_name"] = df["track"].apply(get_track_name)
df["track_config"] = df["track"].apply(get_track_config)
df["track_id"] = df["track"].apply(get_track_id)

columns_to_keep = [
    "session_id",
    "subsession_id",
    "start_time",
    "end_time",
    "license_category",
    "num_drivers",
    "event_average_lap",
    "event_best_lap_time",
    "event_laps_complete",
    "cust_id",
    "starting_position",
    "finish_position",
    "starting_position_in_class",
    "finish_position_in_class",
    "laps_complete",
    "laps_led",
    "incidents",
    "car_class_name",
    "car_name",
    "track_id",
    "track_name",
    "track_config",
    "official_session",
    "season_year",
    "season_quarter",
    "event_type_name",
    "series_name",
    "race_week_num",
    "event_strength_of_field",
    "champ_points",
]

df_clean = df[columns_to_keep].copy()

# Convert timestamps
df_clean["start_time"] = pd.to_datetime(df_clean["start_time"], errors="coerce")
df_clean["end_time"] = pd.to_datetime(df_clean["end_time"], errors="coerce")

# Add calculated columns
df_clean["positions_gained"] = (
    df_clean["starting_position"] - df_clean["finish_position"]
)

df_clean["incident_rate"] = (
    df_clean["incidents"] / df_clean["laps_complete"].replace(0, pd.NA)
)

df_clean.to_csv(OUTPUT_FILE, index=False)

print(f"Rows loaded: {len(df)}")
print(f"Columns exported: {len(df_clean.columns)}")
print(f"Clean API file saved to: {OUTPUT_FILE}")
print(df_clean.head())