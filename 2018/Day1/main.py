# First star
frequency_changes = list(map(int,open("Day1/input.txt",'r').read().splitlines()))
print('Resulting frequency: ', sum(frequency_changes))

# Second star
previous_frequencies = {}
frequency = 0;
answer_found = False;
while(not answer_found):
    for freq_change in frequency_changes:
        frequency += freq_change
        if frequency in previous_frequencies:
            answer_found = True
            print('First frequency your device reaches twice:', frequency)
            break
        else:
            previous_frequencies[frequency] = "found"
