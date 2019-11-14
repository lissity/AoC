
class Node:
    def __init__(self, no_children, no_metadata):
        self.no_children = no_children
        self.no_metadata = no_metadata
        self.children = list()
        self.metadata = list()
    def print_node(self):
        message = 'NumberOfChildren: ' + str(self.no_children) + '\n'
        message += 'NumberOfMetadata: ' + str(self.no_metadata) + '\n'
        message += 'Children: ' + str(self.children)
        print(message)
        return

def create_Node(input, index):
    quantity_children = int(input[index])
    index += 1
    quantity_metadata = int(input[index])
    index += 1
    node = Node(quantity_children, quantity_metadata)
    for i in range(0, quantity_children):
        child_node, index = create_Node(input, index)
        node.children.append(child_node)
    for i in range(0, quantity_metadata):
        node.metadata.append(int(input[index]))
        index += 1
    return node, index

def add_metadata(node):
    sum = 0
    for child in node.children:
        sum += add_metadata(child)
    for meta in node.metadata:
        sum += meta
    return sum

def calc_value_of_node(node):
    #leaf node
    if(node.no_children == 0):
        sum = 0
        for d in node.metadata:
            sum += d
        return sum
    value = 0
    for d in node.metadata:
        if(d <= node.no_children and d > 0):
            index = d-1
            value += calc_value_of_node(node.children[index])
    return value

input = open('2018/Day8/input.txt', 'r').readline()[:-1].split()
root, i = create_Node(input, 0)
print('Metadata Sum: ' + str(add_metadata(root)))
print('Value of root: ' + str(calc_value_of_node(root)))
