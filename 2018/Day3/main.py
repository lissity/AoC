
#Star 1
with open('Day3/input.txt') as f:
    lines = f.read().splitlines()

fabric = dict()

for x in lines:
    id = x.split()[0]
    coordStart = x.split()[2][:-1].split(',')
    dimensions = x.split()[3].split('x')
    coordStart[0] = int(coordStart[0])
    coordStart[1] = int(coordStart[1])
    dimensions[0] = int(dimensions[0])
    dimensions[1] = int(dimensions[1])

    for x in range(coordStart[0], coordStart[0]+dimensions[0]):
        for y in range(coordStart[1], coordStart[1]+dimensions[1]):
            if (fabric.get((x,y)) == None):
                fabric[(x,y)] = 1
            else:
                fabric[(x,y)] += 1

overlap_sum = 0
for key in fabric:
    if(fabric[key] > 1):
        overlap_sum += 1

print('Number of overlapping squares: ' + str(overlap_sum))

#Star 2
ids = dict()
fabric = dict()
for x in lines:
    id = x.split()[0]
    coordStart = x.split()[2][:-1].split(',')
    dimensions = x.split()[3].split('x')
    coordStart[0] = int(coordStart[0])
    coordStart[1] = int(coordStart[1])
    dimensions[0] = int(dimensions[0])
    dimensions[1] = int(dimensions[1])
    ids[id] = True

    for x in range(coordStart[0], coordStart[0]+dimensions[0]):
        for y in range(coordStart[1], coordStart[1]+dimensions[1]):
            if (fabric.get((x,y)) == None):
                fabric[(x,y)] = id
            else:
                ids[fabric[(x,y)]] = False
                ids[id] = False
                #fabric[(x,y)] += 1

for key in ids:
    if(ids[key] == True):
        print(str(ids[key]) + str(key))
        break
