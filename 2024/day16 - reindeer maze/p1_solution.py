import heapq

# Directions: N, E, S, W (North, East, South, West)
DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def find_lowest_score(grid):
    rows, cols = len(grid), len(grid[0])
    
    # Find start (S) and end (E) positions
    start, end = None, None
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'S':
                start = (r, c)
            elif grid[r][c] == 'E':
                end = (r, c)

    # Priority queue for Dijkstra's Algorithm
    pq = [(0, start[0], start[1], 1)]  # (cost, row, col, direction)
    visited = set()  # To track visited states (row, col, direction)

    while pq:
        cost, r, c, direction = heapq.heappop(pq)
        
        # Stop when we reach the end position
        if (r, c) == end:
            return cost
        
        # Skip if already visited with the same direction
        if (r, c, direction) in visited:
            continue
        visited.add((r, c, direction))
        
        # Option 1: Move forward
        dr, dc = DIRECTIONS[direction]
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != '#':
            heapq.heappush(pq, (cost + 1, nr, nc, direction))
        
        # Option 2: Turn left (counterclockwise)
        left_direction = (direction - 1) % 4
        heapq.heappush(pq, (cost + 1000, r, c, left_direction))
        
        # Option 3: Turn right (clockwise)
        right_direction = (direction + 1) % 4
        heapq.heappush(pq, (cost + 1000, r, c, right_direction))

    return -1  # If no path is found (shouldn't happen with a valid input)


filename = 'input.txt'

with open(filename, 'r') as file:
    data = file.read().splitlines()
grid = [line.strip() for line in data]

# Solve the problem
lowest_score = find_lowest_score(grid)
print(f"The lowest score is: {lowest_score}")
# answer is 73404