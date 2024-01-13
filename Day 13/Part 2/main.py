file_to_open = r'Day 13\Input\input.txt'
grid = open(file_to_open).read()


def find_mirror(pattern):
    l = 0
    smudges_left = 1
    while l < len(pattern) - 1:
        diffs = sum([1 for a,b in zip(pattern[l], pattern[l+1]) if a != b])
    
        has_error = False
        offset = 0
        # Check if current line and next line are the same, with one or zero differences, continue
        if (diffs == 1 and smudges_left > 0) or (diffs == 0 and smudges_left >= 0):
            if diffs == 1 and smudges_left > 0:
                smudges_left -= 1
            elif diffs == 0:
                pass
            else:
                has_error = True
                break
            #print(diffs, smudges_left, pattern[l], pattern[l+1])
            offset += 1
            while offset < len(pattern):
                ix_left = l-offset
                ix_right = l + offset + 1
                # We're at the end
                if ix_left < 0 or ix_right >= len(pattern):
                    break
                
                diffs = sum([1 for a,b in zip(pattern[ix_left], pattern[ix_right]) if a != b])
                #print('---', diffs, smudges_left, pattern[ix_left], pattern[ix_right], offset)
                # Encountered an error so not good enough
                if diffs > smudges_left:
                    has_error = True
                    smudges_left = 1
                    break
                if diffs == 1 and smudges_left == 1:
                    smudges_left -= 1
                offset += 1
            if not has_error:
                # No errors, but if the smudges are still in place, you need to go ahead and find another solution with a smudge
                if smudges_left > 0:
                    l += 1
                    continue
                #print('------', l)
                return l + 1
        l += 1

sum_val = 0
for pattern in grid.split("\n\n"):
    mirror_row = find_mirror(pattern.splitlines(), 'row')
    if mirror_row:
        sum_val += mirror_row * 100
    else:
        # Transpose to check for cols
        t_pattern = []
        for e in zip(*pattern.splitlines()):
            t_pattern.append(''.join(e))
        mirror_col = find_mirror(t_pattern, 'col')
        sum_val += mirror_col
print(sum_val)