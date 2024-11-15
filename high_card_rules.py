from state_manager import update_game_state

def determine_high_card_winner(players):
    """Determines the winner based on the high card in each player's hand."""
    highest_card = None
    winner = None
    rank_order = {"9": 1, "10": 2, "J": 3, "Q": 4, "K": 5, "A": 6}

    for player, data in players.items():
        card = data["hand"][0]
        rank = card[:-1]  # Get the rank part (e.g., "9", "J")
        card_value = rank_order[rank]

        if highest_card is None or card_value > highest_card:
            highest_card = card_value
            winner = player

    return winner
def determine_round_winner(players):
    """Determines the winner of the round, updates scores, and returns the winner and card played."""
    if not any(player_data["hand"] for player_data in players.values()):
        return None, "Please deal cards before determining the winner."

    winner = determine_high_card_winner(players)
    players[winner]["score"] += 1
    winning_card = players[winner]["hand"][0]

    return winner, winning_card

def process_round_winner(players):
    """Determines the winner of the round, updates the score, and saves the game state."""
    winner, winning_card = determine_round_winner(players)
    if winner:
        players[winner]["score"] += 1  # Update the winner's score
        update_game_state({"players": players, "winner": winner})
        return winner, winning_card, f"The winner of this round is {winner} with the card {winning_card}!"
    else:
        return None, None, "Please deal cards before determining the winner."
