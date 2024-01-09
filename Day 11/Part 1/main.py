file_to_open = r'Day 11\Part 1\input.txt'
f = open(file_to_open).read()
grid = f.splitlines()

def double_dotted_rows(grid):
    line_ix = 0
    extra_rows = grid.copy()
    # Add extra row when there's only dots in it
    for line in grid:
        if len(line) == line.count("."):
            extra_rows.insert(line_ix, line)
            line_ix += 1
        line_ix += 1
    return extra_rows

# Double the rows with only dots
grid = double_dotted_rows(grid)

t_grid = []
# Transpose, to expand the columns
for e in zip(*grid):
    t_grid.append(''.join(e))
t_grid = double_dotted_rows(t_grid)
# Transpose back again to get back to original orientation
grid = []
for e in zip(*t_grid):
    grid.append(''.join(e))

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

# Make a list of the pairs and calculate the distance between them
sum = 0
pairs = [(a, b) for idx, a in enumerate(tags) for b in tags[idx + 1:]]
for pair in pairs:
    vert_distance = abs(pair[1][0] - pair[0][0])
    hor_distance = abs(pair[1][1] - pair[0][1])
    total_distance = vert_distance + hor_distance
    sum += total_distance
print(sum)