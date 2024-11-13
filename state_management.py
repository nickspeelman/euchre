import streamlit as st
from google_sheets_manager import get_game_state, update_game_state
from deck_utilities import shuffle_deck, create_euchre_deck

def initialize_game_state():
    """Initialize the game state from Google Sheets or set up a default game state."""
    if "game_state" not in st.session_state:
        st.session_state.game_state = get_game_state() or {
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
        # Save initial state to Google Sheets if it's newly created
        update_game_state(st.session_state.game_state)

def reset_game_state():
    """Reset the game state to the default configuration."""
    st.session_state.game_state = {
        "deck": shuffle_deck([]),
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
    update_game_state(st.session_state.game_state)
