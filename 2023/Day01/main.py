import re

def get_str_num(strnum):
    number_translator = {'one': '1', 'two': '2', 'three': '3', 'four': '4',
                         'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 
                         'nine': '9'}
    if strnum.isdigit():
        return strnum
    else:
        return number_translator[strnum]

# Obtain input
numbers1 = []
numbers2 = []
for line in open('2023/Day01/input.txt', 'r').readlines():
    # Find all digits
    numbers1.append(re.findall(r'\d', line))
    
    # Find all digits, and specific words (one,two,...,nine). Uses lookahead assertion
    # to find overlapping matches (?=...). E.g. string 'sevenine' is ['seven', 'nine']
    numbers2.append(re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', line))

# Part 1
part1_sum = sum([(int(n[0] + n[-1])) for n in numbers1])
print(f"Part 1: The sum of calibration values is {part1_sum}.")

# Part 2
part2_num = sum([int(get_str_num(n[0]) + get_str_num(n[-1])) for n in numbers2])
print(f"Part 2: The sum of calibration values is {part2_num}.")
