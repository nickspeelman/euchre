import streamlit as st
from deck_manager import shuffle_deck, deal_cards_to_players
from state_manager import initialize_game_state, reset_game_state, update_game_state
from table_manager import display_game_controls, display_players_around_table
from high_card_rules import process_round_winner
from utilities import logger

# Step 1: Initialize the game state from Google Sheets or set a default
initialize_game_state()

# Step 3: Display game controls and check for actions
logger.info('Displaying table')
action = display_players_around_table(st.session_state.game_state["players"])
logger.info('Table Displayed')

# Step 3: Display game controls and check for actions
logger.info('Displaying game controls')
action = display_game_controls()
logger.info('Controls Displayed')

# Handle actions from the game controls
if action == "shuffle_deck":
    st.session_state.game_state["deck"] = shuffle_deck(st.session_state.game_state["deck"])
    update_game_state(st.session_state.game_state)
    st.write("Deck shuffled!")

elif action == "deal_cards":
    st.session_state.game_state["players"], message = deal_cards_to_players(
        st.session_state.game_state["deck"],
        st.session_state.game_state["players"]
    )
    update_game_state(st.session_state.game_state)
    st.write(message)


elif action == "determine_winner":
    winner, winning_card, message = process_round_winner(st.session_state.game_state["players"])
    st.session_state.game_state["winner"] = winner
    update_game_state(st.session_state.game_state)
    st.write(message)

elif action == "reset_game":
    reset_game_state()
    st.write("Game reset!")



#%%
