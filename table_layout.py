import streamlit as st

def display_players_around_table(players):
    """Displays players around a virtual table with positions N, E, S, W."""
    col_N, col_center, col_E = st.columns([1, 2, 1])
    col_W,  col_center_bottom, col_S = st.columns([1, 2, 1])

    # North player
    with col_N:
        st.subheader(players["N"]["name"])
        st.write(f"Hand: {players['N']['hand']}")
        st.write(f"Score: {players['N']['score']}")

    # East player
    with col_E:
        st.subheader(players["E"]["name"])
        st.write(f"Hand: {players['E']['hand']}")
        st.write(f"Score: {players['E']['score']}")

    # South player
    with col_S:
        st.subheader(players["S"]["name"])
        st.write(f"Hand: {players['S']['hand']}")
        st.write(f"Score: {players['S']['score']}")

    # West player
    with col_W:
        st.subheader(players["W"]["name"])
        st.write(f"Hand: {players['W']['hand']}")
        st.write(f"Score: {players['W']['score']}")

def display_game_controls():
    """Displays game control buttons in the center of the table layout."""
    col_center = st.columns([1, 2, 1])[1]  # Use the center column for controls
    with col_center:
        st.subheader("Game Controls")

        if st.button("Shuffle Deck"):
            return "shuffle_deck"

        if st.button("Deal Cards"):
            return "deal_cards"

        if st.button("Determine Winner"):
            return "determine_winner"

    # Bottom center for reset button
    col_center_bottom = st.columns([1, 2, 1])[1]
    with col_center_bottom:
        if st.button("Reset Game"):
            return "reset_game"

    return None  # No action taken
