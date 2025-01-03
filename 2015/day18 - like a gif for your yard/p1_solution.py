
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
        row = []
        for y in range(len(grid[0])):
            neighbors = count_neighbors(grid, x, y)
            if grid[x][y] == '#':
                row.append('#' if neighbors in [2, 3] else '.')
            else:
                row.append('#' if neighbors == 3 else '.')
        new_grid.append(row)
    return new_grid

def count_lights(grid):
    """
    Count the number of lights that are on ('#')
    """
    return sum(row.count('#') for row in grid)

def simulate_lights(initial_grid, steps):
    """
    Simulate the grid for a number of steps.
    """
    grid = initial_grid
    for _ in range(steps):
        grid = update_grid(grid)
    return count_lights(grid)



filename = 'input.txt'

grid = parse_input(filename)
result = simulate_lights(grid, 100)
print(result)
# answer is 821