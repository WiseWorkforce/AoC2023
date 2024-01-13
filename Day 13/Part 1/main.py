file_to_open = r'Day 13\Input\test.txt'
grid = open(file_to_open).read()


def find_mirror(pattern):
    l = 0
    while l < len(pattern) - 1:
        has_error = False
        offset = 0
        # Check if current line and next line are the same
        if pattern[l] == pattern[l+1]:
            offset += 1
            while offset < len(pattern):
                ix_left = l-offset
                ix_right = l + offset + 1
                if ix_left < 0 or ix_right >= len(pattern):
                    break
                if pattern[ix_left] != pattern[ix_right]:
                    has_error = True
                    break
                offset += 1
            if not has_error:
                return l + 1
        l += 1

sum_val = 0
for pattern in grid.split("\n\n"):
    mirror_row = find_mirror(pattern.splitlines())
    if mirror_row:
        sum_val += mirror_row * 100
    else:
        # Transpose to check for cols
        t_pattern = []
        for e in zip(*pattern.splitlines()):
            t_pattern.append(''.join(e))
        mirror_col = find_mirror(t_pattern)
        sum_val += mirror_col
print(sum_val)
'''
if mirror_col:
    sum_val += mirror_col
else:
    t_pattern = []
    #Transpose, to expand the columns
    for e in zip(*pattern.splitlines()):
        t_pattern.append(''.join(e))
    mirror_row = find_mirror(t_pattern)
    sum_val += mirror_row * 100
'''