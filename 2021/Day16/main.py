import numpy as np

version_sum = 0

def hex_to_binary(hex):
    hex_to_bin = {'0' : '0000', '1' : '0001', '2' : '0010', '3' : '0011', '4' : '0100',
              '5' : '0101', '6' : '0110', '7' : '0111', '8' : '1000', '9' : '1001',
              'A' : '1010', 'B' : '1011', 'C' : '1100', 'D' : '1101', 'E' : '1110',
              'F' : '1111'}
    binary_str = []
    for char in hex:
        binary_str.append(hex_to_bin[char])
    return ''.join(binary_str)

def parse_literal(binary, index):
    bits = []
    while(True):
        group_prefix = binary[index]
        index += 1
        bits.append(binary[index:index+4])
        index += 4
        if group_prefix == '0':      # The last bit group was just added - break
            break
    return index, int(''.join(bits), 2)

def parse_packet(binary, start_index, stop_index):
    global version_sum
    
    # Read Header
    index = start_index
    version = int(binary[index:index+3],2)
    index += 3
    type_id = int(binary[index:index+3],2)
    index += 3
    version_sum += version          # Sum of versions for Part 1

    if (type_id == 4):      # Literal
        index, literal = parse_literal(binary, index)
        return index, literal
    else:                   # Operator
        length_type_id = binary[index]
        index += 1
        sub_packet_values = []
        if (length_type_id == '0'):         # total length in bits
            bit_length = int(binary[index:index+15],2)
            index += 15
            stop = index + bit_length
            while(index < stop):
                index, value = parse_packet(binary, index, stop)
                sub_packet_values.append(value)
        elif (length_type_id == '1'):       # number of sub-packets
            number_of_subpackets = int(binary[index:index+11],2)
            index += 11
            for _ in range(number_of_subpackets):
                index, value = parse_packet(binary, index, stop_index)
                sub_packet_values.append(value)
        value = 0
        if(type_id == 0):                   # Sum packet
            value = sum(sub_packet_values)
        elif (type_id == 1):                # Product packet
            value = np.prod(sub_packet_values, dtype=np.longlong)
        elif (type_id == 2):                # Minimum packet
            value = min(sub_packet_values)
        elif (type_id == 3):                # Maximum packet
            value = max(sub_packet_values)
        elif (type_id == 5):                # Greater than packet
            value = 1 if sub_packet_values[0] > sub_packet_values[1] else 0
        elif (type_id == 6):                # Less than packet
            value = 1 if sub_packet_values[0] < sub_packet_values[1] else 0
        elif (type_id == 7):                # Equal to packet
            value = 1 if sub_packet_values[0] == sub_packet_values[1] else 0
        return index, value

# Obtain puzzle input
with open('2021/Day16/input.txt', 'r') as file:
    puzzle_input = file.readline().strip()
binary_data = hex_to_binary(puzzle_input)

# Part 1 & 2
index, value = parse_packet(binary_data, 0, len(binary_data))
print(f'Part 1: The sum of the version numbers is {version_sum}.')
print(f'Part 2: The value of the outermost packet is {value}.')
