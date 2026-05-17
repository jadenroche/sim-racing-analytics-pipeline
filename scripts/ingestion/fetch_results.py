import requests
import json
from pathlib import Path
from scripts.ingestion.auth_iracing import get_access_token

# Directory for raw API response storage
RAW_API_DIR = Path("data/raw/incoming/api_json")
RAW_API_DIR.mkdir(parents=True, exist_ok=True)

def fetch_results(subsession_id):
    # Fetch race result data from the iRacing API and save
    # the raw JSON response locally.

    token = get_access_token()

    if token is None:
        print("No access token available. Using local JSON ingestion instead.")
        return

    url = "https://members-ng.iracing.com/data/results/get"

    headers = {
        "Authorization": f"Bearer {token}"
    }

    params = {
        "subsession_id": subsession_id
    }

    # Initial API request
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()

    first_response = response.json()

    # Extract downloadable data link
    data_link = first_response.get("link")

    if not data_link:
        raise ValueError("No data link returned from iRacing API.")

    # Download detailed race result JSON
    data_response = requests.get(data_link)
    data_response.raise_for_status()

    result_data = data_response.json()

    output_path = RAW_API_DIR / f"result_{subsession_id}.json"

    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(result_data, file, indent=4)

    print(f"Saved raw result JSON to: {output_path}")

if __name__ == "__main__":
    fetch_results(38280997)