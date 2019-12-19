import re
import itertools
import copy
import math

class Moon:
    def __init__(self, x, y, z):
        self.pos = {'x': x, 'y': y, 'z': z}
        self.vel = {'x': 0, 'y': 0, 'z': 0}

    def get_state(self, axis):
        return str(self.pos[axis]) + ',' + str(self.vel[axis]) + ','

    def update_velocity(self, x, y, z):
        self.vel['x'] += x
        self.vel['y'] += y
        self.vel['z'] += z

    def print_moon(self):
        print(self.pos, self.vel)

    def update_position(self):
        self.pos['x'] += self.vel['x']
        self.pos['y'] += self.vel['y']
        self.pos['z'] += self.vel['z']

    def calc_total_energy(self):
        potential = abs(self.pos['x']) + abs(self.pos['y'])  + abs(self.pos['z'])
        kinetic = abs(self.vel['x']) + abs(self.vel['y'])  + abs(self.vel['z'])
        return potential * kinetic

def apply_gravity(moon1, moon2):
    moon1_velocity_change = [0,0,0]
    moon2_velocity_change = [0,0,0]
    axis = ['x', 'y', 'z']
    for i in range(0,3):
        if(moon1.pos[axis[i]] > moon2.pos[axis[i]]):
            moon1_velocity_change[i] = -1
            moon2_velocity_change[i] = 1
        elif(moon1.pos[axis[i]] < moon2.pos[axis[i]]):
            moon1_velocity_change[i] = 1
            moon2_velocity_change[i] = -1
    moon1.update_velocity(*moon1_velocity_change)
    moon2.update_velocity(*moon2_velocity_change)

def get_axis_state(moons, axis):
    state = ''
    for moon in moons:
        state += moon.get_state(axis)
    return state

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

# Obtain input
input = open('2019/Day12/input.txt', 'r').readlines()
moons_start = []
for planet_pos in input:
    position = list(map(int, re.findall(r'-?\d+', planet_pos)))
    moon = Moon(*position)
    moons_start.append(moon)

# --- Part1 ---
moons = copy.deepcopy(moons_start)
for i in range(0, 1000):
    # Update velocity by applying gravity
    for combo in list(itertools.combinations(moons, 2)):
        apply_gravity(combo[0], combo[1])
    # Update position by applying velocity
    for moon in moons:
        moon.update_position()

print('[part1] The total energy in the system is {}'.format(sum([moon.calc_total_energy() for moon in moons])))

# --- Part2 ---
moons = copy.deepcopy(moons_start)
initial_state_x = get_axis_state(moons, 'x')
initial_state_y = get_axis_state(moons, 'y')
initial_state_z = get_axis_state(moons, 'z')
x_cycle = 0
y_cycle = 0
z_cycle = 0
ts = 0
while(not (x_cycle and y_cycle and z_cycle)):
    # Update velocity by applying gravity
    for combo in list(itertools.combinations(moons, 2)):
        apply_gravity(combo[0], combo[1])
    # Update position by applying velocity
    for moon in moons:
        moon.update_position()
    ts += 1
    # Check if x, y, or z, has completed a cycle.
    if(x_cycle == 0 and initial_state_x == get_axis_state(moons, 'x')):
        x_cycle = ts
    if(y_cycle == 0 and initial_state_y == get_axis_state(moons, 'y')):
        y_cycle = ts
    if(z_cycle == 0 and initial_state_z == get_axis_state(moons, 'z')):
        z_cycle = ts

x_y_lcm = lcm(x_cycle, y_cycle)
x_y_z_lcm = lcm(x_y_lcm, z_cycle)
print('[part2] It takes {} steps to reach a state that matches a previous state'\
      .format(x_y_z_lcm))
