file_to_open = r'Day 4\Part 2\input.txt'
grid = open(file_to_open).read().splitlines()
cards_dict = {}
num_cards = len(grid)
iter_dict = {}
for row in grid:
    card_number = int(row.split(':')[0].replace("Card ", ""))
    rest_of_card = row.split(':')[1]
    winning_str = rest_of_card.split('|')[0].strip().split(' ')
    winning_str = [x for x in winning_str if x != '']
    have_str = rest_of_card.split('|')[1].strip().split(' ')
    have_str = [x for x in have_str if x != '']
    num_corresponding = len(set(winning_str) & set(have_str))
    cards_dict[card_number] = [*range(card_number+1, num_corresponding+card_number+1)]
    iter_dict[card_number] = {}
    iter_dict[card_number][1] = cards_dict[card_number]
#
# cards_dict = card_number, [cards_earned]
# Iter_dict = card_number, iteration, [cards_earned] --> i.e. card 1, iteration 1 = iter_dict[1][1] = [2,3,4,5] and iter_dict[2][1] = [3,4]
#

card_number = 1
while card_number <= num_cards:
    another_iteration = True
    iter = 1
    # When we're at the end, continue to the next card
    if not another_iteration:
        continue
    while another_iteration:
        cards_list = []
        for card_to_search in iter_dict[card_number][iter]:
            for i in range(0, len(cards_dict[card_to_search])):
                cards_list.append(cards_dict[card_to_search][i])
        if len(cards_list) > 0:
            iter += 1
            iter_dict[card_number][iter] = cards_list
            another_iteration = True
        else:
            another_iteration = False
    card_number += 1
sum_value = 0
# Now, count all of the card numbers you have
for card_number in range(1, num_cards+1):
    for iter in iter_dict[card_number]:
        cards_found = iter_dict[card_number][iter]
        for card in cards_found:
            sum_value += 1
# Add the initial number of cards to the cards you earned
print(sum_value + num_cards)