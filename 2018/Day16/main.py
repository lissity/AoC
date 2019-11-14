import re
def read_input(path):
    input = open(path,'r').read().splitlines()
    input = [value for value in input if value != '']
    input_dict = dict()
    id = 0
    for i in range(0, len(input), 3):
        new_dict = dict()
        new_dict['Before'] = [int(s) for s in re.findall(r'\b\d+\b', input[i])]
        new_dict['Instruction'] = [int(s) for s in re.findall(r'\b\d+\b', input[i+1])]
        new_dict['After'] = [int(s) for s in re.findall(r'\b\d+\b', input[i+2])]
        input_dict[id] = new_dict
        id += 1
    return input_dict
def addr(A, B, C, reg):
    reg[C] = reg[A] + reg[B]
    return reg
def addi(A, B, C, reg):
    reg[C] = reg[A] + B
    return reg
def mulr(A,B,C,reg):
    reg[C] = reg[A] * reg[B]
    return reg
def muli(A,B,C,reg):
    reg[C] = reg[A] * B
    return reg
def banr(A,B,C,reg):
    reg[C] = reg[A] & reg[B]
    return reg
def bani(A,B,C,reg):
    reg[C] = reg[A] & B
    return reg
def borr(A,B,C,reg):
    reg[C] = reg[A] | reg[B]
    return reg
def bori(A,B,C,reg):
    reg[C] = reg[A] | B
    return reg
def setr(A,B,C,reg):
    reg[C] = reg[A]
    return reg
def seti(A,B,C,reg):
    reg[C] = A
    return reg
def gtir(A,B,C,reg):
    if (A > reg[B]):
        reg[C] = 1
    else:
        reg[C] = 0
    return reg
def gtri(A,B,C,reg):
    if(reg[A] > B):
        reg[C] = 1
    else:
        reg[C] = 0
    return reg
def gtrr(A,B,C,reg):
    if(reg[A] > reg[B]):
        reg[C] = 1
    else:
        reg[C] = 0
    return reg
def eqir(A,B,C,reg):
    if(A == reg[B]):
        reg[C] = 1
    else:
        reg[C] = 0
    return reg
def eqri(A,B,C,reg):
    if(reg[A] == B):
        reg[C] = 1
    else:
        reg[C] = 0
    return reg
def eqrr(A,B,C,reg):
    if(reg[A] == reg[B]):
        reg[C] = 1
    else:
        reg[C] = 0
    return reg

input_dict = read_input('2018/Day16/input1.txt')
# Part 1
total_samples = 0
for key in input_dict:
    reg_before = input_dict[key]['Before']
    opcode = input_dict[key]['Instruction'][0]
    A = input_dict[key]['Instruction'][1]
    B = input_dict[key]['Instruction'][2]
    C = input_dict[key]['Instruction'][3]
    reg_after =input_dict[key]['After']

    list1 = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]
    matches = 0
    for func in list1:
        reg_b = reg_before.copy()
        a = A
        b = B
        c = C
        reg_a = reg_after.copy()
        ret_reg = func(a,b,c,reg_b)
        if(ret_reg == reg_a):
            matches +=1
    if(matches >= 3):
        total_samples +=1
print('Samples that behave like 3 or more opcodes: ', total_samples)
def dict_is_ambigious(dict):
    isit = False
    for key in dict:
        if(len(dict[key])>1):
            isit = True
            break
    return isit
def read_input_2(path):
    input = open(path, 'r').read().splitlines()
    input_list = list()
    for line in input:
        input_list.append(line.split())
    return input_list
def execute_instruction(instruction, reg, opcode_dict, op_list):
    opcode = instruction[0]
    A = instruction[1]
    B = instruction[2]
    C = instruction[3]
    for key in opcode_dict:
        if(opcode_dict[key][0] == opcode):
            #print('found match')
            opc = key
    for item in op_list:
        if opc == item[0]:
            reg = item[1](A,B,C,reg)
    return reg

# Part 2
opcode_dict = dict()
op_list = [('addr', addr), ('addi',addi), ('mulr', mulr), ('muli', muli),\
        ('banr', banr), ('bani', bani), ('borr', borr), ('bori', bori),\
        ('setr', setr), ('seti', seti), ('gtir', gtir), ('gtri', gtri),\
        ('gtrr', gtrr), ('eqir', eqir), ('eqri', eqri), ('eqrr', eqrr)]
for item in op_list:
    opcode_dict[item[0]] = list()
for key in input_dict:
    reg_before = input_dict[key]['Before']
    opcode = input_dict[key]['Instruction'][0]
    A = input_dict[key]['Instruction'][1]
    B = input_dict[key]['Instruction'][2]
    C = input_dict[key]['Instruction'][3]
    reg_after =input_dict[key]['After']

    for func in op_list:
        reg_b = reg_before.copy()
        a = A
        b = B
        c = C
        reg_a = reg_after.copy()
        ret_reg = func[1](a,b,c,reg_b)
        if(ret_reg == reg_a):
            opcode_dict[func[0]].append(opcode)
# Remove duplicates
for key in opcode_dict:
    opcode_dict[key] = list(set(opcode_dict[key]))
# Find
while(dict_is_ambigious(opcode_dict)):
    #find list with len = 1
    for key in opcode_dict:
        if(len(opcode_dict[key]) == 1):
            remove_this = opcode_dict[key][0]
            dont_remove_here = key
            #remove set.value from other sets
            for key in opcode_dict:
                if(key != dont_remove_here and remove_this in opcode_dict[key]):
                    opcode_dict[key].remove(remove_this)

instructions = read_input_2('2018/Day16/input2.txt')
register = [0,0,0,0]
for ins in instructions:
    ins = [int(ins[0]),int(ins[1]),int(ins[2]),int(ins[3])]
    register = execute_instruction(ins, register, opcode_dict, op_list)
print('Register at end: ', register)
