import fnmatch
import copy
import itertools
import queue

class Node:
    def __init__(self, gamestate, parent, level):
        self.gamestate = gamestate
        self.parent = parent
        self.level = level

def print_game_state(floor_state):
    print('Game State')
    print('F4',floor_state[3])
    print('F3',floor_state[2])
    print('F2',floor_state[1])
    print('F1',floor_state[0])
    print('\n')

def check_game_state(floor_state):
    for floor in floor_state:
        # If there is a *G on the floor, are there xG for all xM on the floor?
        # Then return True, else False
        generators = fnmatch.filter(floor, '?G')
        microchips = fnmatch.filter(floor, '?M')
        if(generators):         # If generator list is not empty
            for chip in microchips:
                corresponding_generator = chip[0] + 'G'
                if(corresponding_generator not in generators):
                    return False
    return True

def game_state_2_string(floor_state):
    game_state_str = ''
    for floor in floor_state:
        floor_list = []
        for item in floor:
            if(item == 'E'):
                floor_list.append(item)
            else:
                # Only G or M is added to gamestate string, since pairs are interchangable.
                # e.g. (F1: HG,HM F2: LG,LM) is the same as (F1: LG,LM F2: HG,HM)
                # when it comes to how many steps are needed to get all items to the top floor.
                floor_list.append(item[1])
        floor_list.sort()
        game_state_str += ''.join(floor_list)
        game_state_str += ','
    return game_state_str

def get_elevator_level(floor_state):
    for i in range(0, len(floor_state)):
        if('E' in floor_state[i]):
            return i

def go_up(floor_state, item1, item2):
    level = get_elevator_level(floor_state)
    if(('E' in floor_state[3]) or       # Elevator is already at top floor
       (item1 == '' and item2=='') or   # Atleast one item must be brought
       ((item1 is not '') and (item1 not in floor_state[level])) or         # Items are not on the current level
       ((item2 is not '') and (item2 not in floor_state[level]))):
        return False, floor_state
    floor_state_copy = copy.deepcopy(floor_state)
    new_level = level + 1
    floor_state_copy[new_level].append('E')
    floor_state_copy[level].remove('E')
    if(item1 is not ''):
        floor_state_copy[new_level].append(item1)
        floor_state_copy[level].remove(item1)
    if(item2 is not ''):
        floor_state_copy[new_level].append(item2)
        floor_state_copy[level].remove(item2)
    if(check_game_state(floor_state_copy)):
        return True, floor_state_copy
    else:
        return False, floor_state_copy

def go_down(floor_state, item1, item2):
    level = get_elevator_level(floor_state)
    if(('E' in floor_state[0]) or       # Elevator is already at bottom floor
       (item1 == '' and item2=='') or   # Atleast one item must be brought
       ((item1 is not '') and (item1 not in floor_state[level])) or         # Items are not on the current level
       ((item2 is not '') and (item2 not in floor_state[level]))):
        return False, floor_state
    floor_state_copy = copy.deepcopy(floor_state)
    new_level = level - 1
    floor_state_copy[new_level].append('E')
    floor_state_copy[level].remove('E')
    if(item1 is not ''):
        floor_state_copy[new_level].append(item1)
        floor_state_copy[level].remove(item1)
    if(item2 is not ''):
        floor_state_copy[new_level].append(item2)
        floor_state_copy[level].remove(item2)
    if(check_game_state(floor_state_copy)):
        return True, floor_state_copy
    else:
        return False, floor_state_copy

def get_item_combinations(floor_state):
    combos = []
    current_level = get_elevator_level(floor_state)
    level_items = floor_state[current_level].copy()
    level_items.remove('E')
    level_items.append('')
    return list(itertools.combinations(level_items, 2))

def check_win(floor_state):
    for i in range(0, len(floor_state)-1):
        if(floor_state[i]):
            return False
    return True

def create_valid_child(func_name, arg1, arg2, current_node, node_queue, seen_gamestates):
    valid, new_state = func_name(current_node.gamestate, arg1, arg2)
    gamestate_str = game_state_2_string(new_state)
    if(valid and (gamestate_str not in seen_gamestates)):
        new_child = Node(new_state, current_node, current_node.level+1)
        node_queue.put(new_child)
        seen_gamestates[gamestate_str] = True

# Part1
floor_state = [[],[],[],[]]
floor_state[0] = ['E', 'PG', 'PM']
floor_state[1] = ['CG', 'KG', 'RG', 'LG']
floor_state[2] = ['CM', 'KM', 'RM', 'LM']
floor_state[3] = []

q = queue.Queue(0)
root = Node(floor_state, None, 0)
q.put(root)
seen_gamestates = {}    # used for pruning already seen game states.
seen_gamestates[game_state_2_string(floor_state)] = True

while(not q.empty()):
    current_node = q.get()
    if(check_win(current_node.gamestate)):
        print('[part1] The minimum number of steps to bring all items to the '
              '4th floor is {}'.format(current_node.level))
        break
    # Try different moves and create a child for each valid move
    arg_combos = get_item_combinations(current_node.gamestate)
    for combo in arg_combos:
        create_valid_child(go_up, combo[0], combo[1], current_node, q, seen_gamestates)
        create_valid_child(go_down, combo[0], combo[1], current_node, q, seen_gamestates)


# Part2
floor_state = [[],[],[],[]]
floor_state[0] = ['E', 'PG', 'PM', 'EG', 'EM', 'DG', 'DM']
floor_state[1] = ['CG', 'KG', 'RG', 'LG']
floor_state[2] = ['CM', 'KM', 'RM', 'LM']
floor_state[3] = []

# Initialize values
q = queue.Queue(0)
root = Node(floor_state, None, 0)
q.put(root)
seen_gamestates = {}    # used for pruning already seen game states.
seen_gamestates[game_state_2_string(floor_state)] = True

while(not q.empty()):
    current_node = q.get()
    if(check_win(current_node.gamestate)):
        print('[part2] The minimum number of steps to bring all items to the '
              '4th floor is {}'.format(current_node.level))
        break
    # Try different moves and create a child for each valid move
    arg_combos = get_item_combinations(current_node.gamestate)
    for combo in arg_combos:
        create_valid_child(go_up, combo[0], combo[1], current_node, q, seen_gamestates)
        create_valid_child(go_down, combo[0], combo[1], current_node, q, seen_gamestates)
