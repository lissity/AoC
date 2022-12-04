# Obtain input
puzzle_input = [line.strip().split(',') for line in open('2022/Day04/input.txt').readlines()]
puzzle_input = [(line[0].split('-'), line[1].split('-')) for line in puzzle_input]

# Part 1 & 2
fully_contains_count = 0
part_contains_count = 0

for pairs in puzzle_input:
    range1min = int(pairs[0][0])
    range1max = int(pairs[0][1])
    range2min = int(pairs[1][0])
    range2max = int(pairs[1][1])

    # Check if range1 contains range2
    if (range2min >= range1min and range2max <= range1max):
        fully_contains_count +=1
    # Check if range2 contains range1
    elif (range1min >= range2min and range1max <= range2max):
        fully_contains_count +=1
    # Check if ranges are partially overlapping
    elif (range1max >= range2min and range1max <= range2max):
        part_contains_count += 1
    elif (range1min >= range2min and range1min <= range2max):
        part_contains_count += 1

print(f'Part 1: In {fully_contains_count} assignment pairs does one range fully'
      f' contain the other.')
print(f'Part 2: In {fully_contains_count + part_contains_count} assignment '
      f'pairs does the ranges overlap.')
