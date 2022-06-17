def hasValidData(passport):
    for field_data in passport:
        field = field_data.split(":")[0]
        value = field_data.split(":")[1]
        if (field == "byr"):
            if (not(value.isnumeric() and 1920 <= int(value) <= 2002)):
                return False
        elif (field == "iyr"):
            if (not(value.isnumeric() and 2010 <= int(value) <= 2020)):
                return False
        elif (field == "eyr"):
            if (not(value.isnumeric() and 2020 <= int(value) <= 2030)):
                return False
        elif (field == "hgt"):
            unit = value[-2:]
            length = value[:-2]
            if ((not(unit in ['in', 'cm']))):
                return False
            if (unit == 'cm'):
                if (not(length.isnumeric() and 150 <= int(length) <= 193)):
                    return False
            elif (unit == 'in'):
                if (not(length.isnumeric() and 59 <= int(length) <= 76)):
                    return False
        elif (field == "hcl"):
            if (not(value[0] == '#' and value[1:].isalnum() and len(value[1:]) == 6)):
                return False
        elif (field == "ecl"):
            valid_eye_color = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
            if (not(value in valid_eye_color)):
                return False
        elif (field == "pid"):
            if (not (value.isnumeric() and len(value) == 9)):
                return False
    return True

# Obtain input
passports = [passport.replace('\n', ' ') for passport in 
            open('2020/Day04/input.txt', 'r').read().split("\n\n")]
passports = [p.split() for p in passports]

# Part 1
req_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
valid_passport_cnt = 0
for passport in passports:
    field_names = [field.split(':')[0] for field in passport]
    if all(field in field_names for field in req_fields):
        valid_passport_cnt += 1

print(f"Part 1: {valid_passport_cnt} passports are valid (has the required " +
        "fields).")

# Part 2
valid_passport_cnt = 0
for passport in passports:
    field_names = [field.split(':')[0] for field in passport]
    if all(field in field_names for field in req_fields):
        if hasValidData(passport):
            valid_passport_cnt += 1

print(f"Part 2: {valid_passport_cnt} passports are valid (has the required " +
        "fields and valid values).")
