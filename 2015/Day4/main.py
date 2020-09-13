import hashlib

input = 'bgvyzdsv'

# Part 1
counter = 0
while True:
    text = input + str(counter)
    hash = hashlib.md5(str.encode(text)).hexdigest()
    if (hash[0:5] == '00000'):
        print('Part 1: Hashing', text, 'produces the hash',
              hash, '-> Answer:', counter)
        break
    counter += 1

# Part 2
while True:
    text = input + str(counter)
    hash = hashlib.md5(str.encode(text)).hexdigest()
    if (hash[0:6] == '000000'):
        print('Part 2: Hashing', text, 'produces the hash',
              hash, '-> Answer:', counter)
        break
    counter += 1
