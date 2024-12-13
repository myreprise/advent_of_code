
def parse_input(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    return [line.strip() for line in lines]

def initialize_grid(size):
    """
    Initialize a grid with all lights turned off
    """
    return [[0] * size for _ in range(size)]

def apply_instructions(grid, instruction):
    """
    Apply a single instruction to the grid
    """
    parts = instruction.split()
    if parts[0] == 'toggle':
        action = 'toggle'
        start_coords = parts[1]
        end_coords =parts[3]
    else:
        action = parts[1]
        start_coords = parts[2]
        end_coords = parts[4]

    # parse the coordinations
    x1, y1 = map(int, start_coords.split(','))
    x2, y2 = map(int, end_coords.split(','))

    # apply the action
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            if action == 'on':
                grid[i][j] = 1
            elif action == 'off':
                grid[i][j] = 0
            elif action == 'toggle':
                grid[i][j] = 1 - grid[i][j]

def count_lit_lights(grid):
    """
    Count the number of lights that are lit in the grid
    """

    return sum(sum(row) for row in grid)

filename = 'input.txt'
instructions = parse_input(filename)

grid_size = 1000
grid = initialize_grid(grid_size)

# apply instructions
for instruction in instructions:
    apply_instructions(grid, instruction)

# count the lit lights
result = count_lit_lights(grid)
print(result)
# answer is 543903
