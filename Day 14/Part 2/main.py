file_to_open = r'Day 14\Input\input.txt'
grid = open(file_to_open).read().splitlines()



def turn_table(t_grid, len_of_grid):
    rows_rocks = []
    for r in t_grid:
        start_col = 0
        col_rocks = {}
        col_rocks[start_col] = 0
        c_ix = 0
        while c_ix < len(r):
            if r[c_ix] == "O":
                col_rocks[start_col] +=1
            if r[c_ix] == "#":
                col_rocks[c_ix] = "#"
                col_rocks[c_ix + 1] = 0
                start_col = c_ix + 1
            c_ix += 1
        rows_rocks.append(col_rocks)
    output = []
    for row in rows_rocks:
        nr_list = []
        i = 0
        while i < len_of_grid:
            if i in row.keys():
                if row[i] != 0:
                    if row[i] != "#":
                        to_add = ["O" for x in range(1,row[i]+1)]
                    else:
                        to_add = ["#"]
                    nr_list = nr_list + to_add
                    i = i + len(to_add) -1
                else:
                    nr_list.append('.')
                i += 1
            else:
                nr_list.append('.')
                i += 1
        output.append(''.join(nr_list))
    return output

init_grid = grid.copy()

def run_cycles(num_of_cycles, output):
    all_grids = [output]
    for i in range(num_of_cycles):
        # NORTH
        len_of_grid = len(output)
        t_grid = []
        for e in zip(*output):
            t_grid.append(''.join(e))
        output = turn_table(t_grid, len_of_grid)

        # WEST
        len_of_grid = len(output)
        t_grid = []
        for e in zip(*output):
            t_grid.append(''.join(e))
        output = turn_table(t_grid, len_of_grid)

        # SOUTH
        len_of_grid = len(output)
        # reverse the list to go top-to-bottom
        output = list(reversed(output))
        t_grid = []
        for e in zip(*output):
            t_grid.append(''.join(e))
        output = turn_table(t_grid, len_of_grid)

        # EAST
        len_of_grid = len(output)
        t_grid = []
        for e in zip(*output):
            t_grid.append(''.join(e))
        t_grid = list(reversed(t_grid))
        t_grid = [x[::-1] for x in t_grid]
        output = turn_table(t_grid, len_of_grid)
        output = [x[::-1] for x in output]
        # Check if the current grid, is already part of all of the grids (it will cycle!)
        if output in all_grids:
            ix = all_grids.index(output)
            cycle = i - ix -1
            return (cycle, all_grids, output, ix, i)
        all_grids.append(output)


num_of_cycles = 1000000000
cycle, all_grids, output, first_cycle_ix, i= run_cycles(num_of_cycles, init_grid)
final = all_grids[
    (num_of_cycles - first_cycle_ix) % (i + 1 - first_cycle_ix)
    + first_cycle_ix
]
t_grid = []
for e in zip(*final):
    t_grid.append(''.join(e))
sum_value = 0
for row in t_grid:
    i = 0
    load = len(grid)
    while i < len(row):
        if row[i] == "O":
            sum_value += load
        load -= 1
        i += 1   
print(sum_value)