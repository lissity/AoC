def parse_input(input):
    locations = dict()
    for row in input:
        row = row.split()
        loc1 = row[0]
        loc2 = row[2]
        distance = int(row[4])
        if loc1 not in locations:
            locations[loc1] = []
        if loc2 not in locations:
            locations[loc2] = []
        locations[loc1].append((loc2, distance))
        locations[loc2].append((loc1, distance))
    return locations

def distance_to_new_city(distance_list, visited_cities, reverse_sort):
    """ Return the (city, distance)-tuple to a new city.
        If reverse_sort is True the longest distance is returned.
        If reverse_sort is False the shortest distance is returned. """
    distance_list.sort(key=lambda tup: tup[1], reverse=reverse_sort)
    for item in distance_list:
        if(item[0] not in visited_cities):
            return item

# Get input
input = open("2015/Day09/input.txt").read().splitlines()
locations = parse_input(input)

# --- Part 1 ---
distances = []

# Each location in 'locations' are used as a start-location
for loc in locations:
    current_loc = loc
    visited = [current_loc]     # Add current location to visited-list
    current_distance = 0

    # Travel 'len(locations)-1' times to visit all locations once
    for i in range(len(locations)-1):   
        tup = distance_to_new_city(locations[current_loc], visited, False)
        current_loc = tup[0]        # Update current location
        current_distance += tup[1]  # Update distance travelled
        visited.append(tup[0])      # Add location to visited-list

    # Save distance travelled for this start location    
    distances.append(current_distance)

print('Part 1: The distance of the shortest route is', min(distances))

# --- Part 2 ---
distances = []

for loc in locations:
    current_loc = loc
    visited = [current_loc]
    current_distance = 0

    for i in range(len(locations)-1):
        tup = distance_to_new_city(locations[current_loc], visited, True)
        current_loc = tup[0]
        current_distance += tup[1]
        visited.append(tup[0])
    distances.append(current_distance)

print('Part 2: The distance of the longest route is', max(distances))
