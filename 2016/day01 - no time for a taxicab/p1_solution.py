
def parse_input(filename):
    with open(filename) as f:
        data = f.read()
    return data

def compute_distance(instructions_str):
    # Split the input string into individual instructions
    instructions = instructions_str.split(", ")

    # Starting position (x, y) and facing direction index (0: North)
    x, y = 0, 0
    direction_index = 0  # 0: North, 1: East, 2: South, 3: West

    # Define movement vectors for the four cardinal directions
    directions = [
        (0, 1),   # North
        (1, 0),   # East
        (0, -1),  # South
        (-1, 0)   # West
    ]

    # Process each instruction
    for instruction in instructions:
        turn = instruction[0]      # 'L' or 'R'
        blocks = int(instruction[1:])  # the number of blocks to move

        # Update the direction index based on the turn
        if turn == "R":
            direction_index = (direction_index + 1) % 4
        elif turn == "L":
            direction_index = (direction_index - 1) % 4
        else:
            raise ValueError("Invalid turn direction provided: " + turn)

        # Get the movement vector for the current direction
        dx, dy = directions[direction_index]
        # Update position
        x += dx * blocks
        y += dy * blocks

    # Calculate Manhattan distance
    distance = abs(x) + abs(y)
    return distance

filename = 'input.txt'
instructions = parse_input(filename)
result = compute_distance(instructions)
print(result)
# answer is 146