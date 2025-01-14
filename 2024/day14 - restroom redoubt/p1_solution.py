
# Define the constants for the space dimensions and simulation time
WIDTH = 101
HEIGHT = 103
SECONDS = 100


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

def count_quadrants(positions, width, height):
    mid_x = width // 2
    mid_y = height // 2
    
    quadrants = [0, 0, 0, 0]  # TL, TR, BL, BR
    
    for x, y in positions:
        if x == mid_x or y == mid_y:
            continue
        if x < mid_x and y > mid_y:
            quadrants[0] += 1  # Top-left
        elif x >= mid_x and y > mid_y:
            quadrants[1] += 1  # Top-right
        elif x < mid_x and y < mid_y:
            quadrants[2] += 1  # Bottom-left
        elif x > mid_x and y < mid_y:
            quadrants[3] += 1  # Bottom-right
    
    return quadrants

def calculate_safety_factor(quadrants):
    factor = 1
    for count in quadrants:
        factor *= count
    return factor


filename = 'input.txt'
data = import_data(filename)
#print(data)

robots = parse_data(data)
#print(robots)

final_positions = simulate_motion(robots=robots, seconds=SECONDS, width=WIDTH, height=HEIGHT)
quadrants = count_quadrants(positions=final_positions, width=WIDTH, height=HEIGHT)
safety_factor = calculate_safety_factor(quadrants)

print("Final Quadrants Count:", quadrants)

print(safety_factor)
# answer is 220971520