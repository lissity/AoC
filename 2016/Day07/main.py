def check_TLS_support(letter_seq):
    abba_inside = False
    abba_outside = False
    inside_square_bracket = False
    for i in range(0, len(letter_seq)-3):
        if(letter_seq[i] == '['):
            inside_square_bracket = True
        elif (letter_seq[i] == ']'):
            inside_square_bracket = False
        elif (letter_seq[i].isalpha() and letter_seq[i+1].isalpha() and
              letter_seq[i+2].isalpha() and letter_seq[i+3].isalpha()):
            let_1 = letter_seq[i]
            let_2 = letter_seq[i+1]
            let_3 = letter_seq[i+2]
            let_4 = letter_seq[i+3]
            if(let_1 == let_2):
                pass
            elif((let_1+let_2) == (let_4+let_3)): # ABBA found
                if (inside_square_bracket):
                    abba_inside = True
                else:
                    abba_outside = True
    return (abba_outside and not abba_inside)

def check_SSL_support(letter_seq):
    abas = []
    babs = []
    inside_square_bracket = False
    for i in range(0, len(letter_seq)-2):
        if(letter_seq[i] == '['):
            inside_square_bracket = True
        elif (letter_seq[i] == ']'):
            inside_square_bracket = False
        elif (letter_seq[i].isalpha() and letter_seq[i+1].isalpha() and
              letter_seq[i+2].isalpha()):
            let_1 = letter_seq[i]
            let_2 = letter_seq[i+1]
            let_3 = letter_seq[i+2]
            if(let_1 == let_2):
                pass
            elif(let_1 == let_3): # ABA/BAB found
                if (inside_square_bracket):
                    babs.append(let_1+let_2+let_3)
                else:
                    abas.append(let_1+let_2+let_3)
    # Check found ABAs for corresponding BABs
    for aba in set(abas):
        corr_bab =  aba[1] + aba[0] + aba[1]
        if corr_bab in set(babs):
            return True
    return False

# Obtain input
ip_addresses = [l.strip() for l in open('2016/Day07/input.txt').readlines()]

# First star
count = 0
for ip in ip_addresses:
    if(check_TLS_support(ip) == True):
        count += 1
print('[part1] The number of IPs that support TLS is {}'.format(count))

# Second star
count = 0
for ip in ip_addresses:
    if(check_SSL_support(ip)):
        count += 1
print('[part2] The number of IPs that support SSL is {}'.format(count))
