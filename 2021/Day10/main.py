import statistics

# Obtain puzzle input
with open('2021/Day10/input.txt', 'r') as file:
    puzzle_input = [line.strip() for line in file.readlines()]

pairs_open = { ')' : '(', ']' : '[', '}' : '{', '>' : '<'}
pairs_close = { '(' : ')', '[' : ']', '{' : '}', '<' : '>'}
score_table_p1 = { ')' : 3, ']' : 57, '}' : 1197, '>' : 25137}
score_table_p2 = { ')' : 1, ']' : 2, '}' : 3, '>' : 4}

# Part 1 & 2
syntax_error_score = 0
autocomplete_scores = []
for row in puzzle_input:
    syntax_error_found = False
    stack = []
    for char in row:
        if char in ['(', '[', '{', '<']:
            stack.append(char)
        else:
            element = stack.pop()
            if (element != pairs_open[char]):               # Syntax error
                syntax_error_score += score_table_p1[char]
                syntax_error_found = True
                break
    if (not syntax_error_found and len(stack) != 0):        # Incomplete line
        autocomplete_chars = [pairs_close[c] for c in reversed(stack)]
        score = 0
        for i in autocomplete_chars:
            score *= 5
            score += score_table_p2[i]
        autocomplete_scores.append(score)

print(f'Part 1: The total syntax error score is {syntax_error_score}.')
print(f'Part 2: The middle of the autocomplete scores is '+
      f'{statistics.median(autocomplete_scores)}.')
