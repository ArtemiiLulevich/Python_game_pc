from classes.Card import Card
import shelve
import random

with shelve.open('data_for_game') as data:
    cards = data['cards']

deck = []

for card in cards:

    card_attributes = tuple(card.split('\t'))

    color, form, value = card_attributes

    new_card = Card(color, form, value)  # colour, form, value

    deck.append(new_card)

random.shuffle(deck)

for card in deck:
    # print(card)
    card.get_card_name()

print('Count of cards in deck is {}'.format(len(deck)))



