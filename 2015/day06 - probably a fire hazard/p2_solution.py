
def parse_input(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    return [line.strip() for line in lines]


def initialize_brightness(size):
    """
    Initialize a grid with all brightness levels set to 0
    """
    return [[0] * size for _ in range(size)]


def apply_brightness_instructions(grid, instruction):
    """
    Apply a single brightness instruction to the grid
    """
    parts = instruction.split()
    if parts[0] == 'toggle':
        action = 'toggle'
        start_coords = parts[1]
        end_coords =parts[3]
    else:
        action = parts[1]  # on or off
        start_coords = parts[2]
        end_coords = parts[4]

    # parse the coordinations
    x1, y1 = map(int, start_coords.split(','))
    x2, y2 = map(int, end_coords.split(','))

    # apply the action
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            if action == 'on':
                grid[i][j] += 1
            elif action == 'off':
                grid[i][j] = max(0, grid[i][j] - 1)
            elif action == 'toggle':
                grid[i][j] += 2


def total_brightness(grid):
    """
    Count the number of lights that are lit in the grid
    """

    return sum(sum(row) for row in grid)


filename = 'input.txt'
instructions = parse_input(filename)
grid_size = 1000
grid = initialize_brightness(grid_size)

# apply instructions
for instruction in instructions:
    apply_brightness_instructions(grid, instruction)

# count the lit lights
result = total_brightness(grid)
print(result)
# answer is 14687245
