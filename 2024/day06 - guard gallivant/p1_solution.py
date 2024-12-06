def read_input_file(file_path):
    """
    Reads the input file and converts it into a 2D grid.
    """
    with open(file_path, 'r') as file:
        grid = [line.strip() for line in file.readlines()]
    return grid

def simulate_guard_distinct_positions(grid):
    """
    Simulates the guard's movement and counts how many distinct positions the guard visits
    before leaving the grid.
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
    
    # Raise an error if no initial position is found
    if guard_pos is None or guard_dir is None:
        raise ValueError("No guard starting position (e.g., '^', 'v', '<', '>') found in the grid.")
    
    rows, cols = len(grid), len(grid[0])
    visited_positions = set()
    
    while True:
        visited_positions.add(guard_pos)
        
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
    
    return len(visited_positions)


filename = 'input.txt'
grid = read_input_file(filename)

result = simulate_guard_distinct_positions(grid)
print(result)
# answer is 4890