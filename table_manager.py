import streamlit as st

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

def _render_table(players):
    """Internal helper to render the table."""
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
    _, col_N, _ = st.columns([1, 2, 1])
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
