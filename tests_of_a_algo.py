def card_name_check(card_name):
    if card_name in deck:
        return True
    else:
        return False


def place_check(card_place):
    places = 'NWESnwes'
    if card_place in places:
        return True
    else:
        return False


def find_location_of_card(game_field, card_name):
    x = 0
    y = 0
    for line in game_field:
        try:
            x = line.index(card_name)
        except ValueError:
            print('Not in the list')
        finally:
            y += 1

    location_of_card = (x, y)
    return location_of_card


field = [[],
         ['BlTr1'],
         []]

deck = ['BlCr3',
        'ReSq3',
        'BlCi3',
        'BlCi2',
        'BlTr4']


print(find_location_of_card(field, 'BlTr1'))


# while True:
#     card_and_place = input("Enter the card name and location using a space: ")
#     if card_and_place.lower() == 'q':
#         break
#
#     card, place = card_and_place.split(' ')
#     if place_check(place) and card_name_check(card):
#         if place.lower() == 'N':
#             pass
#         elif place.lower == 'S':
#             pass
#         elif place.lower == 'W':
#             pass
#         elif place.lower == 'E':
#             pass
#         else:
#             print('Unexpected error')
#             break


