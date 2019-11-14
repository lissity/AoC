def check_vowels(string):
    vowels = ['a','e','i','o','u']
    vowel_count = 0
    for char in string:
        if(char in vowels):
            vowel_count += 1
    if(vowel_count >= 3):
        return True
    else:
        return False

def check_double_letter(string):
    index = 0
    double_letter_found = False
    for char in range(0, len(string)-1):
        next_char = string[char+1]
        if(string[char] == next_char):
            double_letter_found = True
            break
        index += 1
    return double_letter_found

def check_disallowed_combination(string):
    disallowed = ['ab', 'cd', 'pq', 'xy']
    index = 0
    disallowed_ok = True
    for char in range(0, len(string)-1):
        next_char = string[char+1]
        combo = string[char] + next_char
        if combo in disallowed:
            disallowed_ok = False
            break
        index += 1
    return disallowed_ok

def check_two_pairs(string):
    two_pairs_found = False
    pairs = dict()
    for i in range(0, len(string), 2):
        pair = string[i] + string[i+1]
        pairs[(i,i+1)] = pair
    for i in range(1, len(string)-1, 2):
        pair = string[i] + string[i+1]
        pairs[(i,i+1)] = pair
    for pair in pairs:
        current_index = pair
        current_combo = pairs[pair]
        for pair2 in pairs:
            if pairs[pair] == pairs[pair2] and\
               pair[1] != pair2[0] and\
               pair[0] != pair2[1] and\
               pair[0] != pair2[0] and \
               pair[1] != pair2[1]:
                two_pairs_found = True
                break
    return two_pairs_found

def check_repeat_letter(string):
    repeat_found = False
    for i in range(0, len(string)-2):
        if(string[i] == string[i+2]):
            repeat_found = True
            break
    return repeat_found

input = open('2015/Day5/input.txt', 'r').read().splitlines()
# Part 1
nice_strings = 0
for string in input:
    if (check_vowels(string) and \
    check_double_letter(string) and \
    check_disallowed_combination(string)):
        nice_strings +=1

print('Nice strings: ' + str(nice_strings))

# Part 2
nice_strings = 0
for string in input:
    if(check_two_pairs(string) and check_repeat_letter(string)):
        nice_strings += 1

print('Nice strings: ' + str(nice_strings))
