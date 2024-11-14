import streamlit as st

def display_players_around_table(players):
    """Displays players around a virtual table with positions N, E, S, W."""

    def centered_player_display(player_data):
        """Helper function to create centered display for a player."""
        st.markdown(
            f"""
            <div style="text-align: center; padding: 10px;">
                <h3>{player_data['name']}</h3>
                <p>Hand: {player_data['hand']}</p>
                <p>Score: {player_data['score']}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    # Row 1: North player centered
    col_N, _, _ = st.columns([1, 2, 1])
    with col_N:
        centered_player_display(players["N"])

    # Row 2: West and East players on the left and right
    col_W, col_center, col_E = st.columns([1, 2, 1])
    with col_W:
        centered_player_display(players["W"])

    with col_E:
        centered_player_display(players["E"])

    # Row 3: South player centered
    _, col_S, _ = st.columns([1, 2, 1])
    with col_S:
        centered_player_display(players["S"])

def display_game_controls():
    """Displays game control buttons in the center of the table layout."""
    # Center column for main game controls
    col_center = st.columns([1, 2, 1])[1]
    with col_center:
        st.markdown(
            "<div style='text-align: center;'>"
            "<h2>Game Controls</h2></div>",
            unsafe_allow_html=True
        )

        if st.button("Shuffle Deck"):
            return "shuffle_deck"

        if st.button("Deal Cards"):
            return "deal_cards"

        if st.button("Determine Winner"):
            return "determine_winner"

    # Bottom row for the reset button
    col_center_bottom = st.columns([1, 2, 1])[1]
    with col_center_bottom:
        st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
        if st.button("Reset Game"):
            st.markdown("</div>", unsafe_allow_html=True)  # Close div after button
            return "reset_game"

    return None  # No action taken

