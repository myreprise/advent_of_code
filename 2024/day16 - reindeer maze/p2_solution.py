from heapq import heappop, heappush

def part2(grid):
    #grid = puzzle_input.split('\n')
    m, n = len(grid), len(grid[0])

    # Finding the start and end positions
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 'S':
                start = (i, j)
            elif grid[i][j] == 'E':
                end = (i, j)

    # Replacing the 'E' with '.' in the grid for traversal
    grid[end[0]] = grid[end[0]].replace('E', '.')

    # Helper function to check if a cell can be visited
    def can_visit(d, i, j, score):
        prev_score = visited.get((d, i, j))
        if prev_score and prev_score < score:
            return False
        visited[(d, i, j)] = score
        return True

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Directions (East, South, West, North)
    heap = [(0, 0, *start, {start})]  # (score, direction, x, y, path)
    visited = {}  # visited stores the lowest score for each (direction, x, y) tuple
    lowest_score = None
    winning_paths = set()  # Set to store all the best paths

    while heap:
        score, d, i, j, path = heappop(heap)

        # If the current score is already greater than the lowest score found, stop exploring further
        if lowest_score and lowest_score < score:
            break

        # If the end is reached, update the winning paths
        if (i, j) == end:
            lowest_score = score
            winning_paths |= path  # Adding the current path to the winning paths
            continue

        # Skip paths that have already been visited with a better score
        if not can_visit(d, i, j, score):
            continue

        # Move forward
        x = i + directions[d][0]
        y = j + directions[d][1]
        if grid[x][y] == '.' and can_visit(d, x, y, score + 1):
            heappush(heap, (score + 1, d, x, y, path | {(x, y)}))

        # Rotate clockwise (right turn)
        right = (d + 1) % 4
        if can_visit(right, i, j, score + 1000):
            heappush(heap, (score + 1000, right, i, j, path))

        # Rotate counterclockwise (left turn)
        left = (d - 1) % 4
        if can_visit(left, i, j, score + 1000):
            heappush(heap, (score + 1000, left, i, j, path))

    # Return the number of distinct tiles that are part of at least one optimal path
    return len(winning_paths)

filename = "input.txt"
def parse_input(filename):
    with open(filename, 'r') as file:
        grid = [line.strip() for line in file.readlines()]
    return grid

maze_lines = parse_input(filename)

result = part2(maze_lines)
print(result)
# answer is 449
