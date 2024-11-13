import streamlit as st
from deck_utilities import shuffle_deck, deal_one_card_to_each_player
from high_card_rules import determine_round_winner
from session_manager import initialize_game_state, reset_game_state

# Step 1: Initialize game state
initialize_game_state()

# Step 2: Shuffle the deck
if st.button("Shuffle Deck"):
    st.session_state.game_state["deck"] = shuffle_deck(st.session_state.game_state["deck"])
    st.write("Deck shuffled!")

# Step 3: Deal one card to each player
if st.button("Deal Cards"):
    try:
        st.session_state.game_state["players"] = deal_one_card_to_each_player(
            st.session_state.game_state["deck"],
            st.session_state.game_state["players"]
        )
        st.write("Cards dealt to all players.")
    except ValueError as e:
        st.write(str(e))

# Step 4: Determine the winner of this round
if st.button("Determine Winner"):
    winner, winning_card = determine_round_winner(st.session_state.game_state["players"])
    if winner:
        st.session_state.game_state["winner"] = winner
        st.write(f"The winner of this round is {winner} with the card {winning_card}!")
    else:
        st.write(winning_card)  # Show message if no cards were dealt

# Display each player's hand and score
st.write("Player Hands and Scores:")
for player, data in st.session_state.game_state["players"].items():
    st.write(f"{player}: Hand: {data['hand']} | Score: {data['score']}")

# Reset the game state
if st.button("Reset Game"):
    reset_game_state()
    st.write("Game reset!")
