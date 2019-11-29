def press_capsule_button(time, discs):
    for disc in discs:
        time += 1
        new_position = (disc['start_pos'] + time) % disc['no_positions']
        if(new_position != 0):
            return False
    return True             # All discs had position 0 when the capsule passed

# Obtain and parse input
input = [l.strip().split() for l in open('2016/Day15/input.txt', 'r').readlines()]
discs = []
for row in input:
    dict = {
            'disc_num': row[1],
            'no_positions': int(row[3]),
            'start_pos': int(row[11][:-1])
            }
    discs.append(dict)

# First star
successfull_drop = False
time = 0
while(not successfull_drop):
    if(press_capsule_button(time, discs)):
        successfull_drop = True
        print('[part1] The first time the button can be pressed to get a capsule is {}'.format(time))
    time += 1

# Second star
dict = {
        'disc_num': '#7',
        'no_positions': 11,
        'start_pos': 0
        }
discs.append(dict)
successfull_drop = False
time = 0
while(not successfull_drop):
    if(press_capsule_button(time, discs)):
        successfull_drop = True
        print('[part2] The first time the button can be pressed to get a capsule is {}'.format(time))
    time += 1
