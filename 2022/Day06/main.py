# Obtain input
buffer = open('2022/Day06/input.txt').readline().strip()

start_of_packet = 0
start_of_message = 0
start_of_packet_found = False

for i in range(len(buffer)):
    if not start_of_packet_found:               # Part 1
        data4chars = list(buffer[i:i+4])
        data4chars_set = set(data4chars)
        if len(data4chars_set) == 4:            # Looking for 4 unique chars
            start_of_packet = i+4
            start_of_packet_found = True
    else:                                       # Part 2
        data14chars = list(buffer[i:i+14])
        data14chars_set = set(data14chars)
        if len(data14chars_set) == 14:          # Looking for 14 unique chars
            start_of_message = i+14
            break

print(f'Part 1: {start_of_packet} characters needs to be processed before the '
    + f'start-of-packet marker.')

print(f'Part 2: {start_of_message} characters needs to be processed before the '
    + f'start-of-message marker.')
