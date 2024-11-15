import streamlit as st
import requests
import json
from utilities import  logger

# Load the Apps Script URL and access key from Streamlit secrets
APPS_SCRIPT_URL = st.secrets["APPS_SCRIPT_URL"]
ACCESS_KEY = st.secrets["ACCESS_KEY"]

# Function to fetch game state from Google Sheets via Apps Script
def get_game_state():
    """Fetch game state from Google Sheets."""
    response = requests.get(APPS_SCRIPT_URL, params={"key": ACCESS_KEY})
    print("Response content:", response.text)  # Debugging print statement
    try:
        return response.json() if response.status_code == 200 else {}
    except ValueError:
        print("Error decoding JSON. Response content:", response.text)
        return {}

# Function to update game state in Google Sheets via Apps Script
def update_game_state(game_state):
    # 1. Update Google Sheets
    logger.info("Updated game state")
    headers = {"Content-Type": "application/json"}
    data = json.dumps({"key": ACCESS_KEY, **game_state})
    logger.info('Data sent to google sheets: ', data)
    response = requests.post(APPS_SCRIPT_URL, headers=headers, data=data)

    # 2. Check if update to Sheets was successful
    if response.status_code == 200:
        # 3. Sync `st.session_state.game_state` with the updated state
        st.session_state.game_state = game_state
        logger.info("Game State: ", game_state)
        return True
    else:
        st.error("Failed to update Google Sheets.")
        return False