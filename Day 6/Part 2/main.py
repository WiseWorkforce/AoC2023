file_to_open = r'Day 6\Part 1\input.txt'
grid = open(file_to_open).read().splitlines()

time_row = [int(x) for x in grid[0].split(' ') if x != '' and x != 'Time:']
distance_row = [int(x) for x in grid[1].split(' ') if x != '' and x != 'Distance:']

time = int(''.join(map(str, time_row)))
min_distance = int(''.join(map(str, distance_row)))

xs = set()
# Get the midpoint of the time
midpoint = 1 + (time-1)/2
for x in range(int(round(midpoint+0.1))-1, 0, -1):
    distance = x * (time -x)
    x2 = int(midpoint + (midpoint - x) -1)
    if distance <= min_distance:
        break
    xs.add(x)
    xs.add(x2)
print(len(xs))