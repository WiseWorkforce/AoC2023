file_to_open = r'Day 11\Part 2\input.txt'
f = open(file_to_open).read()
grid = f.splitlines()

def get_dotted_lines(grid):
    line_ix = 0
    dotted_ix = []
    # Make a list of the cols/rows with only dots
    for line in grid:
        if len(line) == line.count("."):
            dotted_ix.append(line_ix)
        line_ix += 1
    return dotted_ix

# Get the Rows with only dots
dotted_rows = get_dotted_lines(grid)

t_grid = []
# Transpose, to search the colums
for e in zip(*grid):
    t_grid.append(''.join(e))
# Get the Columns with only dots
dotted_cols = get_dotted_lines(t_grid)

# Get location of the #
tags = []
l = 0
while l < len(grid):
    c = 0
    while c < len(grid[l]):
        if grid[l][c] == "#":
            tags.append((l,c))
        c +=1
    l += 1

# Make a list of the pairs and calculate the distance between them (and when there's a dotted row/col in between add the number of lines)
sum = 0
pairs = [(a, b) for idx, a in enumerate(tags) for b in tags[idx + 1:]]
lines_to_add = 1000000 -1
for pair in pairs:
    start_row = pair[0][0]
    end_row = pair[1][0]
    extra_rows = 0
    for i in range(start_row+1, end_row+1):
        if i in dotted_rows:
            extra_rows += lines_to_add
    vert_distance = abs(pair[1][0] - pair[0][0]) + extra_rows
    if pair[1][1] > pair [0][1]:
        start_col = pair[0][1]
        end_col = pair[1][1]
    else:
        start_col = pair[1][1]
        end_col = pair[0][1]
    extra_cols = 0
    for i in range(start_col+1, end_col+1):
        if i in dotted_cols:
            extra_cols += lines_to_add
    hor_distance = abs(pair[1][1] - pair[0][1]) + extra_cols
    total_distance = vert_distance + hor_distance
    sum += total_distance
print(sum)