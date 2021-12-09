def create_translation_map(signal_patterns):
    signal_patterns = [''.join(sorted(pattern)) for pattern in signal_patterns]
    translation = {}

    # Finding translation for 1, 4 , 7, and 8 which have unique number of segments
    translation[1] = [sp for sp in signal_patterns if len(sp) == 2][0]
    translation[4] = [sp for sp in signal_patterns if len(sp) == 4][0]
    translation[7] = [sp for sp in signal_patterns if len(sp) == 3][0]
    translation[8] = [sp for sp in signal_patterns if len(sp) == 7][0]
    for i in [1,4,7,8]:
        signal_patterns.remove(translation[i])
    
    # Finding translation for 3 (5 segements and contains the same segments as 1)
    for sp in signal_patterns:
        if (len(sp) == 5 and translation[1][0] in sp and translation[1][1] in sp):
            translation[3] = sp
    signal_patterns.remove(translation[3])

    # Finding translation for 9 (6 segements and contains the same segments as 4)
    char_list = []
    char_list[:0] = translation[4]
    for sp in signal_patterns:
        if(len(sp) == 6 and all([char in sp for char in char_list])):
            translation[9] = sp
    signal_patterns.remove(translation[9])

    # Finding translation for 6 (6 segments and contains one of 1's segment)
    char_list = []
    char_list[:0] = translation[1]
    for sp in signal_patterns:
        if(len(sp) == 6 and sum([char in sp for char in char_list]) == 1):
            translation[6] = sp
    signal_patterns.remove(translation[6])

    # Finding translation for 0 (The only pattern left with 6 segments)
    translation[0] = [sp for sp in signal_patterns if len(sp) == 6][0]
    signal_patterns.remove(translation[0])
    
    # Finding translation for 5 (5 segments and contains five of 6's segments)
    char_list = []
    char_list[:0] = translation[6]
    for sp in signal_patterns:
        if(len(sp) == 5 and sum([char in sp for char in char_list]) == 5):
            translation[5] = sp
    signal_patterns.remove(translation[5])

    # Finding translation for 2 (The only pattern left with 5 segments)
    translation[2] = [sp for sp in signal_patterns if len(sp) == 5][0]
    signal_patterns.remove(translation[2])

    # Swapping keys and values in dictionary
    translation = {value:key for key, value in translation.items()}
    return translation

def translate_output(value, translation):
    value = [''.join(sorted(pattern)) for pattern in value]
    return int(''.join([str(translation[pattern]) for pattern in value]))

# Obtain puzzle input
with open('2021/Day08/input.txt','r') as file:
    lines = file.readlines()
    puzzle_input = [line.strip().split(' | ') for line in lines]
    puzzle_input = [[entry[0].split(), entry[1].split()] for entry in puzzle_input]

# Part 1
count = 0                           # Number of times 1, 4, 7, or 8 appear
for entry in puzzle_input:
    tmp = len([p for p in entry[1] if len(p) in [2,4,3,7]])
    count += tmp
print(f'Part 1: The digits 1, 4, 7, and 8 appear {count} times in output values.')

# Part 2
output_sum = 0
for row in puzzle_input:
    translation = create_translation_map(row[0])
    num = translate_output(row[1], translation)
    output_sum += num
print(f'Part 2: The sum of output values is {output_sum}.')
