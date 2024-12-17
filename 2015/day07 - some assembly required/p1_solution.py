
def import_data(filename):
    with open(filename, 'r') as file:
        lines = file.read()

    return lines


def parse_instructions(instructions):
    """
    Parse the circuit instructions into a dictionary
    """

    circuit = {}
    for line in instructions.splitlines():
        expression, wire = line.split(" -> ")
        circuit[wire] = expression
    return circuit


def evaluate(wire, circuit, cache):
    """
    Recursively evaluate the value of a wire
    """
    if wire.isdigit():
        return int(wire)  # Direct numeric value

    if wire in cache:
        return cache[wire]  # Cached value to avoid recomputation

    if wire not in circuit:
        raise ValueError(f"Wire '{wire}' is not defined in the circuit.")  # Handle undefined wire

    expression = circuit[wire]
    if expression.isdigit():
        value = int(expression)
    elif "AND" in expression:
        x, y = expression.split(" AND ")
        value = evaluate(x, circuit, cache) & evaluate(y, circuit, cache)
    elif "OR" in expression:
        x, y = expression.split(" OR ")
        value = evaluate(x, circuit, cache) | evaluate(y, circuit, cache)
    elif "LSHIFT" in expression:
        x, n = expression.split(" LSHIFT ")
        value = evaluate(x, circuit, cache) << int(n)
    elif "RSHIFT" in expression:
        x, n = expression.split(" RSHIFT ")
        value = evaluate(x, circuit, cache) >> int(n)
    elif "NOT" in expression:
        x = expression.split("NOT ")[1]
        value = ~evaluate(x, circuit, cache) & 0xFFFF  # Ensure 16-bit result
    else:
        value = evaluate(expression, circuit, cache)  # Single wire
    
    cache[wire] = value

    return value


def find_signal(instructions, target_wire):
    """
    Main function to find the signal
    """
    circuit = parse_instructions(instructions=instructions)
    cache = {}  # Cache to store computed wire values
    return evaluate(target_wire, circuit, cache)


def compute_all_wires(instructions):
    """
    Parse instruction into a circuit dictionary
    """
    circuit = parse_instructions(instructions)
    cache = {}

    # Evaluate all wires and store values
    all_values = {}
    for wire in circuit.keys():
        all_values[wire] = evaluate(wire, circuit, cache)
    
    return all_values


filename = 'input.txt'
instructions = import_data(filename)

#result = compute_all_wires(instructions=instructions)
result = find_signal(instructions, "a")
print(result)
# answer is 16076