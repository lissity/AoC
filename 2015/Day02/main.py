def get_outer_area(x, y, z):
    return x*y*2 + x*z*2 + y*z*2


def get_slack(x, y, z):
    values = sorted([x, y, z])
    return values[0] * values[1]


def get_ribbon_length(x, y, z):
    values = sorted([x, y, z])
    return values[0] * 2 + values[1] * 2


def get_bow_length(x, y, z):
    return x*y*z


# Get input
input = open('2015/Day02/input.txt').read().splitlines()
input_list = []
for row in input:
    row = row.split('x')
    row = list(map(int, row))
    input_list.append(row)

# Part 1
total_sqfr = 0
for dimensions in input_list:
    total_sqfr += get_outer_area(*dimensions) + get_slack(*dimensions)
print('Total square feet of wrapping paper needed: ' + str(total_sqfr))

# Part 2
total_ribbon_len = 0
for dimensions in input_list:
    total_ribbon_len += get_ribbon_length(*dimensions) + get_bow_length(*dimensions)
print('Total feet of ribbon needed: ' + str(total_ribbon_len))
