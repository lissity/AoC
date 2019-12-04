def check_adjacent_digits(num):
    pair_found = False
    for i in range(len(num)-1):
        if(num[i] == num[i+1]):
            pair_found = True
            break
    return pair_found

def check_never_decrease(num):
    for i in range(1, len(num)):
        if(num[i-1] > num[i]):
            return False
    return True

def check_adjacent_digits_version_2(num):
    pair_found = False
    for i in range(len(num)-1):
        if(num[i] == num[i+1]):         # Pair was found
            # Check if the pair is not part of a largers group of matching digits
            if(not (i-1 >= 0 and num[i-1] == num[i]) and not (i+2 < len(num) and num[i+2] == num[i])):
               pair_found = True
               break
    return pair_found

# Puzzle input
num_range = (128392, 643281)

# First star
possible_password_counter = 0
for i in range(num_range[0], num_range[1]):
    if(check_adjacent_digits(str(i)) and check_never_decrease(str(i))):
        possible_password_counter += 1

print('[part1] The number of passwords that meet the criteria is {}'\
      .format(possible_password_counter))

# Second star
possible_password_counter = 0
for i in range(num_range[0], num_range[1]):
    if(check_adjacent_digits_version_2(str(i)) and check_never_decrease(str(i))):
        possible_password_counter += 1

print('[part2] The number of passwords that meet the criteria is {}'\
       .format(possible_password_counter))
