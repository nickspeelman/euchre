

import streamlit as st
from utilities import logger


# Create a global container for the player table
player_table_container = st.container()

def display_players_around_table(players):
    """Initial setup of the players around the table."""
    with player_table_container:
        # Render the initial table
        _render_table(players)

def update_table(players):
    """Updates the table without recreating it."""
    with player_table_container:
        # Clear and re-render the table
        player_table_container.empty()  # Clear existing content
        _render_table(players)
        logger.info('Table Updated')

def _render_table(players):
    """Internal helper to render the table."""
    def centered_player_display(player_data):
        """Helper function to create centered display for a player."""
        if not isinstance(player_data, dict):
            logger.error(f"Invalid player data: {player_data}")
            st.write("Error: Invalid player data")
            return

        name = player_data.get("name", "Unknown")
        hand = player_data.get("hand", [])
        score = player_data.get("score", 0)

        st.markdown(
            f"""
            <div style="text-align: center; padding: 10px;">
                <h3>{name}</h3>
                <p>Hand: {hand}</p>
                <p>Score: {score}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    # Row 1: North player centered
    _, col_N, _ = st.columns([1, 2, 1])
    with col_N:
        centered_player_display(players["N"])
        n_player = players["N"]
        logger.info(f"N Player {n_player}")

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

    logger.info('Table Rendered')
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

        # Center buttons without nested divs
        shuffle = st.button("Shuffle Deck")
        deal = st.button("Deal Cards")
        determine_winner = st.button("Determine Winner")
        reset = st.button("Reset Game")

        # Return action based on which button was clicked
        if shuffle:
            return "shuffle_deck"
        elif deal:
            return "deal_cards"
        elif determine_winner:
            return "determine_winner"
        elif reset:
            return "reset_game"


    return None  # No action taken
