file_to_open = r'Day 6\Part 1\input.txt'
grid = open(file_to_open).read().splitlines()

time_row = [int(x) for x in grid[0].split(' ') if x != '' and x != 'Time:']
distance_row = [int(x) for x in grid[1].split(' ') if x != '' and x != 'Distance:']
i = 0
output_list = []
while i < len(time_row):
    xs = set()
    # Get the midpoint of the time
    midpoint = 1 + (time_row[i]-1)/2
    for x in range(int(round(midpoint+0.1))-1, 0, -1):
        distance = x * (time_row[i] -x)
        x2 = int(midpoint + (midpoint - x) -1)
        if distance <= distance_row[i]:
            break
        xs.add(x)
        xs.add(x2)
        #print(x, x2, distance)
    output_list.append(len(xs))
    i += 1
# Calc the product
product = 1
for element in output_list:
        product *= element
print(product)