import streamlit as st
from google_sheets_manager import get_game_state, update_game_state
from deck_utilities import shuffle_deck, create_euchre_deck

def initialize_game_state():
    """Initialize or reset the game state."""
    if "game_state" not in st.session_state:
        # Fetch the game state from Google Sheets
        game_state = get_game_state()

        # If there's no existing game data, reset to start a new game
        if not game_state:
            reset_game_state()
        else:
            # Use the existing game state from Google Sheets
            st.session_state.game_state = {
                "deck": game_state.get("deck", shuffle_deck(create_euchre_deck())),
                "players": game_state.get("players", {
                    "player1": {"hand": [], "score": 0},
                    "player2": {"hand": [], "score": 0},
                    "player3": {"hand": [], "score": 0},
                    "player4": {"hand": [], "score": 0}
                }),
                "current_round": game_state.get("current_round", 1),
                "current_turn": game_state.get("current_turn", "player1"),
                "winner": game_state.get("winner", None)
            }
def reset_game_state():
    """Reset the game state to the default configuration for a new game."""
    st.session_state.game_state = {
        "deck": shuffle_deck(create_euchre_deck()),
        "players": {
            "player1": {"hand": [], "score": 0},
            "player2": {"hand": [], "score": 0},
            "player3": {"hand": [], "score": 0},
            "player4": {"hand": [], "score": 0}
        },
        "current_round": 1,
        "current_turn": "player1",
        "winner": None
    }
    # Save the reset state to Google Sheets
    update_game_state(st.session_state.game_state)
