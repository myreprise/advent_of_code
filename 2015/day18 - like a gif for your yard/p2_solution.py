
def parse_input(filename):
    with open(filename, 'r') as file:
        return [list(line.strip()) for line in file]


def count_neighbors(grid, x, y):
    """
    Count the number of neighbors that are on.
    """
    directions = [(-1, 1), (-1, 0), (-1, -1), (0, 1), (0, -1), (1, 1), (1, 0), (1, -1)]
    count = 0
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == '#':
            count += 1
    return count


def update_grid(grid):
    """
    Update grid based on the rules.
    """
    new_grid = []
    for x in range(len(grid)):
        new_row = []
        for y in range(len(grid[0])):
            # Skip the four corner lights and keep them on
            if (x == 0 and y == 0) or (x == 0 and y == len(grid[0])-1) or (x == len(grid)-1 and y == 0) or (x == len(grid)-1 and y == len(grid[0])-1):
                new_row.append('#')
            else:
                on_neighbors = count_neighbors(grid, x, y)
                if grid[x][y] == '#':
                    if on_neighbors == 2 or on_neighbors == 3:
                        new_row.append('#')
                    else:
                        new_row.append('.')
                else:  # grid[x][y] == '.'
                    if on_neighbors == 3:
                        new_row.append('#')
                    else:
                        new_row.append('.')
        new_grid.append(new_row)
    return new_grid  # Return the updated grid


def count_lights(grid):
    """
    Count the number of lights that are on ('#')
    """
    return sum(row.count('#') for row in grid)


def simulate_lights(initial_grid, steps):
    """Simulate the grid for a given number of steps."""
    grid = initial_grid
    for step in range(steps):
        grid = update_grid(grid)  # Update grid and reassign to grid
        # print(f"\nStep {step+1}:")
        # for row in grid:
        #     print("".join(row))
    return count_lights(grid)  # Return the result after steps


filename = 'input.txt'

grid = parse_input(filename)
result = simulate_lights(grid, 100)
print(result)
# answer is 886
# answer is not 865 (too low)
# answer is not 893 (too high)