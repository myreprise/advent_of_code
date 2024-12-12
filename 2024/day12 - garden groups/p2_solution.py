from collections import deque

# Directions: up, down, left, right
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def parse_input(filename):

    with open(filename, 'r') as file:
        data = file.read().splitlines()
    
    return [list(line.strip()) for line in data]

def calculate_fence_price(grid):
    rows = len(grid)
    cols = len(grid[0])
    
    visited = [[False] * cols for _ in range(rows)]  # To track visited cells

    def bfs(start_i, start_j):
        plant_type = grid[start_i][start_j]
        area = 0
        sides = 0
        perimeter_cells = {}  # To track perimeter directions
        queue = deque([(start_i, start_j)])
        visited[start_i][start_j] = True

        while queue:
            i, j = queue.popleft()
            area += 1
            # Check all 4 possible sides (up, down, left, right)
            for di, dj in DIRECTIONS:
                ni, nj = i + di, j + dj
                # If it's out of bounds or a different plant type, it's part of the perimeter
                if ni < 0 or ni >= rows or nj < 0 or nj >= cols or grid[ni][nj] != plant_type:
                    sides += 1  # This contributes to the perimeter
                    # Store the direction of the perimeter segment
                    if (di, dj) not in perimeter_cells:
                        perimeter_cells[(di, dj)] = set()
                    perimeter_cells[(di, dj)].add((i, j))
                elif not visited[ni][nj] and grid[ni][nj] == plant_type:
                    visited[ni][nj] = True
                    queue.append((ni, nj))

        # Calculate the sides by processing the perimeter cells
        actual_sides = 0
        for direction, cells in perimeter_cells.items():
            seen_perimeter = set()
            for cell in cells:
                if cell not in seen_perimeter:
                    actual_sides += 1
                    subqueue = deque([cell])
                    while subqueue:
                        ci, cj = subqueue.popleft()
                        if (ci, cj) in seen_perimeter:
                            continue
                        seen_perimeter.add((ci, cj))
                        for di, dj in DIRECTIONS:
                            ni, nj = ci + di, cj + dj
                            if (ni, nj) in cells:
                                subqueue.append((ni, nj))
        
        return area, actual_sides

    total_cost_p2 = 0  # Total cost based on sides

    # Loop through the grid to find all regions (using BFS)
    for i in range(rows):
        for j in range(cols):
            if not visited[i][j]:
                area, sides = bfs(i, j)
                total_cost_p2 += area * sides  # Sides-based cost (for p2)

    return total_cost_p2


filename = 'input.txt'
grid = parse_input(filename)

# Calculate total fence cost
result = calculate_fence_price(grid)
print(result)
# answer is 902620