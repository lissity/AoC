def getInMemoryLength(string):
    length = 0
    i = 1
     # Looping through the string skipping first and last double quote
    while i < len(string)-1:   
        next = string[i:i+2]
        if (next == r'\x'):                     # Hexadecimal escape sequence 
            i += 4
        elif (next == r'\\' or next == r'\"'):  # Escape sequence for \ and "
            i += 2
        else:                                   # Normal string character
            i += 1
        length +=1
    return length

def getEncodedLength(string):
    length = 2                  # Two enclosing double quotes needed
    for char in string:
        if (char == r'"' or char == '\\'):
            length += 2     # 2 characters needed to encode/escape " and \
        else:
            length +=1
    return length

strings = open('2015/Day8/input.txt').read().splitlines()

# --- Part 1 ---
code_representation_len = len(''.join(strings))
in_memory_len = sum(list(map(getInMemoryLength, strings)))

print('Part 1: Answer:', code_representation_len-in_memory_len)

# --- Part 2 ---
encoded_len = sum(list(map(getEncodedLength, strings)))

print('Part 2: Answer:', encoded_len-code_representation_len)