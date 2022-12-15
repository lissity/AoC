import math
import re

class Sensor:
    def __init__(self, sx, sy, bx, by):
        self.pos = (sx,sy)
        self.beacon_pos = (bx,by)
        self.reach = manhattan(self.pos, self.beacon_pos)

def manhattan(a, b):
    return sum([abs(a[0] - b[0]), abs(a[1] - b[1])])

# Obtain input
puzzle_input = [list(map(int,re.findall('\-?\d+',line))) 
                for line in open('2022/Day15/input.txt').readlines()]
sensors = []
for row in puzzle_input:
    sensors.append(Sensor(row[0], row[1], row[2], row[3]))

# Part 1
y = 2000000
no_beacon_pos = {}

for sensor in sensors:
    x = sensor.pos[0]
    row = abs(sensor.pos[1] - y)    # The y-distance between sensor and y-row

    # Calculating the number of x-coords which will be covered by this sensor
    # on the y-row
    sensor_y_length = (sensor.reach * 2 + 1)- (2 * row)
    if sensor_y_length > 0:     # Checking if this sensor reaches the y-row
        x1 = x - math.floor(sensor_y_length / 2)
        x2 = x + math.floor(sensor_y_length / 2)
        for i in range(x1,x2+1):
            cur_pos = (i,y)
            if cur_pos != sensor.beacon_pos:
                no_beacon_pos[cur_pos] = True

print(f'Part 1: On row {y} the number of postions that can\'t contain a ' + 
      f'beacon is {len(no_beacon_pos)}.')

# Part 2
def merge(intervals):
    if len(intervals) == 0 or len(intervals) == 1:
        return intervals
    intervals.sort(key=lambda x:x[0])
    result = [intervals[0]]
    for interval in intervals[1:]:
        if interval[0] <= result[-1][1]:
            result[-1][1] = max(result[-1][1], interval[1])
        else:
            result.append(interval)
    return result

miny = 0
maxy = 4000000

for y_row in range(maxy):
    y = y_row
    intervals = []
    for sensor in sensors:
        x = sensor.pos[0]
        row = abs(sensor.pos[1] - y)
        sensor_y_length = (sensor.reach * 2 + 1)- (2 * row)
        if sensor_y_length > 0:
            x1 = max(miny, x - math.floor(sensor_y_length / 2))
            x2 = min(x + math.floor(sensor_y_length / 2), maxy)
            intervals.append([x1,x2])
    intervals = merge(intervals)
    if len(intervals) != 1:     # Check if interval could not be merged into 1
        beacon_y = y_row
        beacon_x = intervals[0][1] + 1
        break
tuning_freq = beacon_x * 4000000 + beacon_y
print(f'Part 2: The tuning frequency is {tuning_freq}.')
