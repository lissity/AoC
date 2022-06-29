import math

def divide_list(input_list, instructions):
    tmp_list = input_list.copy()
    for char in instructions:
        middle_index = len(tmp_list)//2
        if char in ['B', 'R']:
            tmp_list = tmp_list[middle_index:]
        elif char in ['F', 'L']:
            tmp_list = tmp_list[:middle_index]
    return tmp_list[0]

# Obtain input
seats = [line.strip() for line in open('2020/Day05/input.txt', 'r').readlines()]

# Part 1
seat_ids = []
for seat in seats:
    row = divide_list([*range(0,128)], seat[:7])
    col = divide_list([*range(0,8)], seat[7:])
    seat_ids.append(row*8+col)

print(f'Part 1: The highest seat ID is {max(seat_ids)}.')

# Part 2
seat_ids.sort()
for i in range(1, len(seat_ids)-1):
    if seat_ids[i+1] != seat_ids[i]+1:
        my_seat_id = seat_ids[i]+1
        break

print(f'Part 2: The ID of my seat is {my_seat_id}.')
