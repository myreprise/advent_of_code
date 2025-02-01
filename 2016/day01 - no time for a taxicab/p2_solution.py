
def parse_input(filename):
    with open(filename) as f:
        data = f.read()
    return data

def first_revisited_distance(instructions_str):
    # Split the input string into individual instructions.
    instructions = instructions_str.split(", ")

    # Starting position (x, y) and initial direction (0: North, 1: East, 2: South, 3: West).
    x, y = 0, 0
    direction_index = 0  # Start facing North.

    # Define movement vectors for the four cardinal directions.
    directions = [
        (0, 1),   # North
        (1, 0),   # East
        (0, -1),  # South
        (-1, 0)   # West
    ]

    # Set to keep track of visited positions. Start by marking the origin.
    visited = set()
    visited.add((x, y))

    # Process each instruction.
    for instruction in instructions:
        turn = instruction[0]         # Either 'L' or 'R'
        blocks = int(instruction[1:])   # Number of blocks to move

        # Update the direction index based on the turn.
        if turn == "R":
            direction_index = (direction_index + 1) % 4
        elif turn == "L":
            direction_index = (direction_index - 1) % 4
        else:
            raise ValueError("Invalid turn direction provided: " + turn)

        # Get the movement vector for the current direction.
        dx, dy = directions[direction_index]

        # Move one block at a time.
        for _ in range(blocks):
            x += dx
            y += dy

            # Check if the current location has been visited before.
            if (x, y) in visited:
                # Return the Manhattan distance from the origin.
                return abs(x) + abs(y)
            visited.add((x, y))

    # In case no location is visited twice.
    return None

# Test the function with the provided example.
example = "R8, R4, R4, R8"  # Expected output is 4.
print("Distance to the first revisited location:", first_revisited_distance(example))


filename = 'input.txt'
instructions = parse_input(filename)
result = first_revisited_distance(instructions)
print(result)
# answer is 131