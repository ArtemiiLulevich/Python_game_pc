import shelve


# colors = ('Red', 'Yellow', 'Green', 'Blue')
# forms = ('Circle', 'Triangle', 'Square', 'Cross')
# values = ('1', '2', '3', '4')
# cards = list()
#
# with shelve.open("data_for_game") as data_file:
#
#     for colour in colors:
#         for form in forms:
#             for value in values:
#                 # print("{}\t{}\t{}".format(colour, form, value))
#                 cards.append("{}\t{}\t{}".format(colour, form, value))
#
#     cards = tuple(cards)
#
#     data_file['cards'] = cards


data = shelve.open('data_for_game')

cards = data['cards']

print(cards)

for card in cards:
    print(card)

data.close()
