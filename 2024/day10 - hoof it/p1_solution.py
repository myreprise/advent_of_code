from collections import deque

def parse_input(filename):

    with open(filename, 'r') as file:
        data = file.read().splitlines()

    return [list(map(int, line.strip())) for line in data]

def is_valid_move(grid, x, y, current_height):
    """
    Check if move is valid
    """

    rows, cols = len(grid), len(grid[0])
    return (
        0 <= x < rows and 0 <= y < cols
        and grid[x][y] == current_height + 1  # increment height
    )

def bfs_trailhead(grid, start_x, start_y):
    """
    Perform BFS to find all reachable 9s from a trailhead.
    """
    queue = deque([(start_x, start_y)])
    visited = set([(start_x, start_y)])
    reachable_nines = set()

    while queue:
        x, y = queue.popleft()
        current_height = grid[x][y]

        if current_height == 9:
            reachable_nines.add((x, y))
            continue

        # Explore neighbors
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if (nx, ny) not in visited and is_valid_move(grid, nx, ny, current_height):
                queue.append((nx, ny))
                visited.add((nx, ny))

    return len(reachable_nines)

def sum_trailhead_scores(grid):
    """
    Calculate the sum of scores of all trailheads.
    """

    total_score = 0
    rows, cols = len(grid), len(grid[0])

    for x in range(rows):
        for y in range(cols):
            if grid[x][y] == 0:
                total_score += bfs_trailhead(grid, x, y)

    return total_score

filename = 'input.txt'
topographic_map = parse_input(filename=filename)

trailhead_score = sum_trailhead_scores(topographic_map)

print(trailhead_score)
# answer is 798
