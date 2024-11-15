import streamlit as st
from deck_manager import shuffle_deck, create_euchre_deck
import requests
import json
from utilities import logger
from table_manager import display_players_around_table, update_table

# Load the Apps Script URL and access key from Streamlit secrets
APPS_SCRIPT_URL = st.secrets["APPS_SCRIPT_URL"]
ACCESS_KEY = st.secrets["ACCESS_KEY"]

def initialize_game_state():
    """Initialize the game state from Google Sheets or set up a default game state."""
    if "game_state" not in st.session_state:
        print("Initializing game state")  # Debugging print statement

        # Fetch the game state from Google Sheets
        game_state = get_game_state()
        print("Fetched game state from Sheets:", game_state)  # Debugging print

        # If there's no existing game data, reset to start a new game
        if not game_state:
            print("No game data found. Resetting game state.")  # Debugging print
            reset_game_state()  # Ensures "N", "E", "S", "W" are set
        else:
            # Use the existing game state from Google Sheets
            st.session_state.game_state = {
                "deck": game_state.get("deck", shuffle_deck(create_euchre_deck())),
                "players": game_state.get("players", {
                    "N": {"name": "Player 1", "hand": [], "score": 0},
                    "E": {"name": "Player 2", "hand": [], "score": 0},
                    "S": {"name": "Player 3", "hand": [], "score": 0},
                    "W": {"name": "Player 4", "hand": [], "score": 0}
                }),
                "current_round": game_state.get("current_round", 1),
                "current_turn": game_state.get("current_turn", "N"),
                "winner": game_state.get("winner", None)
            }
            print("Game state initialized from Sheets:", st.session_state.game_state)  # Debugging print
            update_game_state(st.session_state.game_state)
def reset_game_state():
    """Reset the game state to the default configuration for a new game."""
    st.session_state.game_state = {
        "deck": shuffle_deck(create_euchre_deck()),
        "players": {
            "N": {"name": "Player 1", "hand": [], "score": 0},
            "E": {"name": "Player 2", "hand": [], "score": 0},
            "S": {"name": "Player 3", "hand": [], "score": 0},
            "W": {"name": "Player 4", "hand": [], "score": 0}
        },
        "current_round": 1,
        "current_turn": "N",
        "winner": None
    }
    print("Reset game state:", st.session_state.game_state)  # Debugging print statement
    update_game_state(st.session_state.game_state)

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
    logger.info("Updating game state...")
    headers = {"Content-Type": "application/json"}
    data = json.dumps({"key": ACCESS_KEY, **game_state})
    logger.info(f"Data sent to Google Sheets: {data}")
    response = requests.post(APPS_SCRIPT_URL, headers=headers, data=data)

    # 2. Check if update to Sheets was successful
    if response.status_code == 200:
        # 3. Sync `st.session_state.game_state` with the updated state
        logger.info(f"Game State updated successfully: {game_state}")

        # 4. Automatically update the player table display
        update_table(game_state['players'])

        return True
    else:
        logger.error(f"Failed to update Google Sheets. Status code: {response.status_code}, Response: {response.text}")
        st.error("Failed to update Google Sheets.")
        return False