class Player:
    """Player class
    Contains information about the player,
    as well as about the hand of the player.
    Methods allow you to control the player's hand,
    as well as lay out cards.

    Args:
        name (srt): Name of a player.
        age (str): Age of a player.

    """
    def __init__(self, name, age):
        self._name = name
        self._age = age
        self.hand = []

    def get_cards(self, deck):
        while len(self.hand) < 5:
            self.hand.append(deck.popup())
