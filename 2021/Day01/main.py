# Obtain input
depths = [int(line.strip()) for line in open('2021/Day01/input.txt', 'r').readlines()]

# Part 1
count = 0
for i in range(1, len(depths)):
    if (depths[i-1] - depths[i] < 0):
        count += 1
print(f"Part 1: {count} measurements are larger than the previous measurement.")

# Part 2
count = 0
for i in range(1, len(depths)-2):
    if( sum(depths[i-1:i+2]) < sum(depths[i:i+3]) ):
        count += 1
print(f"Part 2: {count} sums are larger than the previous sum.")