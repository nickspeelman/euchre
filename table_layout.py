import streamlit as st

import streamlit as st

def display_players_around_table(players):
    """Displays players around a virtual table with positions N, E, S, W."""
    # Row 1: North player centered
    _, col_N, _ = st.columns([1, 2, 1])
    with col_N:
        st.subheader(players["N"]["name"])
        st.write(f"Hand: {players['N']['hand']}")
        st.write(f"Score: {players['N']['score']}")

    # Row 2: West and East players on the left and right
    col_W, col_center, col_E = st.columns([1, 2, 1])
    with col_W:
        st.subheader(players["W"]["name"])
        st.write(f"Hand: {players['W']['hand']}")
        st.write(f"Score: {players['W']['score']}")

    with col_E:
        st.subheader(players["E"]["name"])
        st.write(f"Hand: {players['E']['hand']}")
        st.write(f"Score: {players['E']['score']}")

    # Row 3: South player centered
    _, col_S, _ = st.columns([1, 2, 1])
    with col_S:
        st.subheader(players["S"]["name"])
        st.write(f"Hand: {players['S']['hand']}")
        st.write(f"Score: {players['S']['score']}")

def display_game_controls():
    """Displays game control buttons in the center of the table layout."""
    # Center column for main game controls
    col_center = st.columns([1, 2, 1])[1]
    with col_center:
        st.subheader("Game Controls")

        if st.button("Shuffle Deck"):
            return "shuffle_deck"

        if st.button("Deal Cards"):
            return "deal_cards"

        if st.button("Determine Winner"):
            return "determine_winner"

    # Bottom row for the reset button
    col_center_bottom = st.columns([1, 2, 1])[1]
    with col_center_bottom:
        if st.button("Reset Game"):
            return "reset_game"

    return None  # No action taken
