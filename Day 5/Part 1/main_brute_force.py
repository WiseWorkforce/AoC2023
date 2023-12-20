import pandas as pd
from datetime import datetime

start_time = datetime.now()
file_to_open = r'Day 5\Part 1\input2.txt'
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
        from_to_dict[t,f] = []
    else:
        src, dest, rng = row.split(' ' )
        from_to_dict[t,f].append({'src' : src, 'dest' : dest, 'rng' : rng})
print('Refactoring input to Dicts ready! --- ' + str(datetime.now() - start_time))
print(from_to_dict)
# Make a DF per map with the options
counter = 0
df_dict = {}
num_dfs = len(from_to_dict)
counter = 0
for to_find in from_to_dict.keys():
    counter += 1
    df = pd.DataFrame()
    df[to_find[1]] = []
    df[to_find[0]] = []
    for row in from_to_dict[to_find]:
        src = int(row['src'])
        dest = int(row['dest'])
        rng = int(row['rng'])
        i = 0
        while i < rng:
            col1 = src + i
            col2 = dest + i
            tmp_list = [col2, col1]
            df.loc[len(df)] = tmp_list
            i += 1
    df = df.sort_values(by=to_find[1])
    df_dict[(to_find[1], to_find[0])] = df
    print('DataFrame (' + str(counter) + '/' + str(num_dfs) +') with all options ready! --- ' + str(datetime.now() - start_time))
seed_loc_dict = {}
# for each seed, go over each dict
num_of_seeds = len(seeds_to_collect)
counter = 0
for seed in seeds_to_collect:
    counter += 1
    next_search = 'seed'
    # Get the right dataframe
    param_to_search = seed
    for k in df_dict.keys():
        if next_search in k:
            df = df_dict[k]
            # Check if the seed is in the dataframe
            filtered = df.loc[df[next_search] == param_to_search]  
            # When it's found in the dict, get the next param from the dict, otherwise it's the same
            if len(filtered) == 1:
                param_to_search = filtered[k[1]].iloc[0]
            # Set correct for the next dict to search
            next_search = k[1]
    location = param_to_search
    seed_loc_dict[seed] = location
    print('Seed location (' + str(counter) + '/' + str(num_of_seeds) +') found! --- ' + str(datetime.now() - start_time))

closest_seed = min(seed_loc_dict, key=seed_loc_dict.get)
closest_location = min(seed_loc_dict.values())
print('The closest location is: ' + str(closest_location) +' --- ' + str(datetime.now() - start_time))