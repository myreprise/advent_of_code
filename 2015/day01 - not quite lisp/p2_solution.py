
def parse_input(filename):
    with open(filename, 'r') as file:
        data = file.read()
    
    return data

def find_position_to_basement(instructions):
    floor = 0
    for i, char in enumerate(instructions, start = 1):  # Start at position 1
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1
        if floor == -1:
            return i  # Returns the position
    return None


filename = 'input.txt'
instructions = parse_input(filename)
result = find_position_to_basement(instructions=instructions)
print(result)
# answer is 1771