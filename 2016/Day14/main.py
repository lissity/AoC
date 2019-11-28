import hashlib
import re

def key_stretching(data):
    for i in range(0, 2016):
        data = data.encode('utf-8')
        data = hashlib.md5(data).hexdigest()
    return data

def generate_keys(salt, use_key_stretching=False):
    key_indexes = []
    index = 0
    trip_patt = re.compile(r'([0-9]|[a-f])\1{2}')      # Regex to find triples of any character
    triples = []
    pentas = {'aaaaa': [], 'bbbbb': [], 'ccccc': [], 'ddddd': [], 'eeeee': [], 'fffff': [],
              '00000': [], '11111': [], '22222': [], '33333': [], '44444': [], '55555': [],
              '66666': [], '77777': [], '88888': [], '99999': []}

    while(len(key_indexes)<64):
        data_steam = (salt + str(index)).encode('utf-8')
        hash_value = hashlib.md5(data_steam).hexdigest()

        if(use_key_stretching):
            hash_value = key_stretching(hash_value)

        # Search for pentas for past triples
        for key, value in pentas.items():
            pentas[key] = [val for val in value if val[1] != 0] # remove items where steps are 0
            if(value and hash_value.find(key) != -1): # if found, add indexes in list to key_indexes and empty list.
                for val in value:
                    key_indexes.append(val[0])  # Add indexes to key_indexes
                pentas[key] = []                # Empty list
            else:
                for val in value:
                    val[1] -= 1                 # Decrease number of hashes left

        # Search for triples in current hash
        triple = re.search(trip_patt, hash_value)
        if(triple is not None):                 # Save info about found triple
            penta = triple.group()[0]*5
            pentas[penta].append([index, 1000])

        index += 1

    key_indexes.sort()
    return key_indexes

salt = 'cuanljph'

# First star
key_indexes = generate_keys(salt)
print('[part1] The index that produces the 64th one-time pad key is {}'. format(key_indexes[63]))

# Second star
key_indexes = generate_keys(salt, use_key_stretching=True)
print('[part2] The index that produces the 64th one-time pad key ',
      '(using key-stretching) is {}'. format(key_indexes[63]))
