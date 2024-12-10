
def parse_input(filename):

    with open(filename, 'r') as file:
        data = file.read().splitlines()

    return [list(map(int, line.strip())) for line in data]

def dfs_count_paths(grid, x, y, path, visited):
    """
    Perform DFS to count distinct paths from the current position to height 9.
    """
    rows, cols = len(grid), len(grid[0])
    if grid[x][y] == 9:
        # Reached height 9; add path to visited paths
        visited.add(tuple(path))
        return

    # Explore neighbors (up, down, left, right)
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols:  # Within bounds
            if grid[nx][ny] == grid[x][y] + 1:  # Incremental height
                dfs_count_paths(grid, nx, ny, path + [(nx, ny)], visited)

def calculate_trailhead_rating(grid, start_x, start_y):
    """
    Calculate the rating of a single trailhead.
    """
    visited_paths = set()
    dfs_count_paths(grid, start_x, start_y, [(start_x, start_y)], visited_paths)
    return len(visited_paths)

def sum_trailhead_ratings(grid):
    """
    Calculate the sum of ratings of all trailheads.
    """

    total_rating = 0
    rows, cols = len(grid), len(grid[0])

    for x in range(rows):
        for y in range(cols):
            if grid[x][y] == 0:  # Trailhead found
                total_rating += calculate_trailhead_rating(grid, x, y)

    return total_rating

filename = 'input.txt'
topographic_map = parse_input(filename)
result = sum_trailhead_ratings(topographic_map)
print(result)
# answer is 1816
