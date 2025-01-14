def run_program(instructions, initial_a):
    # Initialize registers with a starting value for `a`
    registers = {"a": initial_a, "b": 0}
    pointer = 0  # Instruction pointer
    
    # Function to parse and execute each instruction
    while 0 <= pointer < len(instructions):
        parts = instructions[pointer].split()
        op = parts[0]
        
        if op == "hlf":
            r = parts[1]
            registers[r] //= 2
            pointer += 1
        
        elif op == "tpl":
            r = parts[1]
            registers[r] *= 3
            pointer += 1
        
        elif op == "inc":
            r = parts[1]
            registers[r] += 1
            pointer += 1
        
        elif op == "jmp":
            offset = int(parts[1])
            pointer += offset
        
        elif op == "jie":
            r = parts[1][0]  # Remove the comma
            offset = int(parts[2])
            if registers[r] % 2 == 0:
                pointer += offset
            else:
                pointer += 1
        
        elif op == "jio":
            r = parts[1][0]  # Remove the comma
            offset = int(parts[2])
            if registers[r] == 1:
                pointer += offset
            else:
                pointer += 1
    
    return registers["b"]

# Example program (repeated for demonstration)
example_program = [
    "inc a",
    "jio a, +2",
    "tpl a",
    "inc a",
]

def read_data(filename):
    with open(filename, 'r') as file:
        data = file.read()
    return data

# Parse the input
def parse_input(input_data):
    return input_data.strip().split("\n")

# Execute the example with a = 1
parsed_example = parse_input("\n".join(example_program))
result = run_program(parsed_example, initial_a=1)
print("Value in register b (example, a=1):", result)


puzzle_input = read_data('input.txt')
parsed_input = parse_input(puzzle_input)
result = run_program(parsed_input, initial_a=1)
print("Value in register b (puzzle, a=1):", result)
# answer is 231