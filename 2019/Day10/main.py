import math
import operator
import collections

def calc_angle(point1, point2):
    x = point2[0] - point1[0]
    y = (point2[1] - point1[1]) * -1        # Adjust y since coordinate system is flipped (y increases downwards)
    return (360 - (math.degrees(math.atan2(y,x))-90)) % 360 # Adjust angle to work better with part2

def detect_asteroids(location, asteroid_locations):
    angles = {}
    for loc in asteroid_locations:
        if(location != loc):
            angle = round(calc_angle(location, loc), 5)
            if angle not in angles:
                angles[angle] = [loc]
            else:
                angles[angle].append(loc)
    return angles

def distance_to_laser(point):
    return math.hypot(point[0]-best_location[0], point[1]-best_location[1])

def asteroids_exists(detections):
    asteroids_found = False
    for key, value in detections.items():
        if(value != []):
            return True

# Obtain input
input = [list(line.strip()) for line in open('2019/Day10/input.txt', 'r').readlines()]
asteroid_locations = []
for row in range(0, len(input)):
    for col in range(0, len(input[row])):
        if(input[row][col] == '#'):
            asteroid_locations.append((col, row))

# Part 1
asteroids_detected = {}
for asteroid_location in asteroid_locations:
    detections = detect_asteroids(asteroid_location, asteroid_locations)
    asteroids_detected[asteroid_location] = len(detections)

best_location, no_detected_asteroids = max(asteroids_detected.items(), key=operator.itemgetter(1))
print('[part1] The maximum number of asteroids detected is {} (at location {})'\
      .format(no_detected_asteroids, best_location))

# Part 2
detections = detect_asteroids(best_location, asteroid_locations)

# Sort the asteroid coordinates on distance from giant laser
for key, value in detections.items():
    detections[key] = sorted(value, key=distance_to_laser)

# Sort the dictionary on angles
ordered_detections = collections.OrderedDict(sorted(detections.items()))

# Find the order which the laser will hit the asteroids
vaporization_order = []
while(asteroids_exists(ordered_detections)):
    for key, value in ordered_detections.items():
        if(value != []):
            vaporization_order.append(ordered_detections[key].pop(0))

answer = vaporization_order[199]
print('[part2] The 200th asteroid to be vaporized is at location {}. The puzzle'\
' answer is 100*{}+{} = {}'.format(answer, answer[0], answer[1], 100*answer[0]+answer[1]))
