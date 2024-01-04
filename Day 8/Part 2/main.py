import re, fnmatch
from math import gcd

file_to_open = r'Day 8\Part 2\input.txt'
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
    
# Get all of the nodes ending with an A
pattern = '??A'
search_srcs = fnmatch.filter(srcs, pattern)
ix_search = []
for search_src in search_srcs:
    ix_search.append(srcs.index(search_src))


output = {}

# Go over each endwith(A) and check the number of steps to the first Z
for src in search_srcs:
    initial = src
    j = 0
    output[initial] = 0
    while True:
        lr = indices.index(order[j])
        j += 1
        if j == len(order):
            j = 0
        if src.endswith('Z'):
            break
        output[initial] += 1
        src_ix = srcs.index(src)
        src = dests[src_ix][lr]

# Calculate the LCM
list_of_steps = list(output.values())
lcm = 1
for i in list_of_steps:
    lcm = lcm*i//gcd(lcm, i)
print(lcm)