def look_and_say_round(seq):
    output = []
    i = 0
    while(i < len(seq)):
        # Append number of digits 
        num_of_digits = 1
        for j in range(i+1, len(seq)):
            if(seq[i] == seq[j]):
                num_of_digits += 1
            else:
                break
        output.append(str(num_of_digits))

        # Append digit
        output.append(seq[i])

        # Increment read-position
        i += num_of_digits
    return ''.join(output)

puzzle_input = '1321131112'

# --- Part 1 ---
rounds = 40
seqence = puzzle_input
for round in range(rounds):
    seqence = look_and_say_round(seqence)
print('Part 1: The length of the result is', len(seqence))

# --- Part 2 ---
rounds = 50
seqence = puzzle_input
for round in range(rounds):
    seqence = look_and_say_round(seqence)
print('Part 2: The length of the result is', len(seqence))
