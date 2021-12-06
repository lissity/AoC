# Obtain input
input = list(map(int, open('2021/Day06/input.txt','r').readline().strip().split(',')))

# Part 1
fishes = input.copy()
for i in range(80):
    for i in range(0, len(fishes)):
        if(fishes[i] == 0):
            fishes[i] = 6
            fishes.append(8)
        else:
            fishes[i] -= 1
print(f'Part 1: There are {len(fishes)} laternfish after 80 days.')

# Part 2
fish_record = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
for fish in input:
    fish_record[fish] += 1

for i in range(256):
    new_spawns = fish_record[0]    # Amount of new fishes(8) and reset fishes(6)
    fish_record[0] = 0
    for i in range(1,9):           # Go through 1-8 and move fishes down one level
        fish_record[i-1] = fish_record[i]
    fish_record[8] = new_spawns    # Adding the new fishes to 8
    fish_record[6] += new_spawns   # Adding reset fishes to 6

print(f'Part 2: There are {sum(fish_record.values())} laternfish after 256 days.')