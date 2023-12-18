import csv
file_to_open = 'input.txt'

sum_value = 0
sum_of_all_game_ids = 0 

balls_per_color = {
    'red' : 12,
    'green' : 13,
    'blue' : 14,
}
output_per_game = {}

with open(file_to_open) as txt_file:
    txtreader = csv.reader(txt_file, delimiter =";")
    for row in txtreader:
        game_id = int(row[0].split(": ")[0].replace("Game ",""))
        output_per_game[game_id] = {}
        row[0] = row[0].replace("Game " + str(game_id) + ": ", "")
        output_per_game[game_id] = {}
        for throw in row:
            color_throw = throw.split(", ")
            for option in color_throw:
                number_color = option.lstrip().split(" ")
                number = number_color[0]
                color = number_color[1]
                if color in output_per_game[game_id].keys():
                    if int(number) > output_per_game[game_id][color]:
                        output_per_game[game_id][color] = int(number)
                else:
                    output_per_game[game_id][color] = int(number)
        sum_of_all_game_ids = sum_of_all_game_ids + int(game_id)
power_per_game = {}
for game_id in output_per_game.keys():
    power_per_game[game_id] = 1
    for color in output_per_game[game_id]:
        power_per_game[game_id] = power_per_game[game_id] * output_per_game[game_id][color]
print(sum(power_per_game.values()))
