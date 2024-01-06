file_to_open = r'Day 10\Part 1\input.txt'
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
print("start", grid[cur_line][cur_chr])
steps = 0
while True:
    steps += 1
    # Check above when it's not the first line
    if cur_line != 0 and next is None or next == "U":
        if grid[cur_line-1][cur_chr] in directions["above"].keys():
            print("above", grid[cur_line-1][cur_chr], cur_line, cur_chr)
            next = directions["above"][grid[cur_line-1][cur_chr]].replace("D","")
            cur_line = cur_line -1 
            continue
    # Check below when it's not the last line
    if cur_line != len(grid)-1 and next is None or next == "D":
        if grid[cur_line+1][cur_chr] in directions["below"].keys():
            print("below", grid[cur_line+1][cur_chr], cur_line, cur_chr)
            next = directions["below"][grid[cur_line+1][cur_chr]].replace("U","")
            cur_line = cur_line + 1
            continue
    # Chech left when it's not the first chr
    if cur_chr != 0 and next is None or next == "L":
        if grid[cur_line][cur_chr-1] in directions["left"].keys():
            print("left", grid[cur_line][cur_chr-1], cur_line, cur_chr)
            next = directions["left"][grid[cur_line][cur_chr-1]].replace("R","")
            cur_chr = cur_chr - 1
            continue
    # Chech right when it's not the last chr
    if cur_chr != len(grid[0])-1 and next is None or next == "R":
        if grid[cur_line][cur_chr+1] in directions["right"].keys():
            print("right", grid[cur_line][cur_chr+1], cur_line, cur_chr)
            next = directions["right"][grid[cur_line][cur_chr+1]].replace("L","")
            cur_chr = cur_chr + 1
            continue
    # When none of the above applies, it must be the end
    break
print(steps, steps / 2)