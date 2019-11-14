from operator import itemgetter
import math

def read_input():
    f = open('Day6/input.txt', 'r')
    coords = list()
    coords_d = dict()
    for line in f:
        x = line.split(',')[0]
        y = line.split()[1]
        y = y.replace('\n','')
        coords.append((int(x),int(y)))
        coords_d[(int(x),int(y))] = 0
    f.close()
    return coords, coords_d

def calc_closest_coord(x, y, coords):
    distances = list()
    for tup in coords:
        #Calculate manhattan distance
        d = abs(x-tup[0]) + abs(y-tup[1])
        distances.append(d)
    m = min(distances)
    min_pos = [i for i, j in enumerate(distances) if j==m]
    if(len(min_pos)==1):
        return coords[min_pos[0]]
    else:
        return (-1, -1);

def calc_total_distance(x,y,coords):
    tot_distance = 0
    for tup in coords:
        d = abs(x-tup[0]) + abs(y-tup[1])
        tot_distance += d
    return tot_distance
# 1st star
coords, coords_d = read_input()
maxX = max(coords, key=itemgetter(0))[0]
minX = min(coords, key=itemgetter(0))[0]
maxY = max(coords, key=itemgetter(1))[1]
minY = min(coords, key=itemgetter(1))[1]
print('xrange: ' + str(minX) + '-' +  str(maxX))
print('yrange: ' + str(minY) + '-' +  str(maxY))
print('Grid area: '+ str((maxX-minX)*(maxY-minY)))
coords_d[(-1,-1)] = 0

for x in range(minX, maxX+1):
    for y in range(minY, maxY+1):
        coord = calc_closest_coord(x,y,coords)
        if(x == minX or x == maxX or y == minY or y == maxY):
            coords_d[coord] = 0
        else:
            coords_d[coord] += 1

max_area = max(coords_d.items(), key=itemgetter(1))
print('Coord ' + str(max_area[0]) + ' gives a maximum area of: ' + str(max_area[1]))

#2nd star
coords, coords_d = read_input()
maxX = max(coords, key=itemgetter(0))[0]
minX = min(coords, key=itemgetter(0))[0]
maxY = max(coords, key=itemgetter(1))[1]
minY = min(coords, key=itemgetter(1))[1]
coords_d[(-1,-1)] = 0

region_size = 0
for x in range(minX, maxX+1):
    for y in range(minY, maxY+1):
        distance = calc_total_distance(x,y,coords)
        if(distance < 10000):
            region_size += 1

print('Region size: ' + str(region_size))
