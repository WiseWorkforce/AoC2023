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
        throw_number = 1
        for throw in row:
            output_per_game[game_id][throw_number] = {}
            color_throw = throw.split(", ")
            for option in color_throw:
                number_color = option.lstrip().split(" ")
                number = number_color[0]
                color = number_color[1]
                if color in output_per_game[game_id]:
                    output_per_game[game_id][throw_number][color] = output_per_game[game_id][throw_number][color] + int(number)
                else:
                    output_per_game[game_id][throw_number][color] = int(number)
            throw_number = throw_number + 1
        sum_of_all_game_ids = sum_of_all_game_ids + int(game_id)
games_that_dont_pass = []

for game_id in output_per_game.keys():
    for throw_number in output_per_game[game_id]:
        for color_to_check in balls_per_color.keys():
            max_num_of_balls = balls_per_color[color_to_check]
            if color_to_check in output_per_game[game_id][throw_number].keys():
                if output_per_game[game_id][throw_number][color_to_check] > max_num_of_balls:
                    games_that_dont_pass.append(game_id)
print(sum_of_all_game_ids)
print(set(games_that_dont_pass))
print(sum_of_all_game_ids - sum(set(games_that_dont_pass)))