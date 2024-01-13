file_to_open = r'Day 14\Input\input.txt'
grid = open(file_to_open).read().splitlines()

# Transpose to do left-to-right operations which is easier
t_grid = []
for e in zip(*grid):
    t_grid.append(''.join(e))

len_of_grid = len(grid)
rows_rocks = []
for r in t_grid:
    print(r)
    start_col = 0
    col_rocks = {}
    col_rocks[start_col] = 0
    c_ix = 0
    while c_ix < len(r):
        if r[c_ix] == "O":
            col_rocks[start_col] +=1
        if r[c_ix] == "#":
            start_col = c_ix + 1
            col_rocks[start_col] = 0
        c_ix += 1
    rows_rocks.append(col_rocks)
output = []
for row in rows_rocks:
    nr_list = []
    i = 0
    while i < len_of_grid:
        if i in row.keys():
            if row[i] != 0:
                to_add = ["O" for x in range(1,row[i]+1)]
                nr_list = nr_list + to_add
                i = i + len(to_add) -1
            else:
                nr_list.append('-')
            i += 1
        else:
            nr_list.append('-')
            i += 1
    output.append(nr_list)
sum_value = 0

for row in output:
    i = 0
    load = len_of_grid
    while i < len(row):
        if row[i] == "O":
            sum_value += load
        load -= 1
        i += 1
print(sum_value)