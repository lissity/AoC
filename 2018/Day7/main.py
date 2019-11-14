from string import ascii_uppercase
def read_input():
    f = open('2018/Day7/input.txt', 'r')
    steps = list()
    step1 = list()
    step2 = list()
    for line in f:
        steps.append((line[5:6],line[36:37]))
        step1.append(line[5:6])
        step2.append(line[36:37])
    return steps, step1, step2

def decide_step(steps):
    step1 = list()
    step2 = list()
    for tup in steps:
        step1.append(tup[0])
        step2.append(tup[1])
    possible_steps = list()
    for step in set(step1):
        if(step2.count(step) == 0):
            possible_steps.append(step)
    return min(possible_steps)

def find_last_step(steps):
    step1 = list()
    step2 = list()
    for tup in steps:
        step1.append(tup[0])
        step2.append(tup[1])
    for step in set(step2):
        if(step1.count(step) == 0):
            return step

def remove_step(steps, s_char):
    remove_these = list()
    for tup in steps:
        if(tup[0]==s_char):
            remove_these.append(tup)
    for tup in remove_these:
        steps.remove(tup)
    return steps

# First star
steps = read_input()[0]
step_order = ''

last_step = find_last_step(steps)

while(len(steps) > 0):
    next_step = decide_step(steps)
    step_order += next_step
    steps = remove_step(steps, next_step)

step_order += last_step
print(step_order)

# Second star
def calc_job_time(step):
    return ord(step) - 4  # 60+ord(step)-64
    #return ord(step)-64

def find_possible_steps(steps, last_step):
    possible_steps = list()
    step1 = list()
    step2 = list()
    for tup in steps:
        step1.append(tup[0])
        step2.append(tup[1])
    for step in set(step1):
        if(step2.count(step) == 0):
            possible_steps.append(step)
    possible_steps.sort()
    return possible_steps

def print_status(elf_list, current_time):
    print(str(current_time) + ': ' + str(elf_list))

steps = read_input()[0]
last_step = find_last_step(steps)
current_time = 0
work_left = True
elf1 = [1, '', 0]
elf2 = [2, '', 0]
elf3 = [3, '', 0]
elf4 = [4, '', 0]
elf5 = [5, '', 0]
elf_list = (elf1,elf2,elf3,elf4,elf5)
steps_being_worked_on = list()
while (work_left):
    # Advance current jobs
    for elf in elf_list:
        if(elf[1] != ''):   #has a job
            elf[2] -= 1
            if(elf[2] == 0):
                steps = remove_step(steps, elf[1])
                steps_being_worked_on.remove(elf[1])
                elf[1] = ''
    # Assign new jobs
    poss = find_possible_steps(steps, last_step)
    if not poss:
        poss.append(last_step)
        if(last_step == ''):
            poss = []
        last_step = ''
    if poss:
        for step in poss:
            if step not in steps_being_worked_on:
                for elf in elf_list:
                    if(elf[1] == ''):
                        elf[1] = step
                        steps_being_worked_on.append(step)
                        elf[2] = calc_job_time(step)
                        break
    # Check if work left
    if(elf1[1] == '' and elf2[1] == '' and elf3[1] == '' and elf4[1] == '' and elf5[1] == ''):
        work_left = False
    print_status(elf_list, current_time)
    # Add time
    current_time += 1

print(current_time-1)
