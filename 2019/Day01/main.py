def fuel_required(mass):
    return int(mass/3)-2

# Obtain input
module_masses = [int(line.strip()) for line in open('2019/Day01/input.txt', 'r').readlines()]

# First star
fuel_sum = 0
for mass in module_masses:
    fuel_sum += fuel_required(mass)
print('[part1] The fuel requirements for all the modules are {}'.format(fuel_sum))

# Second star
fuel_sum = 0
for mass in module_masses:
    module_fuel = fuel_required(mass)
    fuel_sum += module_fuel
    fuel_for_fuel = module_fuel
    while True:
        fuel_for_fuel = fuel_required(fuel_for_fuel)
        if(fuel_for_fuel <= 0):
            break
        fuel_sum += fuel_for_fuel
print('[part2] The fuel requirements for all the modules and the fuel itself is {}'.format(fuel_sum))
