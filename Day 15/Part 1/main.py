file_to_open = r'Day 15\Input\input.txt'
grid = open(file_to_open).read().split(",")

current_value = 0

def run_hash_algorithm(current_value, input):
    multiplier = 17
    current_value = (ord(input) + current_value) * multiplier % 256
    return current_value

sum_value = 0
for p in grid:
    for c in p:
        current_value = run_hash_algorithm(current_value, c)
    sum_value += current_value
    current_value = 0
print(sum_value)