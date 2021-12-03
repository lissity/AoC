import collections

# Obtain input
input = [line.strip() for line in open('2021/Day03/input.txt', 'r').readlines()]

# Part 1
gamma, epsilon = '', ''
for pos in range(0, len(input[0])):
    count = collections.Counter([n[pos] for n in input])
    gamma += max(count, key = count.get)
    epsilon += min(count, key = count.get)
print(f'Part 1: The power consumption is {int(gamma,2) * int(epsilon, 2)}')

# Part 2
O2_rating = input.copy()
for pos in range(0, len(input[0])):
    count = collections.Counter([n[pos] for n in O2_rating])
    if (count['1'] == count['0']):    # 1 and 0 is equally common -> keep values with a 1 the current position
        O2_rating = [item for item in O2_rating if item[pos] == '1']
    else:                             # Keep values with the most common value in the current position
        most_common = max(count, key = count.get)
        O2_rating = [item for item in O2_rating if item[pos] == most_common]
    if (len(O2_rating) == 1):
        O2_rating = int(O2_rating[0], 2)
        break

CO2_rating = input.copy()
for pos in range(0, len(input[0])):
    count = collections.Counter([n[pos] for n in CO2_rating])
    if (count['1'] == count['0']):      # 1 and 0 is equally common -> keep values with a 0 in the current position
        CO2_rating = [item for item in CO2_rating if item[pos] == '0']
    else:                               # Keep values with the least common value in the current position
        least_common = min(count, key = count.get)
        CO2_rating = [item for item in CO2_rating if item[pos] == least_common]
    if (len(CO2_rating) == 1):
        CO2_rating = int(CO2_rating[0], 2)
        break

print(f'Part 2: The life support rating is {O2_rating * CO2_rating}.') 