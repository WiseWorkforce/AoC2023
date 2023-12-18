import csv
file_to_open = 'input.txt'

with open(file_to_open) as txt_file:
    txtreader = csv.reader(txt_file)
    sum_value = 0 
    for row in txtreader:
        all_digits = [x for x in row[0] if x.isdigit() == True]
        first_digit = all_digits[0]
        last_digit = all_digits[-1]
        combined_digit = int(first_digit + last_digit)
        sum_value = sum_value + combined_digit
print(sum_value)