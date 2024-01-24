file_to_open = r'Day 15\Input\input.txt'
grid = open(file_to_open).read().split(",")

box_num = 0

def run_hash_algorithm(current_value, input):
    multiplier = 17
    current_value = (ord(input) + current_value) * multiplier % 256
    return current_value

boxes = {}
num_of_boxes = 256
for i in range(num_of_boxes):
    boxes[i] = []

for p in grid:
    if "=" in p:
        label, focal = p.split("=")
        operation = "="
    else:
        label = p.split("-")[0]
        focal = ''
        operation = '-'
    for c in label:
        box_num = run_hash_algorithm(box_num, c)
    # search the box if the label exists, if so delete
    labels_in_box = [x[0] for x in boxes[box_num]]
    if label in labels_in_box:
        label_ix = labels_in_box.index(label)
        # operation = -, so delete
        if operation == "-":
            del(boxes[box_num][label_ix])
        # operation = '=', so update
        else:
            boxes[box_num][label_ix] = [label, focal]
    else:     
        if operation == "=":
            boxes[box_num].append([label, focal])
    box_num = 0
sum_value = 0
for b in boxes:
    slot = 1
    for l in boxes[b]:
        if l[1] != '':
            lens_power = (b+1) * slot * int(l[1])
            sum_value += lens_power
            slot += 1
print(sum_value)