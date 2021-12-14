from collections import Counter

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.previous=None

def insert_node(node, prev_node, next_node):
    node.previous = prev_node
    node.next = next_node
    prev_node.next = node
    next_node.previous = node

def get_polymer_str(start_node):
    result = []
    node = start_node
    while node != None:
        result.append(node.data)
        node = node.next
    return ''.join(result)

def add_to_dict(dictionary, key, count):
    if key in dictionary:
        dictionary[key] += count
    else:
        dictionary[key] = count

# Obtain puzzle input
rules = {}
with open('2021/Day14/input.txt','r') as file:
    start_polymer = file.readline().strip()
    file.readline()
    for line in file.readlines():
        tmp = line.strip().split(' -> ')
        rules[tmp[0]] = tmp[1]

# Part 1
# Create nodes
node_list = []
for char in start_polymer:
    node_list.append(Node(char))

# Link nodes to eachother (linked list)
for i in range(len(node_list)):
    if (i > 0):
        node_list[i].previous = node_list[i-1]
    if (i < len(node_list)-1):
        node_list[i].next = node_list[i+1]

first_node = node_list[0]           # Keeping track of the first node

for i in range(10):                 # Simulate 10 steps
    node = first_node.next
    while (node != None):
        pair = node.previous.data + node.data
        if pair in rules:
            new_node = Node(rules[pair])
            insert_node(new_node, node.previous, node)
        node = node.next

polymer = get_polymer_str(first_node)
frequency = dict(Counter(polymer))
most_common_letter_count = max(frequency.items(), key=lambda x: x[1])[1]
least_common_letter_count = min(frequency.items(), key=lambda x: x[1])[1]
result = most_common_letter_count - least_common_letter_count
print(f'Part 1: The result is {result}.')

# Part 2
pairs = {}
for i in range(1, len(start_polymer)):
    pair = start_polymer[i-1]+start_polymer[i]
    add_to_dict(pairs, pair, 1)

for i in range(40):                 # Simulate 40 steps
    new_pairs = {}
    for pair in pairs:
        count = pairs[pair]         # The number of new pairs
        new_pair1 = pair[0] + rules[pair]
        new_pair2 = rules[pair]+ pair[1]
        add_to_dict(new_pairs, new_pair1, count)
        add_to_dict(new_pairs, new_pair2, count)
    pairs = new_pairs

frequency = {}
for key, value in pairs.items():
    add_to_dict(frequency, key[0], value)    # Counting the frequency of letters by looking at the first letter of each pair
add_to_dict(frequency, start_polymer[-1], 1) # Adding the last letter which is not included in the method above

most_common_letter_count = max(frequency.items(), key=lambda x: x[1])[1]
least_common_letter_count = min(frequency.items(), key=lambda x: x[1])[1]
result = most_common_letter_count - least_common_letter_count
print(f'Part 2: The result is {result}.')
