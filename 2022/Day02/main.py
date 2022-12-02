def game_score(move1, move2):
    if (move1 == move2):                        # Draw = 3 points
        return 3
    if (move1 == 'A' and (move2 == 'C') or      # Rock vs Scissors
        move1 == 'B' and (move2 == 'A') or      # Paper vs Rock
        move1 == 'C' and (move2 == 'B')):       # Scissors vs Paper
        return 6                                # Win = 6 points
    else:
        return 0                                # Loss = 0 points

def get_move(move1, result):
    if result == 'Y':       # Draw
        return move1
    
    if (move1 == 'A' and result == 'X'):
        return 'C'
    if (move1 == 'A' and result == 'Z'):
        return 'B'

    if (move1 == 'B' and result == 'X'):
        return 'A'
    if (move1 == 'B' and result == 'Z'):
        return 'C'
    
    if (move1 == 'C' and result == 'X'):
        return 'B'
    if (move1 == 'C' and result == 'Z'):
        return 'A'

# Obtain input
strategy = [line.strip().split(' ') for line in open('2022/Day02/input.txt').readlines()]

# 1 for Rock (A), 2 for Paper(B), and 3 for Scissors(C)
score_map = { 'A' : 1, 'B' : 2, 'C' : 3}
move_translate_map = {'X' : 'A', 'Y': 'B', 'Z' : 'C'}

# Part 1
total_score = 0
for round in strategy:
    opponent_move = round[0]
    my_move = move_translate_map[round[1]]
    total_score += score_map[my_move] + game_score(my_move, opponent_move)

print(f'Part 1: The total score would be {total_score}')

# Part 2
result_score_map = { 'X' : 0, 'Y' : 3, 'Z' : 6}    # X = lose, Y = draw, Z = win

total_score = 0
for round in strategy:
    opponent_move = round[0]
    round_result = round[1]
    my_move = get_move(opponent_move, round_result)
    total_score += score_map[my_move] + result_score_map[round_result]

print(f'Part 2: The total score would be {total_score}')