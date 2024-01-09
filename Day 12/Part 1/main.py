file_to_open = r'Day 12\Input\input.txt'
grid = open(file_to_open).read().splitlines()

def generate_all_combinations(rec, ix = 0):
    if ix >= len(rec):
        return [rec]
    if rec[ix] == "?":
        damaged_str = rec[:ix] + "#" + rec[ix+1:]
        working_str = rec[:ix] + "." + rec[ix+1:]
        with_damaged = generate_all_combinations(damaged_str, ix + 1)
        with_working = generate_all_combinations(working_str, ix + 1)
        return with_damaged + with_working
    else:
        return generate_all_combinations(rec, ix + 1)

def check_if_combo_is_valid(rec, damaged):
    check_record = []
    damaged_record = [int(i) for i in damaged.split(',')]
    damaged_combo = rec.count("#")
    # Only do the loops when the number of broken springs is the same
    if damaged_combo == sum(damaged_record):
        num_of_damaged = 0
        for spring in rec:
            # if spring is damaged add one
            if spring == "#":
                num_of_damaged += 1
            # Now we're at the end of damaged ones, so copy to a list and rest
            else:
                if num_of_damaged > 0:
                    check_record.append(num_of_damaged)
                    num_of_damaged = 0
        # If there's a count of damaged ones at the end
        if num_of_damaged > 0:
            check_record.append(num_of_damaged)
        return check_record == damaged_record
    else:
        return False

counter = 0
for line in grid:
    rec, damaged = line.split(' ')
    all_combos = generate_all_combinations(rec)
    for combo in all_combos:
        valid = check_if_combo_is_valid(combo, damaged)
        if valid:
            counter += 1
print(counter)   
    