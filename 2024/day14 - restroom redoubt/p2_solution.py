import os
import time

# Define the constants for the space dimensions and simulation time
WIDTH = 101
HEIGHT = 103
SECONDS = 100
DELAY = 0.05


def import_data(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    return [line.strip() for line in lines]


def parse_data(data):
    robots = []
    for line in data:
        parts = line.split()
        position = tuple(map(int, parts[0][2:].split(',')))
        velocity = tuple(map(int, parts[1][2:].split(',')))
        robots.append((position, velocity))
    return robots

def simulate_motion(robots, seconds, width, height):
    final_positions = []
    for position, velocity in robots:
        x = (position[0] + velocity[0] * seconds) % width
        y = (position[1] + velocity[1] * seconds) % height
        final_positions.append((x, y))
    return final_positions

def simulate_until_unique_positions(robots, width, height, max_seconds=10000):
    """
    Simulate robot motion until all robots are in unique positions
    """
    for t in range(max_seconds):
        positions = [
            ((pos[0] + vel[0] * t) % width, (pos[1] + vel[1] * t) % height)
            for pos, vel in robots
        ]

        # Check if all positions are uniqe
        if len(set(positions)) == len(positions):
            return t, positions
    
    return None, None  # Return None if not found within max_seconds

def visualize_positions(positions, width, height):
    # Create a grid representation of the positions
    grid = [['.' for _ in range(width)] for _ in range(height)]

    for x, y in positions:
        grid[y][x] = '#'
    return '\n'.join(''.join(row) for row in grid)

def clear_terminal():
    """
    Clear the terminal screen.
    """
    os.system('cls' if os.name  == 'nt' else 'clear')

def visualize_movement(robots, width, height, max_seconds, delay):
    """
    Visualize robots assembling into formation
    """

    for t in range(max_seconds):
        # Calculate positions at time t
        positions = [
            ((pos[0] + vel[1] * t) % width, (pos[1] + vel[1] * t) % height)
            for pos, vel in robots
        ]

        # Create a gird for the current time
        grid = [['.' for _ in range(width)] for _ in range(height)]
        for x, y in positions:
            grid[y][x] = '#'
        
        # Clear the terminal and print the grid
        clear_terminal()
        print(f'Seconds: {t}')
        for row in grid:
            print(''.join(row))
        
        # Pause for a short delay


filename = 'input.txt'
data = import_data(filename)
#print(data)

robots = parse_data(data)
#print(robots)


unique_time, unique_positions = simulate_until_unique_positions(robots, WIDTH, HEIGHT)
# Visualization of the unique positions
if unique_positions:
    unique_pattern = visualize_positions(unique_positions, WIDTH, HEIGHT)
    print("Minimum Time for Unique Positions (seconds):", unique_time)
else:
    print("Unique positions not achieved within the maximum time limit.")
# answer is 6355

visualize_movement(robots, WIDTH, HEIGHT, unique_time, DELAY)
