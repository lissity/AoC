import json
from functools import cmp_to_key

def compare_values(a, b):
    if isinstance(a, int) and isinstance(b, int):   # a and b are both ints
        if a < b:
            return 1        # right order
        if b < a:
            return -1       # wrong order
        return 0            # continue checking next input

    elif isinstance(a, list) and isinstance(b, list):   # a and b are lists
        if len(b) < len(a):
            for i in range(len(b)):
                ret = compare_values(a[i], b[i])
                if ret == 1 or ret == -1:
                    return ret
            return -1   # Right list ran out of items -> wrong order
        else:
            for i in range(len(a)):
                ret = compare_values(a[i], b[i])
                if ret == 1 or ret == -1:
                    return ret
            if len(a) == len(b):
                return 0    # Continue checking next input
            return 1    #  Left list ran out of item -> right order

    else: # Exactly one of a and b is an int, convert it to a list and compare
        if isinstance(a, int):
            a = [a]
        else:
            b = [b]
        return compare_values(a,b)

# Obtain input
puzzle_input = [packet.split('\n') for packet in open('2022/Day13/input.txt').read().split('\n\n')]

# Part 1
right_order_indices = []
packet_index = 1
for packet_pair in puzzle_input:
    p1 = json.loads(packet_pair[0])
    p2 = json.loads(packet_pair[1])
    result = compare_values(p1, p2)
    if result == 1:
        right_order_indices.append(packet_index)
    packet_index += 1

print(f'Part 1: The sum of indices of the pairs in the right order is {sum(right_order_indices)}.')

# Part 2
packets = [json.loads(line.strip()) 
           for line in open('2022/Day13/input.txt').readlines()
           if line != '\n']
d1 = [[2]]
d2 = [[6]]
packets.extend([d1,d2])
sorted_packets = list(reversed(sorted(packets, key=cmp_to_key(compare_values))))
decoder_key = (sorted_packets.index(d1)+1) * (sorted_packets.index(d2)+1)

print(f'Part 2: The decoder key is {decoder_key}.')
