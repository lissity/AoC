import collections

# Obtain and arrange input
input = [line.strip() for line in open('2016/Day06/input.txt','r').readlines()]
columns = [[],[],[],[],[],[],[],[]]
for i in range(0,8):
    columns[i] = [x[i] for x in input]

# First star
message = ''
for i in range(0,8):
    char_counter = collections.Counter(columns[i])      # Count the characters
    message += char_counter.most_common(1)[0][0]        # Add the most common char to message
print('[part1] The error-corrected version of the message is "{}"'.format(message))

# Second star
message = ''
for i in range(0,8):
    char_counter = collections.Counter(columns[i])      # Count the characters
    message += char_counter.most_common()[-1][0]        # Add the least common char to message
print('[part2] The error-corrected version of the message is "{}"'.format(message))
