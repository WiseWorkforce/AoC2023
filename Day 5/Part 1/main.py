import pandas as pd
from datetime import datetime

start_time = datetime.now()
file_to_open = r'Day 5\Part 1\input.txt'
grid = open(file_to_open).read().splitlines()

seeds_to_collect = [eval(i) for i in  grid[0].replace('seeds: ', '').split(' ')]
highest_seed = max(seeds_to_collect)

from_to_dict = {}
for row in grid:
    # skip empty rows and the row with the seeds to collect
    if row == '' or 'seeds:' in row:
        continue
    if 'map' in row:
        f, t = row.replace(' map:','').split('-to-')
        from_to_dict[f,t] = []
    else:
        dest, src, rng = row.split(' ' )
        from_to_dict[f,t].append({'src' : int(src), 'dest' : int(dest), 'rng' : int(rng)})
#print('Refactoring input to Dicts ready! --- ' + str(datetime.now() - start_time))
        
seed_loc_dict = {}
for seed in seeds_to_collect:
    # Always start by searching for the seed
    search_type = "seed"
    param_to_search = seed
    # Get the correct dict to search
    for k in from_to_dict.keys():
        if search_type in k:
            # Go over each row for the correct dict
            for row in from_to_dict[k]:
                min_rng = row['src']
                max_rng = row['src'] + row['rng'] -1
                if param_to_search >= min_rng and param_to_search <= max_rng:
                    diff = row['dest'] - row['src']
                    # When it's in the range, get the new param to search and set the search_type for the next dict
                    param_to_search = param_to_search + diff
                    search_type = k[1]
                    seed_loc_dict[seed] = param_to_search
                    break
                search_type = k[1]
closest_seed = min(seed_loc_dict, key=seed_loc_dict.get)
closest_location = min(seed_loc_dict.values())
print('The closest seed is: ' + str(closest_seed) + ' at location: ' + str(closest_location))