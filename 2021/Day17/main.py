from operator import itemgetter

def within_target_area(x, y, target_x, target_y):
    if (target_x[0] <= x <= target_x[1]) and (target_y[0] <= y <= target_y[1]):
        return True
    else:
        return False

# Puzzle input
target_x = (236, 262)
target_y = (-78,-58)

# Part 1 & 2
highest_y_positions = []
velocities = []

for initial_x_vel in range(1,target_x[1]+1):
    for initial_y_vel in range(target_y[0], 100):
        x,y = 0,0
        x_velocity, y_velocity = initial_x_vel, initial_y_vel
        positions = []
        while(True):            # Simulate the trajectory
            x += x_velocity
            y += y_velocity
            positions.append((x,y))     # Saving all positions in the trajectory

            # Changing the velocities due to drag and gravity
            if x_velocity > 0:
                x_velocity -=1
            elif x_velocity < 0:
                x_velocity += 1
            y_velocity -= 1

            # Checking if the probe is inside the area or has passed area
            if(within_target_area(x, y, target_x, target_y)):     # Inside target area
                highest_y = max(positions, key=itemgetter(1))[1]
                highest_y_positions.append(highest_y)
                velocities.append((initial_x_vel, initial_y_vel))
                break
            if ( x > target_x[1] or y < target_y[0]):           # Passed target area
                break

print(f'Part 1: The highest y position is {max(highest_y_positions)}.')
print(f'Part 2: The number of initial velocity values is {len(velocities)}.')
