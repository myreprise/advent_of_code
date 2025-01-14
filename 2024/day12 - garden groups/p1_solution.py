from collections import deque

# Directions for moving (up, down, left, right)
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def parse_input(filename):

    with open(filename, 'r') as file:
        data = file.read().splitlines()
    
    return [list(line.strip()) for line in data]

def in_bounds(x, y, rows, cols):
    """
    Check if position (x, y) is within the grid boundaries
    """

    return 0 <= x < rows and 0 <= y < cols

def calculate_perimeter_and_area(gird, visited, start_x, start_y, plant_type):
    """
    Calculate the area and perimeter of a region using BFS
    """
    area = 0
    perimeter = 0
    queue = deque([(start_x, start_y)])
    visited[start_x][start_y] = True

    while queue:
        x, y = queue.popleft()
        area += 1

        # Check the four possible directions for the perimeter
        local_perimeter = 0
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if not in_bounds(nx, ny, len(grid), len(grid[0])) or grid[nx][ny] != plant_type:
                local_perimeter += 1
            elif not visited[nx][ny] and grid[nx][ny] == plant_type:
                visited[nx][ny] = True
                queue.append((nx, ny))
        
        perimeter += local_perimeter
    
    return area, perimeter

def total_fence_cost(grid):
    """
    Calculate the total fencing cost
    """
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    total_cost = 0

    for x in range(rows):
        for y in range(cols):
            if not visited[x][y]:
                plant_type = grid[x][y]
                area, perimeter = calculate_perimeter_and_area(grid, visited, x, y, plant_type)
                total_cost += area * perimeter
    
    return total_cost


filename = 'input.txt'
grid = parse_input(filename)

# Calculate total fence cost
result = total_fence_cost(grid)
print(result)
# answer is 1473620