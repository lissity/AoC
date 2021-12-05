def update_diagram(point1, point2, diagram, consider_diagonal_lines):
    x1, y1, x2, y2 = point1[0], point1[1], point2[0], point2[1]
    if (x1 == x2):                                  # Vertical line
        if (y1 < y2):
            for i in range(y1, y2+1):
                add_point_in_diagram(x1, i)
        else:
            for i in range(y1, y2-1, -1):
                add_point_in_diagram(x1, i)
    if (y1 == y2):                                  # Horizontal line
        if (x1 < x2):
            for i in range(x1, x2+1):
                add_point_in_diagram(i, y1)
        else:
            for i in range(x1, x2-1, -1):
                add_point_in_diagram(i, y1)
    else:                                           # Diagonal line (Part 2)
        if (consider_diagonal_lines):
            if (x1 < x2 and y1 < y2):
                x, y = x1, y1
                for i in range(0, x2-x1+1):
                    add_point_in_diagram(x, y)
                    x += 1
                    y += 1
            if (x1 > x2 and y1 > y2):
                x, y = x2, y2
                for i in range(0, x1-x2+1):
                    add_point_in_diagram(x, y)
                    x += 1
                    y += 1
            if (x1 < x2 and y1 > y2):
                x, y = x1, y1
                for i in range(0, x2-x1+1):
                    add_point_in_diagram(x, y)
                    x += 1
                    y -= 1
            if (x1 > x2 and y1 < y2):
                x, y = x2, y2
                for i in range(0, x1-x2+1):
                    add_point_in_diagram(x, y)
                    x += 1
                    y -= 1

def add_point_in_diagram(x,y):
    if (x, y) in diagram:
        diagram[(x,y)] += 1
    else:
        diagram[(x,y)] = 1

# Obtain input
# Input will contain list of items in the format: [(x1, y1), (x2, y2)]
input = [line.strip().split(' -> ') for line in open('2021/Day05/input.txt', 'r',).readlines()]
input = [[tuple(map(int,item[0].split(','))), tuple(map(int, item[1].split(',')))] for item in input]

# Part 1
diagram = {}
for coords in input:
    update_diagram(coords[0], coords[1], diagram, False)

count = 0
for coord, value in diagram.items():
    if(value >= 2):
        count += 1
print(f'Part 1: At least two lines overlap in {count} points (considering ' +
      f'vertical and horizontal lines).')

# Part 2
diagram = {}
for coords in input:
    update_diagram(coords[0], coords[1], diagram, True)

count = 0
for coord, value in diagram.items():
    if(value >= 2):
        count += 1
print(f'Part 2: At least two lines overlap in {count} points (considering all' +
      f' lines).')