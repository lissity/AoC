import collections

def validate_room(name, chksum):
    char_counter = collections.Counter(name)
    sorted_x = sorted(char_counter.items(), key=lambda x: (-x[1], x[0]))
    room_value = ''.join([tup[0] for tup in sorted_x[:5]])
    return room_value == chksum

def decrypt_name(name, shift):
    plain_text = ''
    for char in name:
        plain_text += chr((ord(char) - 97 + shift) % 26 + 97)
    return plain_text

# Obtain and parse input
lines = [l.strip() for l in open('2016/Day04/input.txt','r').readlines()]
input = []
for line in lines:
    chksum = line[-6:-1:1]
    id = int(line.split('-')[-1][:-7])
    name = ''.join(line.split('-')[:-1])
    dict = {'name': name, 'id': id, 'chksum': chksum}
    input.append(dict)

# First star
sum_of_ids = 0
real_rooms = []
for inp in input:
    if(validate_room(inp['name'], inp['chksum'])): # Check if room is real
        real_rooms.append(inp)
        sum_of_ids += inp['id']
print('[part1] The sum of sector IDs of the real rooms is {}'.format(sum_of_ids))

# Second star
for room in real_rooms:
    decrypted_name = decrypt_name(room['name'], room['id'])
    if(decrypted_name.find('north') is not -1):
        print('[part2] The room "{}" have section ID {} '.format(decrypted_name, room['id']))
