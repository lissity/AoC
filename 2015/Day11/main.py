def increment_password(pwd):
    for i in range(len(pwd)-1, 0-1, -1):
        pwd[i] = increment_char(pwd[i])

        # If the incremented letter is i, o, or l we discard the password
        # by incrementing again
        if (pwd[i] in ['i', 'o', 'l']):
            pwd[i] = increment_char(pwd[i])

        if (pwd[i] != 'a'):
            # letter did not wrap around -> increment done
            break
    return pwd

def increment_char(c):
    if (c == 'z'):
        return 'a'
    else:
        return chr(ord(c)+1)

def contains_2_pairs(word):
    pairs_found = 0
    i = 0
    while(i < len(word)-1):
        if (word[i] == word[i+1]):
            pairs_found += 1
            i += 1              # Increment i to avoid overlapping pairs
        i+=1
    return (pairs_found >= 2)

def contains_sequence_of_3(word):
    for i in range(0, len(word)-2):
        if(ord(word[i]) == ord(word[i+1])-1 == ord(word[i+2])-2):
            return True
    return False

puzzle_input = "hepxcrrq"

# --- Part 1 ---
current_pwd = list(puzzle_input)
while(True):
    current_pwd = increment_password(current_pwd)
    if(contains_2_pairs(current_pwd) and contains_sequence_of_3(current_pwd)):
        break

print(f'Part 1: The next password should be {"".join(current_pwd)}')

# --- Part 2 ---
while(True):
    current_pwd = increment_password(current_pwd)
    if(contains_2_pairs(current_pwd) and contains_sequence_of_3(current_pwd)):
        break

print(f'Part 2: The next-next password should be {"".join(current_pwd)}')
