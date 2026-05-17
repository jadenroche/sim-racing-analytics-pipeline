from dotenv import load_dotenv
import os

load_dotenv("config/.env")

def get_access_token():
    print("Auth client creation is currently paused by iRacing.")
    print("API connector is prepared but disabled for now.")
    return None

    client_id = os.getenv("IRACING_CLIENT_ID")

    if not client_id:
        raise ValueError("Missing IRACING_CLIENT_ID in config/.env")
    
    print("Config loaded succesfully.")
    print("Auth token setup will go here.")

    return None

if __name__ == "__main__":
    get_access_token()