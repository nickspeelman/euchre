import streamlit as st
from deck_utilities import shuffle_deck, deal_cards_to_players
from high_card_rules import process_round_winner
from state_management import initialize_game_state, reset_game_state, update_game_state

# Step 1: Initialize the game state from Google Sheets or set a default
initialize_game_state()

# Shuffle the deck
if st.button("Shuffle Deck"):
    st.session_state.game_state["deck"] = shuffle_deck(st.session_state.game_state["deck"])
    update_game_state(st.session_state.game_state)
    st.write("Deck shuffled!")

# Deal cards to each player
if st.button("Deal Cards"):
    st.session_state.game_state["players"], message = deal_cards_to_players(
        st.session_state.game_state["deck"],
        st.session_state.game_state["players"]
    )
    st.write(message)

# Determine the round winner
if st.button("Determine Winner"):
    winner, winning_card, message = process_round_winner(st.session_state.game_state["players"])
    st.session_state.game_state["winner"] = winner
    st.write(message)

# Display each player's hand and score
st.write("Player Hands and Scores:")
for player, data in st.session_state.game_state["players"].items():
    st.write(f"{player}: Hand: {data['hand']} | Score: {data['score']}")

# Reset the game state
if st.button("Reset Game"):
    reset_game_state()
    st.write("Game reset!")
