file_to_open = r'Day 7\Part 2\input.txt'
grid = open(file_to_open).read().splitlines()
cards_order = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']
type_order = [6, 5, 4, 3, 2, 1, 0] # ['five', 'four', 'fullhouse', 'three', '2pair', '1pair', 'one']

def get_type_of_entry(entry):
    unique_entries = ''.join(set(entry))
    num_of_j = entry.count("J")
    entry_type = None
    # one unique char is always a 5 of a kind
    if len(unique_entries) == 1:
        # 5 OF A KIND
        entry_type = 6
    # Two unique chars, either 4 of a kind (when there's no J) or a 5 of a kind (when there is a J)
    # (XXYYY) or (XXXXY)
    elif len(unique_entries) == 2:
        # When there are 1, (JXXXX), 2 (JJXXX), 3 (JJJXX) or 4 (JJJJX) J's, it becomes a 5 of a kind (XXJJJ)
        if num_of_j >= 1:
            entry_type = 6
        else:
            # check for each unique entry how many times it appears in the entry
            i = 0
            while i < len(unique_entries):
                times = entry.count(unique_entries[i])
                # when something appears 4 times it's a four of a kind, so break after
                if times == 4:
                    entry_type = 5
                    break
                # When a char apears 3 times, it's a full house
                elif times == 3:
                    entry_type = 4
                    break
                i += 1
    # 3 unique chars, a three of a kind (XXXYZ) or two pair (XXYYZ)
    elif len(unique_entries) == 3:
        # Where there are 2 (JJXXY) or 3 (JJJXY) J's, it becomes a 4 of a kind
        # When there are 3 J's, it becomes a 4 of a kind (XYJJJ)
        if num_of_j >= 2:
            entry_type = 5
        else:
            # Either a three of a kind or Two pair
            # check for each unique entry how many times it appears in the entry
            i = 0
            while i < len(unique_entries):
                if unique_entries[i] == "J":
                    i += 1
                    continue
                times = entry.count(unique_entries[i])
                # When something appears twice, it's always a two pair, so break after
                if times == 2:
                    # When there is a J, it becomes a Full House (XXYYJ)
                    if num_of_j == 1:
                        entry_type = 4
                        break
                    entry_type = 2
                    break
                # When something appears three times, it's always a three of a kind, so break after
                elif times == 3:
                    # When there is a J, it becomes a 4 of a kind
                    if num_of_j == 1:
                        entry_type = 5
                        break
                    entry_type = 3
                    break
                i += 1
    # 4 unique chars, one pair (XXYZA)
    elif len(unique_entries) == 4:
        # If there are 1 (XXJYZ) or 2 (JJXYZ) J's, it becomes a 3 of a kind
        if num_of_j >= 1:
            entry_type = 3
        else:
            entry_type = 1
    # 5 unique chars, high card (XYZAB)
    elif len(unique_entries) == 5:
        # If there's a J, it becomes a pair
        if num_of_j == 1:
            entry_type = 1
        else:
            entry_type = 0
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