file_to_open = r'Day 5\Part 2\input.txt'
grid = open(file_to_open).read().splitlines()

seeds_to_collect = [eval(i) for i in  grid[0].replace('seeds: ', '').split(' ')]
pairs = [seeds_to_collect[i:i+2] for i in range(0,len(seeds_to_collect),2)]

# Add the ranges for the initial seeds
from_to = []
row_list = []
for pair in pairs:
    dest_f = pair[0]
    dest_t = pair[0] + pair[1] -1
    to_append = [None, None, dest_f, dest_t, None]
    row_list.append(to_append)
from_to.append(row_list)

# Add the ranges for the next mappings
row_list = []
for row in grid:
    # skip empty rows and the row with the seeds to collect
    if row == '' or 'seeds:' in row:
        continue
    # When we're at a new entry, add the list of rows to the master list
    if 'map' in row:
        if len(row_list) >  0:
            from_to.append(row_list)
        row_list = []
    else:
        dest, src, rng = row.split(' ' )
        start_src = int(src)
        end_src = start_src + int(rng) -1
        start_dest = int(dest)
        end_dest = start_dest + int(rng) - 1
        calc_diff = start_dest - start_src
        row_list.append([start_src, end_src, start_dest, end_dest, calc_diff])
# Don't forget to add the last one
from_to.append(row_list)
#####
#from_to = from_to[0:2]
####
i = 0
# There's no need to the iteration for the last list, since that's the location of the seed :)
iteration_list = ['seed to soil', 'soil to fert', 'fert to water', 'water to light', 'light to temp', 'temp to hum', 'hum to loc']
i = 0
add_extra_ix = False
# Go over the iterations (but not the last one, that only a search_in, hence the -1)
while i < len(from_to)-1:
    if 'list_for_next_iteration' not in globals():
        from_lists = from_to[i]
    else:
        from_lists = list_for_next_iteration
        add_extra_ix = True
    #print(iteration_list[i], from_lists)
    # Clear the list_for_next_iteration to be repopulated
    list_for_next_iteration = set()
    # Go over the entries to search for
    for from_list in from_lists:
        if add_extra_ix: 
            from_list = from_list[0]
        inside_calc = []
        inside_src = []
        search_for = from_list[2:4]
        #print('search_for', search_for)
        # Go over the entries to search in (That's the next list, hence the +1)
        for to_list in from_to[i+1]:
            search_in = to_list[0:2]
            calc_diff = to_list[4]
            # when the start and end search are within the search range (and stop the loop, because all is mapped)
            if search_for[0] >= search_in[0] and search_for[1] <= search_in[1]:
                inside_calc.append((None, None, search_for[0] + calc_diff, search_for[1] + calc_diff, None))
                inside_src.append([search_for[0], search_for[1]])
            # When start is before and end is within make two ranges, one before and one within
            elif search_for[0] < search_in[0] and search_for[1] <= search_in[1] and search_for[1] >= search_in[0]:
                inside_calc.append((None, None, search_in[0]+calc_diff, search_for[1]+calc_diff, None))
                inside_src.append([search_in[0], search_for[1]])
            # When start is within and end is outside (make two ranges, one within and one after)
            elif search_for[0] >= search_in[0] and search_for[1] > search_in[1] and search_for[0] <= search_in[1]:
                inside_calc.append((None, None, search_for[0] + calc_diff, search_in[1] + calc_diff, None))
                inside_src.append([search_for[0], search_in[1]])
            # When the search_in is smaller then the search_for
            elif (search_for[0] <= search_in[0] and search_for[1] >= search_in[1]):
                inside_calc.append((None, None, search_in[0] + calc_diff, search_in[1] + calc_diff, None))
                inside_src.append([search_in[0], search_in[1]])
        # If there's some part (or all, within the range of the to_list)
        if len(inside_src) > 0:
            # Add the values which are outside the ranges
            min_max_list = sum(inside_src, [])
            first_mapped_id = min(min_max_list)
            last_mapped_id = max(min_max_list)
            if search_for[0] < first_mapped_id:
                inside_calc.append((None, None, search_for[0], first_mapped_id-1, None))
            if search_for[1] > last_mapped_id:
                inside_calc.append((None, None, last_mapped_id+1, search_for[1], None))
            j = 0
            # Get the non-mapped numbers in between
            list_missing = []
            while j < len(inside_src) - 1:
                inside_calc.append((None, None, inside_src[j][1]+1, inside_src[j+1][0]-1, None))
                j += 1
        # When all is outside the to_list, just map the current start and end
        else:
            inside_calc.append((None, None, search_for[0], search_for[1], None))
        for inside in inside_calc:
            list_for_next_iteration.add(tuple(inside_calc))
        #print('end-from-list', list_for_next_iteration)
    # Go the next iteration
    i += 1
minimum_values = []
for ends in list_for_next_iteration:
    for end in ends:
        minimum_values.append(end[2])
print(min(minimum_values))