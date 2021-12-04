def mark_board(board, number):
    for row in board:
        for board_item in row:
            if (board_item[0] == number):
                board_item[1] = True

def check_if_bingo(board):
    # Check for bingo row
    for row in board:
        marked = [board_item[1] for board_item in row]
        if (all(marked)):
            return True
    # Check for bingo column
    for pos in range(0, len(board[0])):
        marked = [row[pos][1] for row in board]
        if (all(marked)):
            return True
    return False

def get_score(board):
    score = 0
    for row in board:
        score += sum([item[0] for item in row if item[1] == False])
    return score

def reset_board(board):
    for row in board:
        for item in row:
            item[1] = False

# Obtain input
with open('2021/Day04/input.txt', 'r') as f:
    numbers = list(map(int, f.readline().strip().split(',')))    # Drawn numbers
    boards = []
    board = []
    count = 0
    for line in f:
        if(line != '\n'):
            board_row_nums = list(map(int,line.strip().split()))
            board_row = []
            for num in board_row_nums:
                board_item = [num, False]
                board_row.append(board_item)
            board.append(board_row)
            count += 1
        else:
            count = 0
        if (count == 5):
            boards.append(board)
            board = []

# Part 1
for num in numbers:
    for board in boards:
        mark_board(board, num)
        if(check_if_bingo(board)):
            winning_board = board
            last_num = num
            break
    else:
        continue
    break

score = get_score(winning_board)
print(f'Part 1: The final score will be {score* last_num}')

# Part 2
boards2 = []
for board in boards:
    reset_board(board)
    boards2.append([board, False])

for num in numbers:
    for board in boards2:
        if (board[1] == False):
            mark_board(board[0], num)
            if(check_if_bingo(board[0])):
                last_winning_board = board
                last_num = num
                board[1] = True

score = get_score(last_winning_board[0])
print(f'Part 2: The final score will be {score* last_num}')