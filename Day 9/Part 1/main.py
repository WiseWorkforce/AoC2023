file_to_open = r'Day 9\Part 1\input.txt'
grid = open(file_to_open).read().splitlines()

init_line_num = 0
list_of_lines = {}
for line in grid:
    list_of_lines[init_line_num] = []
    entries = [int(x) for x in line.split(' ')]
    list_of_lines[init_line_num].append(entries)
    line_i = 1
    end  = len(entries)-1
    while True:
        new_line = []
        # Calculate the differences
        for i in range(line_i, end+1):
            diff = entries[i] - entries[i-1]
            new_line.append(diff)
        count_zeros = new_line.count(0)
        if count_zeros == end:
            break
        else:
            list_of_lines[init_line_num].append(new_line)
            entries = new_line
            line_i = 1
            end = len(entries) -1
    init_line_num += 1
outcome = 0
for line in list_of_lines.keys():
    num_to_add = 0
    for add_line in reversed(list_of_lines[line]):
        add_line.append(add_line[-1] + num_to_add)
        num_to_add = add_line[-1]
        print(add_line, num_to_add)
    outcome += num_to_add
    print("new")
print(outcome)