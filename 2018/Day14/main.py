from llist import dllist, dllistnode

def create_new_recipies(rec1, rec2, list):
    v1 = rec1.value
    v2 = rec2.value
    tot = v1+v2
    tot = str(tot)
    c = 0
    for char in tot:
        list.append(int(char))
        c += 1
    return str(tot), c
def move_steps_in_list(start_node, steps, list):
    current = start_node
    for i in range(steps):
        if(current.next == None):
            current = list.first
        else:
            current = current.next
    return current

def calc_score(list):
    last_node = list.last
    score = ''
    for i in range(10):
        score = str(last_node.value) + score
        last_node = last_node.prev
    return score

def constuct_seq(start_node, size):
    seq = ''
    current = start_node
    for i in range(size):
        seq = seq + str(current.value)
        current = current.next
    return seq
# Part 1
no_recipes = 824501

lst = dllist()
elf1 = lst.append(3)
elf2 = lst.append(7)

while(lst.size < no_recipes+10):
    create_new_recipies(elf1, elf2, lst)
    elf1 = move_steps_in_list(elf1, elf1.value+1, lst)
    elf2 = move_steps_in_list(elf2, elf2.value+1, lst)

while(lst.size > no_recipes+10):
    lst.pop()
#print(lst)     #ohoh, don't print a linked list of 800k+ items :^)
print('Score:', calc_score(lst))

# Part 2    #tar 100+ sekunder att köra
score_seq = '824501'
seq_size = len(score_seq)

lst = dllist()
elf1 = lst.append(3)
seq = lst.first
elf2 = lst.append(7)
seq_not_found = True
recipe_count = 0
count = 0

while(seq_not_found):
    # if(count%100000 == 0):
    #     print(count)
    create_new_recipies(elf1, elf2, lst)
    if(lst.size >= seq_size):
        seq_str = constuct_seq(seq, seq_size)
        seq = seq.next
        #print(seq_str, score_seq)
        if(seq_str == score_seq):
            print('Found it!', recipe_count)
            seq_not_found = False
        recipe_count +=1
    elf1 = move_steps_in_list(elf1, elf1.value+1, lst)
    elf2 = move_steps_in_list(elf2, elf2.value+1, lst)
    count +=1
