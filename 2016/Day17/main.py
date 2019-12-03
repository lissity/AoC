import hashlib
import queue

class GameState:
    def __init__(self, position, path_taken_so_far):
        self.position = position
        self.path_taken_so_far = path_taken_so_far

def get_md5_first_4_chars(data):
    data = data.encode('utf-8')
    return hashlib.md5(data).hexdigest()[0:4]

puzzle_input = 'yjjvjgan'
open_door_codes = ['b', 'c', 'd', 'e', 'f']
paths_to_vault = []

start_state = GameState((0,0), '')
q = queue.Queue(0)
q.put(start_state)

while(not q.empty()):
    state = q.get()
    if(state.position == (3,3)):
        paths_to_vault.append(state.path_taken_so_far)
    else:
        door_status = get_md5_first_4_chars(puzzle_input + state.path_taken_so_far)
        if(door_status[0] in open_door_codes and state.position[1] > 0):      # Door above exists and is open
            new_position = (state.position[0], state.position[1]-1)
            newGS = GameState(new_position, state.path_taken_so_far + 'U')
            q.put(newGS)
        if(door_status[1] in open_door_codes and state.position[1] < 3):      # Door down exists and is open
            new_position = (state.position[0], state.position[1]+1)
            newGS = GameState(new_position, state.path_taken_so_far + 'D')
            q.put(newGS)
        if(door_status[2] in open_door_codes and state.position[0] > 0):      # Door left exists and is open
            new_position = (state.position[0]-1, state.position[1])
            newGS = GameState(new_position, state.path_taken_so_far + 'L')
            q.put(newGS)
        if(door_status[3] in open_door_codes and state.position[0] < 3):      # Door right exists and is open
            new_position = (state.position[0]+1, state.position[1])
            newGS = GameState(new_position, state.path_taken_so_far + 'R')
            q.put(newGS)

print('[part1] The shortest path to the vault door is {}'.format(paths_to_vault[0]))
print('[part2] The length of the longest path to the vault door is {}' \
      .format(len(max(paths_to_vault, key=len))))
