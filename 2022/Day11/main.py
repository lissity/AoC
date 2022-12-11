import math
import re

class Monkey:
    def __init__(self, info_list):
        self.id = int(info_list[0].split()[1][:-1])
        self.items = list(map(int, re.findall('[0-9]+',info_list[1])))
        self.operand1 = info_list[2].strip().split()[3:][0]
        self.operator = info_list[2].strip().split()[3:][1]
        self.operand2 = info_list[2].strip().split()[3:][2]
        self.div_test = int(info_list[3].strip().split()[3])
        self.true_id = int(info_list[4].strip().split()[5])
        self.false_id = int(info_list[5].strip().split()[5])
        self.inspected_items = 0
  
    def __str__(self):
        return f'Monkey {self.id} holding items {self.items}. Inspected {self.inspected_items} times.'

    def perform_operation(self, item):
        if self.operand1 == 'old':
            op1 = item
        else:
            op1 = int(self.operand1)
        if self.operand2 == 'old':
            op2 = item
        else:
            op2 = int(self.operand2)
        if self.operator == '*':
            return op1 * op2
        elif self.operator == '+':
            return op1 + op2

    def handle_item(self, worry_level_reducer=0):
        if len(self.items) == 0:
            return None, None
        self.inspected_items += 1
        item = self.items[0]
        del self.items[0]
        item = self.perform_operation(item)

        if worry_level_reducer == 0:        # Reducing worry levels in Part 1
            item = math.floor(item/3)
        else:                               # Reducing worry levels in Part 2
            reduce = math.floor(item / worry_level_reducer)
            item = item - reduce * worry_level_reducer
        
        if item % self.div_test == 0:
            return self.true_id, item
        else:
            return self.false_id, item

# Obtain input
puzzle_input =  [chunk.splitlines() for chunk in open('2022/Day11/input.txt').read().split('\n\n')]

# Part 1
monkeys1 = {}
i = 0
for info_chunk in puzzle_input:
    monkey = Monkey(info_chunk)
    monkeys1[i] = monkey
    i += 1

for round in range(20):
    for i in range(len(monkeys1)):
        ret = -1
        while ret is not None:
            ret, item = monkeys1[i].handle_item()
            if (ret is not None):
                monkeys1[ret].items.append(item)

num_items_inspected = []
for id, monkey in monkeys1.items():
    num_items_inspected.append(monkey.inspected_items)

num_items_inspected.sort(reverse=True)
print(f'Part 1: The level of monkey business after 20 rounds is ' +
      f'{num_items_inspected[0]* num_items_inspected[1]}.')

# Part 2
monkeys2 = {}
i = 0
for info_chunk in puzzle_input:
    monkey = Monkey(info_chunk)
    monkeys2[i] = monkey
    i += 1

# Creating a "reducer" number which will keep worry level managable.
reducer = 1
for id, monkey in monkeys2.items():
    reducer *= monkey.div_test

for round in range(10000):
    for i in range(len(monkeys2)):
        ret = -1
        while ret is not None:
            ret, item = monkeys2[i].handle_item(reducer)
            if (ret is not None):
                monkeys2[ret].items.append(item)

num_items_inspected = []
for id, monkey in monkeys2.items():
    num_items_inspected.append(monkey.inspected_items)

num_items_inspected.sort(reverse=True)
print(f'Part 2: The level of monkey business after 10000 rounds is ' +
      f'{num_items_inspected[0]* num_items_inspected[1]}.')
