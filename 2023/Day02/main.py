import re

# Parse input
parsed_data = {}
for line in open('2023/Day02/input.txt', 'r').readlines():
    l = line.split(":")
    game_id = int(re.search(r'\d+', l[0]).group())
    game_info = l[1].split(';')
    rounds_info = []
    for game_round in game_info:
        game_round = game_round.replace(',','')
        gr = game_round.split()
        draw = {'red': 0, 'green': 0, 'blue': 0}
        for i in range(0, len(gr)-1, 2):
            number, color = int(gr[i]), gr[i+1]
            draw[color] = number
        rounds_info.append(draw.copy())
    parsed_data[game_id] = rounds_info

# Part 1
id_sum = 0
config = {'red': 12, 'green': 13, 'blue': 14}
for id, game_info in parsed_data.items():
    game_is_possible= True
    for round in game_info:
        if (round['red'] > config['red'] or
            round['green'] > config['green'] or
            round ['blue'] > config['blue']):
            game_is_possible = False
            break
    if game_is_possible:
        id_sum += id

print(f"Part 1: The sum of the IDs of the games that are possible is {id_sum}.")

# Part 2
power_sum = 0
for id, game_info in parsed_data.items():
    red, green, blue = [], [], []
    for round in game_info:
        red.append(round['red'])
        green.append(round['green'])
        blue.append(round['blue'])
    power_sum += max(red)*max(blue)*max(green)

print(f"Part 2: The sum of the power of the sets is {power_sum}.")
