file_to_open = r'Day 10\Part 2\input.txt'
grid = open(file_to_open).read().splitlines()

directions = {"above" : 
                {
                    "|" : "UD",
                    "7" : "DL",
                    "F" : "DR", 
                },
            "below" :
                {
                    "|" : "UD",
                    "L" : "UR",
                    "J" : "UL",
                },
            "left" :
                {
                    "-" : "LR",
                    "L" : "UR",
                    "F" : "DR",
                },
            "right" :
                {
                    "-" : "LR",
                    "J" : "UL",
                    "7" : "DL",
                },
            }
for line in grid:
    if line.find("S") != -1:
        start_line = grid.index(line)
        start_chr = line.find("S")
# Check the char above, below, left and right to see where to go
cur_line = start_line
cur_chr = start_chr
next = None
to_keep = []
to_keep.append((cur_line, cur_chr))

while True:
    # Check left when it's not the first chr
    if cur_chr != 0 and next is None or next == "L":
        if grid[cur_line][cur_chr-1] in directions["left"].keys():
            next = directions["left"][grid[cur_line][cur_chr-1]].replace("R","")
            cur_chr = cur_chr - 1
            to_keep.append((cur_line, cur_chr))
            continue
    # Check right when it's not the last chr
    if cur_chr != len(grid[0])-1 and next is None or next == "R":
        if grid[cur_line][cur_chr+1] in directions["right"].keys():
            next = directions["right"][grid[cur_line][cur_chr+1]].replace("L","")
            cur_chr = cur_chr + 1
            to_keep.append((cur_line, cur_chr))
            continue
    # Check above when it's not the first line
    if cur_line != 0 and next is None or next == "U":
        if grid[cur_line-1][cur_chr] in directions["above"].keys():
            next = directions["above"][grid[cur_line-1][cur_chr]].replace("D","")
            cur_line = cur_line -1 
            to_keep.append((cur_line, cur_chr))
            continue
    # Check below when it's not the last line
    if cur_line != len(grid)-1 and next is None or next == "D":
        if grid[cur_line+1][cur_chr] in directions["below"].keys():
            next = directions["below"][grid[cur_line+1][cur_chr]].replace("U","")
            cur_line = cur_line + 1
            to_keep.append((cur_line, cur_chr))
            continue
    
    # When none of the above applies, it must be the end
    break
def shoelace_formula(polygonBoundary, absoluteValue = True):
    nbCoordinates = len(polygonBoundary)
    nbSegment = nbCoordinates - 1

    l = [(polygonBoundary[i+1][0] - polygonBoundary[i][0]) * (polygonBoundary[i+1][1] + polygonBoundary[i][1]) for i in range(nbSegment)]

    if absoluteValue:
        return abs(sum(l) / 2.)
    else:
        return sum(l) / 2.

A = shoelace_formula(to_keep)
b = len(to_keep)
# Pick's Theorem = i = A - b/2 - h + 1 (h = 0)
result = A - b /2 + 1
print(result)