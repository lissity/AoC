import re

def repeat_data(marker, input, decompressed_data):
    marker = marker.strip('()')
    no_chars = int(marker.split('x')[0])
    repeat = int(marker.split('x')[1])
    decompressed_data += input[0:no_chars]*repeat
    return decompressed_data, no_chars

def recursive_repeat(input, current_pos, end_pos):
    len_sum = 0
    marker_pattern = re.compile('\(.*?\)')
    match = re.search(marker_pattern, input[current_pos:end_pos])
    if(match is None):
        return len_sum + len(input[current_pos:end_pos])
    else:
        while(match is not None):
            # Gather marker length, and values
            marker_len = len(match.group())
            marker = match.group().strip('()')
            no_chars = int(marker.split('x')[0])
            repeat = int(marker.split('x')[1])

            if(match.span()[0] is not 0):   # Marker is not at beggining of input
                len_sum += match.span()[0]
                current_pos += match.span()[0]
            current_pos += marker_len
            len_sum += recursive_repeat(input, current_pos, current_pos+no_chars)*repeat
            current_pos += no_chars
            match = re.search(marker_pattern, input[current_pos:end_pos])
        return len_sum + (end_pos-current_pos)

# Obtain input
input = open('2016/Day09/input.txt').readline().strip()

# First star
marker_pattern = re.compile('\(.*?\)')
decompressed = ''
pos = 0
while(pos < len(input)):
    match = re.search(marker_pattern, input[pos:])
    if (match is not None and match.span()[0] == 0):
        pos += match.span()[1]      # Update current position to start after marker
        decompressed, no_chars = repeat_data(match.group(), input[pos:], decompressed)
        pos += no_chars
    else:
        decompressed += input[pos]
        pos += 1
print('[part1] The decompressed length is {}'.format(len(decompressed)))

# Second star
decmpr_len = recursive_repeat(input, 0, len(input))
print('[part2] The decompressed length using the improved format is {}'.format(decmpr_len))
