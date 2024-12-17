
def import_data(filename):
    with open(filename, 'r') as file:
        lines = file.read().splitlines()

    # Separate the map and the movement instructions
    warehouse_map = []
    instructions = []
    parsing_instructions = False

    for line in lines:
        if line.strip() == '':
            parsing_instructions = True
        elif parsing_instructions:
            instructions.append(line.strip())
        else:
            warehouse_map.append(line)

    # Combine the instruction lines into one continuous string

    instructions = ''.join(instructions)
    instructions = "".join(instructions.split())
    warehouse_map = [list(line) for line in warehouse_map]

    return warehouse_map, instructions


def parse_input(grid_str, moves_str):
    grid = [list(line) for line in grid_str.splitlines()]
    moves = "".join(moves_str.split())  # Remove newlines in the moves
    return grid, moves

def find_robot_position(grid):
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == "@":
                return row, col
    return None

def simulate_moves(grid, moves):
    rows, cols = len(grid), len(grid[0])
    directions = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}
    robot_row, robot_col = find_robot_position(grid)
    print(robot_row, robot_col)

    for move in moves:
        dr, dc = directions[move]
        next_row, next_col = robot_row + dr, robot_col + dc
        if 0 <= next_row < rows and 0 <= next_col < cols:
            if grid[next_row][next_col] == ".":  # Move to empty space
                grid[robot_row][robot_col] = "."
                grid[next_row][next_col] = "@"
                robot_row, robot_col = next_row, next_col
            elif grid[next_row][next_col] == "O":  # Try to push a box
                if can_push_chain(grid, next_row, next_col, dr, dc):  # Check if chain can move
                    push_chain(grid, next_row, next_col, dr, dc)  # Push the chain of boxes
                    grid[robot_row][robot_col] = "."
                    grid[next_row][next_col] = "@"
                    robot_row, robot_col = next_row, next_col
                else:
                    # Debug: Log when a chain of boxes cannot be pushed
                    print(f"Move {move} blocked: box chain at ({next_row}, {next_col}) cannot move")

        # Debug: Print the grid after each move
        print(f"After move {move}:")
        for line in grid:
            print("".join(line))
        print()


def can_push_chain(grid, row, col, dr, dc):
    """
    Recursively checks if a chain of boxes can be pushed in the given direction.
    """
    rows, cols = len(grid), len(grid[0])
    while 0 <= row < rows and 0 <= col < cols:
        if grid[row][col] == ".":  # Found an empty space
            return True
        elif grid[row][col] == "O":  # Continue checking the chain
            row += dr
            col += dc
        else:  # Blocked by a wall or invalid cell
            return False
    return False


def push_chain(grid, row, col, dr, dc):
    """
    Pushes a chain of boxes in the given direction.
    """
    boxes = []  # Collect all box positions in the chain
    while grid[row][col] == "O":
        boxes.append((row, col))
        row += dr
        col += dc

    # Move the boxes from back to front
    for r, c in reversed(boxes):
        grid[r + dr][c + dc] = "O"
        grid[r][c] = "."


def calculate_gps_sum(grid):
    gps_sum = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == "O":
                gps_sum += 100 * row + col
                # Debug: Log GPS of each box
                print(f"Box at ({row}, {col}): GPS = {100 * row + col}")
    return gps_sum

def lanternfish_warehouse(grid, moves):
    #grid, moves = parse_input(grid_str, moves_str)
    simulate_moves(grid, moves)
    return calculate_gps_sum(grid)



# Calculate the result

filename = 'input.txt'
warehouse_map, instructions = import_data(filename)
print(warehouse_map)
print(instructions)

result = lanternfish_warehouse(warehouse_map, instructions)
print("Sum of GPS coordinates:", result)
# answer is 1437174
