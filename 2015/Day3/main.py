def move(currentCoord, c):
    if(c == '<'):
        newCoord = (currentCoord[0]-1, currentCoord[1])
    elif(c == '^'):
        newCoord = (currentCoord[0], currentCoord[1]+1)
    elif(c == '>'):
        newCoord = (currentCoord[0]+1, currentCoord[1])
    elif(c == 'v'):
        newCoord = (currentCoord[0], currentCoord[1]-1)
    return newCoord

# Part 1
input = open('2015/Day3/input.txt','r').readline()[:-1]
currentCoord = (0, 0)
path = list()
path.append(currentCoord[:])

for c in input:
    currentCoord = move(currentCoord, c)
    path.append(currentCoord)

print('Houses with at least one present: ' + str(len(set(path))))

# Part 2
santaPos = (0, 0)
roboPos = (0, 0)
visitedCoords = list()
santasTurn = True
for c in input:
    if(santasTurn):
        santaPos = move(santaPos, c)
        visitedCoords.append(santaPos)
        santasTurn = False
    elif(not santasTurn):
        roboPos = move(roboPos, c)
        visitedCoords.append(roboPos)
        santasTurn = True

print('Houses with at least one present (Year 2): ' + str(len(set(visitedCoords))))
