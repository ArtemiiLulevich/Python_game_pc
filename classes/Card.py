class Card:
    """Class to represent cards of the game.



    """
    def __init__(self, colour, form, value):
        """Card init method.

        Args:
            form (str): form of the card.
            colour (str): colour of the card.
            value (str): value of the card.
        """
        self._form = form
        self._colour = colour
        self._value = value
        self._card_name = colour[:2] + form[:2] + value

    def get_card_name(self):
        print(self._card_name)

    def get_card_value(self):
        print(int(self._value))


if __name__ == "__main__":
    new_card = Card("Red", "Square", "1")

    new_card.get_card_name()
    new_card.get_card_value()
