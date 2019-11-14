
# First star
file = open("Day2/input.txt", 'r')
two_letters = 0
three_letters = 0

for line in file:
    found_two = False
    found_three = False
    for char in line:
        char_count = line.count(char)
        if (char_count == 2 and found_two == False):
            two_letters += 1
            found_two = True
        if (char_count == 3 and found_three == False):
            three_letters += 1
            found_three = True
file.close()
print('Checksum: ' + str(two_letters) + " * " + str(three_letters) + " = " + \
      str(two_letters*three_letters))

# Second star
with open('Day2/input.txt') as f:
    lines = f.read().splitlines()

for x in lines:
    no_diff = 0
    for y in lines:
        if len([i for i in range(len(x)) if x[i] != y[i]]) == 1:
            print('whoa')
            print(x + " " + y)
