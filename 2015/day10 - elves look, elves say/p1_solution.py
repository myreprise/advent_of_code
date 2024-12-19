
def parse_input(filename):
    with open(filename, 'r') as file:
        lines = file.read().strip()
    return lines


def look_and_say(sequence, iterations):
    for _ in range(iterations):
        next_sequence = []
        count = 1
        for i in range(1, len(sequence)):
            if sequence[i] == sequence[i - 1]:
                count += 1
            else:
                next_sequence.append(f"{count}{sequence[i - 1]}")
                count = 1
        # Append the last group
        next_sequence.append(f"{count}{sequence[-1]}")
        sequence = "".join(next_sequence)
    return len(sequence)

filename = 'input.txt'
sequence = parse_input(filename)
iterations = 40
result = look_and_say(sequence=sequence, iterations=iterations)
print(result)
# answer is 329356