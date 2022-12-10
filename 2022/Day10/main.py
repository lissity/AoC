def recordSignalStrength(cycle, regX):
    if cycle in [20,60,100,140,180,220]:
        signal_strength.append(cycle*regX)

def performCycleWork(screen, screen_row, cycle, reg_X):
    # Record signal strength for Part 1
    recordSignalStrength(cycle, reg_X)

    # Draw to screen for Part 2
    if cycle != 1 and (cycle - 1) % 40 == 0:
       screen.append(screen_row.copy())
       screen_row.clear()
    screen_row.append(drawPixel(cycle, reg_X))

def drawPixel(cycle, regX):
    pos = (cycle - 1) % 40
    if pos in [regX-1, regX, regX+1]:
        return '█'      # Lit pixel
    else:
        return ' '      # Dark pixel

# Obtain input
instructions = [line.strip().split()
                for line in open('2022/Day10/input.txt').readlines()]

# Part 1 & 2
cycle = 1
reg_X = 1
signal_strength = []
screen = []
screen_row = []

for i in range(len(instructions)):
    if instructions[i][0] == 'noop':        # Takes 1 cycle to complete
        performCycleWork(screen, screen_row, cycle, reg_X)
        cycle += 1

    elif instructions[i][0] == 'addx':      # Takes 2 cycles to complete
        performCycleWork(screen, screen_row, cycle, reg_X)
        cycle += 1      

        performCycleWork(screen, screen_row, cycle, reg_X)
        cycle += 1
        reg_X += int(instructions[i][1])    # Reg_X is changed

screen.append(screen_row)                   # Adding the last row to screen

print(f'Part 1: The sum of signal strengths is {sum(signal_strength)}.')
print(f'Part 2: ')
for i in range(len(screen)):
    print(''.join(screen[i]))
