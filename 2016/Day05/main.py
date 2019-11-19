import hashlib

def check_hash_value(input, index):
    input = input + str(index)                  # Create string to hash
    m = hashlib.md5()                           # Create the MD5 hash object
    m.update(input.encode('utf-8'))
    hash = m.hexdigest()
    return hash[0:5]=='00000', hash             # Returns True if the hash starts
                                                # with 5 zeroes, otherwise False

puzzle_input = 'abbhdwsy'

# First star
index = 0
password = ''

for _ in range(0,8):
    hash_found = False
    while(not hash_found):
        hash_found, hash = check_hash_value(puzzle_input, index)
        if(hash_found):
            print('Hashing {} gives the hash value {}'.format(puzzle_input+str(index), hash))
            password += hash[5]
        index += 1;
print('[part1] The password is {}\n'.format(password))

# Second star
index = 0
password = ['','','','','','','','']

while ('' in password):
    hash_found = False
    while(not hash_found):
        hash_found, hash = check_hash_value(puzzle_input, index)
        if(hash_found):
            print('Hashing {} gives the hash value {}'.format(puzzle_input+str(index), hash))
            if(hash[5].isnumeric() and int(hash[5]) < 8 and password[int(hash[5])] is ''):
                password[int(hash[5])] += hash[6]
                print('The password is currently {}'.format(password))
        index += 1;
print('[part2] The password is {}'.format(''.join(password)))
