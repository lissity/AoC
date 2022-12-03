import math

def letter_to_priority(letter):
    if letter.islower():
        return ord(letter)-96           # a-z 1-26
    if letter.isupper():
        return ord(letter)-65+27        # A-Z 27-52

# Obtain input
puzzle_input = [line.strip() for line in open('2022/Day03/input.txt').readlines()]
parsed_input = []
for line in puzzle_input:
    middle_index = math.floor(len(line)/2)
    parsed_input.append([line[:middle_index], line[middle_index:]])

# Part 1
priority_sum = 0
for items in parsed_input:
    common_item = [item for item in items[0] if item in items[1]]
    priority_sum +=letter_to_priority(common_item[0])

print(f'Part 1: The sum of the priorities is {priority_sum}')

# Part 2
priority_sum = 0
for i in range(0, len(puzzle_input), 3):
    bag1 = puzzle_input[i]
    bag2 = puzzle_input[i+1]
    bag3 = puzzle_input[i+2]

    # Find common items between bags
    common_item = [item for item in bag1 if item in bag2 and item in bag3]
    priority_sum +=letter_to_priority(common_item[0])

print(f'Part 2: The sum of the priorities is {priority_sum}')
