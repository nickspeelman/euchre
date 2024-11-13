import streamlit as st
from deck_utilities import create_euchre_deck

def initialize_game_state():
    """Initializes the game state in session state if not already set."""
    if "game_state" not in st.session_state:
        st.session_state.game_state = {
            "deck": create_euchre_deck(),
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

def reset_game_state():
    """Resets the game state to its initial values."""
    st.session_state.game_state = {
        "deck": create_euchre_deck(),
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
