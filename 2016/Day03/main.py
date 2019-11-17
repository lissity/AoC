def check_valid_triangle(side1, side2, side3):
    if ((side1 + side2) <= side3 or
        (side1 + side3) <= side2 or
        (side2 + side3) <= side1):
        return False
    else:
        return True

# Obtain instructions
input = [l.strip().split() for l in open('2016/Day03/input.txt', 'r').readlines()]
#---- First star ----#
valid_triangles = 0
for inp in input:
    if(check_valid_triangle(int(inp[0]), int(inp[1]), int(inp[2]))):
        valid_triangles += 1
print('[part1] There are {} possible triangles in the input'.format(valid_triangles))

#---- Second star ----#
# Rearrange input
col1 = []
col2 = []
col3 = []
for inp in input:
    col1.append(inp[0])
    col2.append(inp[1])
    col3.append(inp[2])
input2 = col1 + col2 + col3

valid_triangles = 0
for i in range(0, len(input2), 3):
    if(check_valid_triangle(int(input2[i]), int(input2[i+1]), int(input2[i+2]))):
        valid_triangles += 1
print('[part2] There are {} possible triangles in the rearranged input'.format(valid_triangles))
