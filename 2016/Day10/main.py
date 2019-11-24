import re
import numpy

def bot_has_two_items(bots):
    for key, value in bots.items():
        if(len(value) == 2):
            return True
    return False

input = [l.strip() for l in open('2016/Day10/input.txt','r').readlines()]

bot_num_pattern = re.compile('bot (\d+)')
output_num_pattern = re.compile('output (\d+)')
initial_values = []
bot_instruction = {}
bot_numbers = []
output_numbers = []
for row in input:
    # Finds all bot and output numbers that exists in the input
    bot_numbers += [int(num) for num in re.findall(bot_num_pattern, row)]
    output_numbers += [int(num) for num in re.findall(output_num_pattern, row)]
    # Parse the instructions
    row = row.split()
    if(row[0] == 'value'):
        dict = {'value': int(row[1]), 'bot': int(row[5])}
        initial_values.append(dict)
    elif(row[0] == 'bot'):
        dict = {}
        if(row[5] == 'bot'):
            dict['low'] = ['bot', int(row[6])]
        elif(row[5] == 'output'):
            dict['low'] = ['output', int(row[6])]
        if(row[10] == 'bot'):
            dict['high'] = ['bot', int(row[11])]
        elif(row[10] == 'output'):
            dict['high'] = ['output', int(row[11])]
        bot_instruction[int(row[1])] = dict

# Remove duplicates and sort
bot_numbers = sorted(list(set(bot_numbers)))
output_numbers = sorted(list(set(output_numbers)))

# Create the bots
bots = {}
for num in bot_numbers:
    bots[num] = []

# Give bots the initial values
for dict in initial_values:
    bots[dict['bot']].append(dict['value'])

# Create the empty outputs
outputs = {}
for num in output_numbers:
    outputs[num] = []

# Keep looping until no bots have 2 items
while(bot_has_two_items(bots)):
    for key, value in bots.items():
        if(len(value) == 2):
            low_type = bot_instruction[key]['low'][0]
            low_num = bot_instruction[key]['low'][1]
            high_type = bot_instruction[key]['high'][0]
            high_num = bot_instruction[key]['high'][1]

            if((value[0] == 61 and value[1]==17) or
                value[0] == 17 and value[1]==61):
                print('[part1] Bot {} is comparing {} with {}'.format(key, value[0], value[1]))

            value = sorted(value)
            low_value = value[0]
            high_value = value[1]

            if(low_type == 'bot'):
                bots[low_num].append(low_value)
            elif(low_type == 'output'):
                outputs[low_num].append(low_value)

            if(high_type == 'bot'):
                bots[high_num].append(high_value)
            elif(high_type == 'output'):
                outputs[high_num].append(high_value)
            bots[key] = []      # Chips are given away -> reset current bot's list

output_chips = outputs[0] + outputs[1] + outputs[2]
print('[part2] The product of the chips in output 0, 1, and 2 is {}'.format(numpy.prod(output_chips)))
