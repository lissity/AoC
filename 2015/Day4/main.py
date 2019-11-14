import hashlib
key = 'bgvyzdsv'

value = 0

# Part1
while(True):
    hashthis = key + str(value)
    hash = hashlib.md5(hashthis.encode('utf-8')).hexdigest()
    #print(hashthis +' : ' +hash)
    if(hash[:5] == '00000'):
        print(str(key) + str(value) + 'hashes to ' + hash)
        print('Answer: ' + str(value))
        break
    value += 1

# Part2
while(True):
    hashthis = key + str(value)
    hash = hashlib.md5(hashthis.encode('utf-8')).hexdigest()
    #print(hashthis +' : ' +hash)
    if(hash[:6] == '000000'):
        print(str(key) + str(value) + 'hashes to ' + hash)
        print('Answer: ' + str(value))
        break
    value += 1
