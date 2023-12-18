import csv
file_to_open = 'input.txt'

sum_value = 0

numbers_dict = {
    'one' : 1,
    'two' : 2,
    'three' : 3,
    'four' : 4,
    'five' : 5,
    'six' : 6,
    'seven' : 7,
    'eight' : 8,
    'nine' : 9,
}
with open(file_to_open) as txt_file:
    txtreader = csv.reader(txt_file)
    row_counter = 0
    first_digits_dict = {}
    last_digits_dict = {}
    for row in txtreader:
        # Make a list with a dictionary for each row
        first_digits_dict[row_counter] = []
        last_digits_dict[row_counter] = []
        # Replace all non-digits with a #, to make sure to only search for digit indices
        all_digits_str = ''.join(["#" if not x.isdigit() else x for x in row[0]])
        digit_or_not = [x.isdigit() for x in all_digits_str]
        # Get the first digit (if it exists)
        first_digit_idx = digit_or_not.index(True) if True in digit_or_not else None
        if first_digit_idx is not None:
            first_digit = row[0][first_digit_idx]
            first_digits_dict[row_counter].append({"index" : first_digit_idx, "number" : first_digit})
        # Get the last digit (if it exists)
        digit_or_not_rev = [x.isdigit() for x in reversed(all_digits_str)]
        last_digit_idx = digit_or_not_rev.index(True) if True in digit_or_not_rev else None
        if last_digit_idx is not None:
            last_digit = row[0][::-1][last_digit_idx]
            last_digits_dict[row_counter].append({"index" : last_digit_idx, "number" :last_digit})
        
        # Replace all digits with a #, to make sure to only search for numwords
        no_digits_str = ''.join(["#" if x.isdigit() else x for x in row[0]])
        # Replace the 'word' with a number and add the position of that number to the dict of this line
        for word, number in numbers_dict.items():
            str_pos = row[0].find(word)
            if str_pos >= 0:                
                replace_numword = no_digits_str.replace(word, str(number))
                # Get the first index of the numword
                first_numword_idx = [x.isdigit() for x in replace_numword].index(True)
                # Get the latest index of the numword
                last_numword_idx = [x.isdigit() for x in reversed(replace_numword)].index(True)
                #print(replace_numword, first_numword_idx, replace_numword[first_numword_idx])
                #print(replace_numword, replace_numword[::-1], last_numword_idx, replace_numword[::-1][last_numword_idx])
                first_digits_dict[row_counter].append({"index" : first_numword_idx, "number" : replace_numword[first_numword_idx]})
                last_digits_dict[row_counter].append({"index" : last_numword_idx, "number" : replace_numword[::-1][last_numword_idx]})
        # Keep track of the row we're reading
        row_counter = row_counter + 1

# sort the dictionary on lowest index for the first number/digit
sorted_first_idx = {}
for row_number in first_digits_dict.keys():
    sorted_first_idx[row_number]= sorted(first_digits_dict[row_number], key=lambda x: x["index"])

# sort the dictionary on lowest index for the last number/digit
sorted_last_idx = {}
for row_number in last_digits_dict.keys():
    sorted_last_idx[row_number]= sorted(last_digits_dict[row_number], key=lambda x: x["index"])

#Combine the two dictionaries, get the first number, combine and sum
for row_number in sorted_first_idx.keys():
    first_number = sorted_first_idx[row_number][0]['number']
    last_number = sorted_last_idx[row_number][0]['number']
    combined_number = int(first_number + last_number)
    sum_value = sum_value + combined_number
print(sum_value)