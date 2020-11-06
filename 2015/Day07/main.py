def isInt(str):
    try: 
        int(str)
        return True
    except ValueError:
        return False

def parseInstruction(instr):
    # Returns an instruction as [operation, arg1, arg2]. Unused parameters
    # are set to None.
    if instr[0] == 'NOT':
        return 'NOT', instr[1], None
    elif (len(instr) == 1):
        return None, instr[0], None
    else:
        return instr[1], instr[0], instr[2]

def getArg(arg, wire):
    # Check if the wire's signal is already known
    if (instructions[wire]['value'] != None):
        return instructions[wire]['value']
    
    # Try to convert argument to int, otherwise find signal of wire
    try: 
        num = int(arg)
        return num
    except ValueError:
        return getSignalOfWire(arg)

def getSignalOfWire(wire):
    value = instructions[wire]['value']
    instr = instructions[wire]['instr']
    
    # Base cases - Wire's signal value is known, or is already an integer.
    if (value != None):
        return value
    if (isInt(instr)):
        instructions[wire]['value'] = int(instr)
        return int(instr)
    
    # Recursivly find the value of wire
    op, arg1, arg2 = parseInstruction(instr.split())
    if (op == 'NOT'):
        mask = 0b1111111111111111
        result = getArg(arg1, wire) ^ mask 
        instructions[wire]['value'] = result    # Save calculated result to wire's value
        return result
    elif (op == 'AND'):
        result = getArg(arg1, wire) & getArg(arg2, wire)
        instructions[wire]['value'] = result
        return result
    elif (op == 'OR'):
        result = getArg(arg1, wire) | getArg(arg2, wire)
        instructions[wire]['value'] = result
        return result
    elif (op == 'RSHIFT'):
        result = getArg(arg1, wire) >> getArg(arg2, wire)
        instructions[wire]['value'] = result
        return result
    elif (op == 'LSHIFT'):
        result = getArg(arg1, wire) << getArg(arg2, wire)
        instructions[wire]['value'] = result
        return result
    elif (op == None):
        result = getArg(arg1, wire)
        instructions[wire]['value'] = result
        return result

# Get input        
lines = open('2015/Day07/input.txt').read().splitlines()
instructions = {}
for line in lines:
    l = line.split('->')
    d = {'instr' : l[0].strip(), 'value' : None}
    instructions[l[1].strip()] = d

# Part 1
wireASignal = getSignalOfWire('a')
print('Part 1: Wire A\'s signal is', wireASignal)

# Part 2
for key in instructions:
    instructions[key]['value'] = None                   # Reset wire values

instructions['b']['instr'] = wireASignal                # Override wire B's value
print('Part 2: Wire A\'s signal is', getSignalOfWire('a'))