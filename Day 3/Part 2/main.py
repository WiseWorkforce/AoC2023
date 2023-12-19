file_to_open = r'Day 3\Part 2\input.txt'
grid = open(file_to_open).read().splitlines()

sum_value = 0

# Iterate over the rows
for row_coord, row in enumerate(grid):
    # Iterate over the characters in the row
    for col_coord, char in enumerate(row):
        # We don't care about the digits or dots
        if char != '*':
            continue
        coord_set = set()
        # row_coord, col_coord is a coordinate for a special char
        # search row -1, row and row + 1
        for cur_row in [row_coord -1, row_coord, row_coord + 1]:
            # search col -1, col and col + 1
            for cur_col in [col_coord - 1, col_coord, col_coord + 1]:
                # when row or column is ou6t of bounds or number is not a digit, we don't care
                if cur_row < 0 or cur_row >= len(grid) or cur_col < 0 or cur_col >= len(grid[row_coord]) or not grid[cur_row][cur_col].isdigit():
                    continue
                # when column is not out of bounds and the character to the left is a digit, decrease the column
                while cur_col > 0 and grid[cur_row][cur_col - 1].isdigit():
                    cur_col -= 1
                coord_set.add((cur_row, cur_col))
        if (len(coord_set) != 2):
            continue

        numbers_list = []
        # Now iterate over the set and merge all the digits to the right of the coords
        for row, col in coord_set:
            number_string = ""
            # While column is smaller than the width of the row and the value is a digit, add this to the string
            while col < len(grid[row]) and grid[row][col].isdigit():
                # add the number to string
                number_string += grid[row][col]
                # Go to next column
                col += 1
            # add the number-string to a list and convert to INT
            numbers_list.append(int(number_string))
        sum_value += numbers_list[0] * numbers_list[1]
print (sum_value)