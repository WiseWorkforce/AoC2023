file_to_open = r'Day 4\Part 1\input.txt'
grid = open(file_to_open).read().splitlines()

prev_card = 0
sum_value = 0
for row in grid:
    card_number = row.split(':')[0]
    rest_of_card = row.split(':')[1]
    winning_str = rest_of_card.split('|')[0].strip().split(' ')
    winning_str = [x for x in winning_str if x != '']
    have_str = rest_of_card.split('|')[1].strip().split(' ')
    have_str = [x for x in have_str if x != '']
    multiplier = 0
    for i in have_str:
        if i in winning_str:
            if multiplier == 0 :
                multiplier = 1
            else:
                multiplier = multiplier * 2
    sum_value += multiplier
print(sum_value)
