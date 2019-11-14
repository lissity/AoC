from llist import dllist, dllistnode

#Part 1
def next_player(current_player):
    if(current_player==431):
        return 0
    else:
        return current_player + 1
def add_marble_to_circle(marble_circle, marble_number, current_marble_index):
    length = len(marble_circle)
    if(length == 0):
        marble_circle.append(marble_number)
        return marble_circle, 0
    elif(length == 1):
        marble_circle.append(marble_number)
        return marble_circle, 1
    elif((current_marble_index + 2) < length ):
        marble_circle.insert(current_marble_index + 2, marble_number)
        return marble_circle, current_marble_index +2
    elif((current_marble_index+2) == length):
        marble_circle.append(marble_number)
        return marble_circle, current_marble_index+2
    elif((current_marble_index + 2) > length):
        new_i = (current_marble_index + 2) % length
        marble_circle.insert(new_i, marble_number)
        return marble_circle, new_i
def take_marble_from_circle(marble_circle, current_marble_index):
    if (current_marble_index - 7 >= 0):
        points = marble_circle[current_marble_index-7]
        del marble_circle[current_marble_index-7]
        current_marble_index = current_marble_index-7
        return points, marble_circle, current_marble_index
    else:
        new_i = len(marble_circle) + (current_marble_index - 7)
        points = marble_circle[new_i]
        del marble_circle[new_i]
        current_marble_index = new_i
        return points, marble_circle, current_marble_index
input = '432 players; last marble is worth 71019 points'
no_players = 432
last_marble_worth = 71019

marble_circle = list()
next_marble = 0
current_marble_index = 0
elf_scores = list()
current_player = 0
for i in range(no_players):
    elf_scores.append(0)

for i in range(last_marble_worth-1):
    if(next_marble !=0 and next_marble % 23 == 0):
        elf_scores[current_player] += next_marble
        points, marble_circle, current_marble_index = take_marble_from_circle(marble_circle,
                                                                      current_marble_index)
        elf_scores[current_player] += points
        next_marble +=1
        current_player = next_player(current_player)
    else:
        marble_circle, current_marble_index = add_marble_to_circle(marble_circle,
                                             next_marble,
                                             current_marble_index)
        next_marble += 1
        current_player = next_player(current_player)
print('Winner score (list): ' + str(max(elf_scores)))

#Part 2
def move_in_dll(list, steps, current):
    if(steps > 0):
        for i in range(steps):
            if(current.next != None):
                current = current.next
            else:
                current = list.first
    elif(steps < 0):
        for i in range(abs(steps)):
            if(current.prev != None):
                current = current.prev
            else:
                current = list.last
    return current
def add_marble_to_circle_dll(marble_circle, marble_number, current_marble):
    length = marble_circle.size
    if(length == 0):
        current_marble = marble_circle.append(marble_number)
        return marble_circle, current_marble
    elif(length == 1):
        current_marble = marble_circle.append(marble_number)
        return marble_circle, current_marble
    #elif(length == 2):
    #    current_marble = marble_circle.insert(marble_number, current_marble)
    #    return marble_circle, current_marble
    else:
        before_node = move_in_dll(marble_circle, 2, current_marble)
        current_marble = marble_circle.insert(marble_number, before_node)
        return marble_circle, current_marble
def take_marble_from_circle_dll(marble_circle, current_marble):
    remove_marble = move_in_dll(marble_circle, -7, current_marble)
    current_marble = move_in_dll(marble_circle, 1, remove_marble)
    points = remove_marble.value
    marble_circle.remove(remove_marble)
    return points, marble_circle, current_marble

no_players = 432
last_marble_worth = 71019*100
marble_circle = dllist()
next_marble = 0
current_marble = dllistnode()
elf_scores = list()
current_player = 0
for i in range(no_players):
    elf_scores.append(0)

for i in range(last_marble_worth-1):
    if(next_marble !=0 and next_marble % 23 == 0):
        elf_scores[current_player] += next_marble
        points, marble_circle, current_marble = take_marble_from_circle_dll(marble_circle,
                                                                            current_marble)
        elf_scores[current_player] += points
        next_marble +=1
        current_player = next_player(current_player)
    else:
        marble_circle, current_marble = add_marble_to_circle_dll(marble_circle,
                                             next_marble,
                                             current_marble)
        next_marble += 1
        current_player = next_player(current_player)

print('Winner score (dll): ' + str(max(elf_scores)))
