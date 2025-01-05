def count_neighbors(lights, x, y):
    """Count the number of 'on' neighbors for the light at (x, y)."""
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    return sum((x + dx, y + dy) in lights for dx, dy in directions)

def simulate_lights(initial_grid, steps):
    """Simulate the grid for a given number of steps with corner lights fixed."""
    corners = {(0, 0), (0, 99), (99, 0), (99, 99)}
    
    # Set of all lights that are on, starting with the initial configuration
    lights = corners | {(x, y) for y, line in enumerate(initial_grid)
                        for x, char in enumerate(line.strip())
                        if char == '#'}
    
    # Simulation for the given number of steps
    for _ in range(steps):
        # Calculate the new set of lights that are on
        new_lights = corners | {
            (x, y) for x in range(100) for y in range(100)
            if (x, y) in lights and 2 <= count_neighbors(lights, x, y) <= 3
            or (x, y) not in lights and count_neighbors(lights, x, y) == 3
        }
        lights = new_lights
    
    # Return the number of lights that are on
    return len(lights)


def parse_input(filename):
    with open(filename, 'r') as file:
        data = file.readlines()
    return data

# Initial grid
initial_grid = parse_input('input.txt')
result = simulate_lights(initial_grid, 100)
print(result)
# answer is 886