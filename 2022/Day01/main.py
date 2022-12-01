# Obtain input
calories = []
current_list = []

for line in open('2022/Day01/input.txt', 'r').readlines():
    line = line.strip()
    if line is '':                       # New elf inventory, reset current list
        calories.append(current_list)
        current_list = []
    else:
        current_list.append(int(line))

# Part 1
calories_sums = [sum(cal) for cal in calories]
print(f"Part 1: The elf carrying the most calories is carrying " + 
       f"{max(calories_sums)} calories.")

# Part 2
calories_sums.sort()
calories_sums.reverse()

print(f"Part 2: The top 3 elfs are carrying {sum(calories_sums[0:3])} in total.")
