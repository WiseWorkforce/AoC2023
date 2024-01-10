from functools import cache
file_to_open = r'Day 12\Input\input.txt'
grid = open(file_to_open).read().splitlines()

# Caching recursive loops for speeeeeed
@cache
def get_valid_solutions(rec, damaged):
    # When the record is done checking, it's only possible if there's groups to check for
    if not rec:
        if len(damaged) == 0:
            return True
        return False
    # When no more damaged groups to check, it's only possible if there are no more # in the record
    if not damaged:
        if rec.count("#") == 0:
            return True
        return False

    char, rest_of_rec = rec[0], rec[1:]
    # ignore the ., so run the function again with the rest of the string
    if char == ".":
        return get_valid_solutions(rest_of_rec, damaged)
    if char == "#":
        # check the first damaged-item
        group = damaged[0]
        # if there's actually room in the record to check for the looped group
        if len(rec) >= group:
            # if the rest of the looped group is possible (no dots, only ? and #)
            if all(c != "." for c in rec[:group]):
                # At the end (len == group) or the next is not a # (would be too big)
                if len(rec) == group or rec[group] != "#":
                    # Check the next possibility
                    return get_valid_solutions(rec[group+1:], damaged[1:])
        return False
    if char == "?":
        new_damaged_str = f"#{rest_of_rec}"
        new_working_str = f".{rest_of_rec}"
        return get_valid_solutions(new_damaged_str, damaged) + get_valid_solutions(new_working_str, damaged)

counter = 0
for line in grid:
    rec, damaged = line.split()
    rec = "?".join([rec] * 5)
    # Convert the damaged str to a list (with ints)
    damaged = [int(i) for i in list(damaged.split(","))]
    damaged *= 5
    counter += get_valid_solutions(rec, tuple(damaged))
print(counter)