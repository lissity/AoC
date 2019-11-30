def modified_dragon_curve(inital_state, required_length):
    state = inital_state
    while (len(state) < required_length):
        a = state
        b = ''.join([replace_bit(char) for char in reversed(a)])
        state = a + '0' + b
    return state[0:required_length]

def replace_bit(character):
    return '1' if character == '0' else '0'

def calc_checksum(input_str):
    temp_str = input_str
    while True:
        chk_sum = []                    # Note: Using a list is much faster - string concatenation is sloooow.
        for i in range(0, len(temp_str), 2):
            if(temp_str[i] == temp_str[i+1]):
                chk_sum.append('1')
            else:
                chk_sum.append('0')
        if(len(chk_sum) % 2 == 1):       # Length of checksum is odd -> stop
            break
        temp_str = chk_sum
    return ''.join(chk_sum)

initial_state = '01000100010010111'

# First star
disk_size = 272
longer_str = modified_dragon_curve(initial_state, disk_size)
print('[part1] The checksum is {}'.format(calc_checksum(longer_str)))

# Second star
disk_size = 35651584
longer_str = modified_dragon_curve(initial_state, disk_size)
print('[part2] The checksum is {}'.format(calc_checksum(longer_str)))
