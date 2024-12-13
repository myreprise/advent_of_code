
def parse_input(filename):
    with open(filename, 'r') as file:
        data = file.read()
    
    return data

def calculate_floor(instructions):
    floor = 0
    for char in instructions:
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1

    return floor


filename = 'input.txt'
instructions = parse_input(filename)
result = calculate_floor(instructions=instructions)
print(result)
# answer is 138