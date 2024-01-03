import re

file_to_open = r'Day 8\Part 1\input.txt'
grid = open(file_to_open).read().splitlines()
indices = ["L", "R"]

order = str(grid[0])
entries = grid[2:]
i = 0
srcs = []
dests = []
while i < len(entries):
    src, dest = entries[i].split(" = ")
    srcs.append(src)
    regex = re.compile(r'\((.*?)\)') 
    temp = regex.findall(dest) 
    dest = [tuple(sub.split(', ')) for sub in temp][0] 
    dests.append(dest)
    i += 1
    
i = srcs.index("AAA")
j = 0
counter = 0
while True:
    if srcs[i] == "ZZZ":
        break
    src = srcs[i]
    dest = dests[i]
    ix = indices.index(order[j])
    i = srcs.index(dest[ix])
    j += 1
    if j == len(order):
        j = 0
    counter += 1
print(counter)