class PasswordInfo:
    def __init__(self, lower_limit, upper_limit, letter, password):
        self.lower_limit = lower_limit
        self.upper_limit = upper_limit
        self.letter = letter
        self.password = password

def isPasswordValidPart1(pwd_info):
    count = pwd_info.password.count(pwd_info.letter)
    if (count not in range(pwd_info.lower_limit, pwd_info.upper_limit + 1)):
        return False
    return True

def isPasswordValidPart2(pwd_info):
    if ((pwd_info.password[pwd_info.lower_limit-1] == pwd_info.letter) and
        (pwd_info.password[pwd_info.upper_limit-1] != pwd_info.letter)):
        return True
    if ((pwd_info.password[pwd_info.lower_limit-1] != pwd_info.letter) and
        (pwd_info.password[pwd_info.upper_limit-1] == pwd_info.letter)):
        return True
    return False

# Obtain input
password_rows = [line.strip() for line in open('2020/Day02/input.txt', 'r').readlines()]

# Parse input in format "1-3 a: abcde" and add information to PasswordInfo object 
password_info_list = []
for row in password_rows:
    tmp_row = row.split(" ")
    pwd_info = PasswordInfo(int(tmp_row[0].split("-")[0]),
                            int(tmp_row[0].split("-")[1]),
                            tmp_row[1][0],
                            tmp_row[2])
    password_info_list.append(pwd_info)

# Part 1
counter = 0
for password in password_info_list:
    if (isPasswordValidPart1(password)):
        counter += 1
print(f"Part 1: The number of valid passwords are {counter}")

#Part 2
counter = 0
for password in password_info_list:
    if (isPasswordValidPart2(password)):
        counter += 1
print(f"Part 2: The number of valid passwords are {counter}")
