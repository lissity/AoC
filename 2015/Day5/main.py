def containsThreeVowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowelCount = 0
    for char in string:
        if char in vowels:
            vowelCount += 1
        if vowelCount >= 3:
            return True
    return False


def containsDoubleLetter(string):
    for i in range(0, len(string)-1):
        if(string[i] == string[i+1]):
            return True
    return False


def containsForbiddenSubStrings(string):
    forbidden = ['ab', 'cd', 'pq', 'xy']
    for i in range(0, len(string)-1):
        if string[i:i+2] in forbidden:
            return True
    return False


def containsRepeatedLetter(string):
    for i in range(0, len(string)-2):
        if (string[i] == string[i+2]):
            return True
    return False


def containsPair(string):
    for i in range(0, len(string)-1):
        pair = string[i:i+2]

        # Search for pairs in beginning of string
        for j in range(0, i-1):
            if (pair == string[j:j+2]):
                return True

        # Search for pairs in end of string
        for k in range(i+2, len(string)-1):
            if (pair == string[k:k+2]):
                return True
    return False


def isStringNice(string):
    return (containsThreeVowels(string) and
            containsDoubleLetter(string) and
            not containsForbiddenSubStrings(string))


def isStringNiceNew(string):
    return (containsPair(string) and containsRepeatedLetter(string))


strings = open('2015/Day5/input.txt').read().splitlines()

# Part 1
nice_counter = sum(list(map(isStringNice, strings)))
print('Part 1:', nice_counter, 'strings are nice')

# Part 2
nice_counter = sum(list(map(isStringNiceNew, strings)))
print('Part 2:', nice_counter, 'strings are nice')
