def read_input_file(file_path):
    """
    Reads the input file and converts it into a 2D grid.
    """
    with open(file_path, 'r') as file:
        grid = [line.strip() for line in file.readlines()]
    return grid

def extract_guard_path(grid):
    """
    Extracts all unique coordinates from the guard's path.
    """
    directions = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}
    right_turn = {'^': '>', '>': 'v', 'v': '<', '<': '^'}
    
    # Find the guard's initial position and direction
    guard_pos = None
    guard_dir = None
    for r, row in enumerate(grid):
        for c, char in enumerate(row):
            if char in directions:
                guard_pos = (r, c)
                guard_dir = char
                break
        if guard_pos:
            break
    
    rows, cols = len(grid), len(grid[0])
    visited_positions = set()  # Track unique coordinates of the guard's path
    
    while True:
        # Mark the current position as visited
        visited_positions.add(guard_pos)
        
        # Move to the next position
        r, c = guard_pos
        dr, dc = directions[guard_dir]
        next_pos = (r + dr, c + dc)
        
        # Check if the guard exits the grid
        if not (0 <= next_pos[0] < rows and 0 <= next_pos[1] < cols):
            break  # Exit simulation when out of bounds
        
        # Check if the next position is an obstacle
        if grid[next_pos[0]][next_pos[1]] == '#':
            guard_dir = right_turn[guard_dir]  # Turn right
        else:
            guard_pos = next_pos  # Move forward
    
    return visited_positions

def simulate_guard_with_obstruction(grid, obstruction_pos, max_steps=10000):
    """
    Simulates the guard's movement with an obstruction at a given position and checks if it causes a loop.
    """
    directions = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}
    right_turn = {'^': '>', '>': 'v', 'v': '<', '<': '^'}
    
    # Find the guard's initial position and direction
    guard_pos = None
    guard_dir = None
    for r, row in enumerate(grid):
        for c, char in enumerate(row):
            if char in directions:
                guard_pos = (r, c)
                guard_dir = char
                break
        if guard_pos:
            break
    
    # Create a copy of the grid
    new_grid = [list(row) for row in grid]
    r, c = obstruction_pos
    new_grid[r][c] = '#'
    
    visited_positions = set()
    step_count = 0
    
    while step_count < max_steps:
        r, c = guard_pos
        dr, dc = directions[guard_dir]
        next_pos = (r + dr, c + dc)
        
        # Check if the guard exits the grid
        if not (0 <= next_pos[0] < len(grid) and 0 <= next_pos[1] < len(grid[0])):
            break  # Exit simulation when out of bounds
        
        # Move the guard
        if new_grid[next_pos[0]][next_pos[1]] == '#':
            guard_dir = right_turn[guard_dir]  # Turn right
        else:
            guard_pos = next_pos  # Move forward
        
        # Check for loops
        if (guard_pos, guard_dir) in visited_positions:
            return True  # A loop has been detected
        
        visited_positions.add((guard_pos, guard_dir))
        step_count += 1
    
    return False  # No loop detected or max steps reached

def count_valid_obstructions(grid, max_steps=10000):
    """
    Counts how many valid obstruction placements cause the guard to get stuck in a loop.
    """
    # Extract all unique coordinates from the guard's path
    guard_path = extract_guard_path(grid)
    
    valid_obstructions = 0
    for obstruction_pos in guard_path:
        if simulate_guard_with_obstruction(grid, obstruction_pos, max_steps):
            valid_obstructions += 1
    
    return valid_obstructions



filename = 'input.txt'
grid = read_input_file(filename)

# Run the count of valid obstruction positions on the newly uploaded grid
result = count_valid_obstructions(grid, max_steps=10000)
print(result)
# answer is 1995