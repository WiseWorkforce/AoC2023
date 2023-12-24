file_to_open = r'Day 7\Part 1\input.txt'
grid = open(file_to_open).read().splitlines()
cards_order = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
type_order = [6, 5, 4, 3, 2, 1, 0] # ['five', 'four', 'fullhouse', 'three', '2pair', '1pair', 'one']

def get_type_of_entry(entry):
    unique_entries = ''.join(set(entry))
    # 5 unique = High Card
    if len(unique_entries) == 5:
        entry_type = 0
    # 4 unique = one pair
    elif len(unique_entries) == 4:
        entry_type = 1
    # 3 unique = 3 of a kind or two pair
    elif len(unique_entries) == 3:
        # check for each unique entry how many times it appears in the entry
        i = 0
        while i < len(unique_entries):
            times = entry.count(unique_entries[i])
            # When something appears twice, it's always a two pair, so break after
            if times == 2:
                entry_type = 2
                break
            # When something appears three times, it's always a three of a kind, so break after
            elif times == 3:
                entry_type = 3
                break
            i += 1
    # 2 unique = 4 of a kind or full house
    elif len(unique_entries) == 2:
        entry_type = 4
        # check for each unique entry how many times it appears in the entry
        i = 0
        while i < len(unique_entries):
            times = entry.count(unique_entries[i])
            # when something appears 4 times it's a four of a kind, so break after
            if times == 4:
                entry_type = 5
                break
            i += 1
    # 1 unique = 5 of a kind
    elif len(unique_entries) == 1:
        entry_type = 6
    return entry_type


value_rank = [x.split(' ') for x in grid]
i = 0
while i < len(value_rank):
    value, rank = value_rank[i]
    entry_list = []
    # add a comparable list of the values
    for chr in value:
        ix = cards_order.index(chr)
        entry_list.append(ix)
    entry_type = get_type_of_entry(value)
    value_rank[i].append(entry_type)
    value_rank[i].append(entry_list)
    i += 1
# Sort the list based on the strength of the hand, and after that on the cardnumber
value_rank.sort(key = lambda x: (x[2], x[3]), reverse=False)
i = 0
output = 0 
while i < len(value_rank):
    value, rank, order, comparable = value_rank[i]
    i += 1
    output += i * int(rank)
print(output)