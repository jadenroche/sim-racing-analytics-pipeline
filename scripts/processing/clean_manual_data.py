import json
import pandas as pd
from pathlib import Path


RAW_FILE = Path("data/raw/incoming/search_results_official.json")
OUTPUT_FILE = Path("data/processed/races_manual_v1.csv")


# Load JSON
with open(RAW_FILE, "r") as file:
    data = json.load(file)

# Actual race records are inside first list
records = data[0]

# Convert to dataframe
df = pd.DataFrame(records)

# Keep only official races
df = df[df["event_type_name"] == "Race"]

# Extract track info from nested track dictionary
def get_track_name(track):
    if isinstance(track, dict):
        return track.get("track_name", "").strip()
    return None

def get_track_config(track):
    if isinstance(track, dict):
        return track.get("config_name")
    return None

def get_track_id(track):
    if isinstance(track, dict):
        return track.get("track_id")
    return None

df["track_name"] = df["track"].apply(get_track_name)
df["track_config"] = df["track"].apply(get_track_config)
df["track_id"] = df["track"].apply(get_track_id)


# Select columns to keep from the raw data
columns_to_keep = [
    "session_id",
    "subsession_id",
    "start_time",
    "end_time",
    "license_category_id",
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
    "car_class_id",
    "car_id",
    "car_class_name",
    "car_name",
    "track_id",
    "track_name",
    "track_config",
    "official_session",
    "season_id",
    "season_year",
    "season_quarter",
    "event_type",
    "event_type_name",
    "series_id",
    "series_name",
    "race_week_num",
    "event_strength_of_field",
    "champ_points",
]

clean_df = df[columns_to_keep]

clean_df.columns = (
    clean_df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

# Save clean CSV
OUTPUT_FILE.parent.mkdir(exist_ok=True)
clean_df.to_csv(OUTPUT_FILE, index=False)

print(f"Clean file created: {OUTPUT_FILE}")
print(f"Rows saved: {len(clean_df)}")
print(clean_df.head())







