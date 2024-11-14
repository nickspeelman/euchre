import random
from google_sheets_manager import update_game_state

def create_euchre_deck():
    """Creates a euchre deck with cards 9, 10, J, Q, K, A in each suit."""
    suits = ["H", "D", "C", "S"]  # Hearts, Diamonds, Clubs, Spades
    ranks = ["9", "10", "J", "Q", "K", "A"]
    return [rank + suit for suit in suits for rank in ranks]

def shuffle_deck(deck):
    """Shuffles the given deck in place."""
    random.shuffle(deck)
    return deck

def deal_one_card_to_each_player(deck, players):
    """Deals one card to each player from the deck."""
    if len(deck) < len(players):
        raise ValueError("Not enough cards left in the deck to deal to each player.")

    for player in players:
        players[player]["hand"] = [deck.pop()]

    return players

def deal_cards_to_players(deck, players):
    """Deals one card to each player and updates the game state."""
    try:
        players = deal_one_card_to_each_player(deck, players)
        update_game_state({"deck": deck, "players": players})
        st.rerun()
        return players, "Cards dealt to all players."
    except ValueError as e:
        return players, str(e)
