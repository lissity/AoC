from string import ascii_lowercase

def reactWithNeighbor(letterIndex, polymer):
    current_letter = polymer[letterIndex]
    if(current_letter.islower()):
        current_letter = current_letter.upper()
        if(letterIndex-1 >= 0):             #valid left neighbor
            if(current_letter == polymer[letterIndex-1]):
                #React
                polymer = polymer[:letterIndex-1] + polymer[letterIndex+1:]
                return True, polymer
            else:
                return False, polymer
    elif(current_letter.isupper()):
        current_letter = current_letter.lower()
        if(letterIndex-1 >= 0):             #valid left neighbor
            if(current_letter == polymer[letterIndex-1]):
                #React
                polymer = polymer[:letterIndex-1] + polymer[letterIndex+1:]
                return True, polymer
            else:
                return False, polymer
    return False, polymer;

# First star
f = open('Day5/input.txt', 'r')
polymer = f.readline()
polymer = polymer[:-1]  #remove newline
f.close()
#polymer = 'dabAcCaCBAcCcaDA'

index = 1;
size = len(polymer)
while(index < size):
    #print(index)
    tup = reactWithNeighbor(index, polymer)
    if (tup[0] == True):
        size = size - 2
        polymer = tup[1]
        if(index > 2):
            index = index - 2
    else:
        index += 1;
print('Units remaining: ' + str(len(polymer)))

#Second star
f = open('Day5/input.txt', 'r')
polymer = f.readline()
polymer = polymer[:-1]  #remove newline
f.close()

for c in ascii_lowercase:
    print('Removing character: ' + c)
    temp_polymer = polymer.replace(c,'')
    temp_polymer = temp_polymer.replace(c.upper(),'')

    index = 1;
    size = len(temp_polymer)
    while(index < size):
        tup = reactWithNeighbor(index, temp_polymer)
        if (tup[0] == True):
            size = size - 2
            temp_polymer = tup[1]
            if(index > 2):
                index = index - 2
        else:
            index += 1;
    print('Units remaining: ' + str(len(temp_polymer)))
