import itertools

def parse_data(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    return lines

def parse_happiness_data(happiness_lines):
    happiness = {}
    for line in happiness_lines:
        parts = line.split()
        person1 = parts[0]
        person2 = parts[-1][:-1]  # Remove the period
        happiness_change = int(parts[3]) if parts[2] == "gain" else -int(parts[3])
        happiness[(person1, person2)] = happiness_change
    return happiness


def calculate_total_happiness(arrangement, happiness):
    total_happiness = 0
    n = len(arrangement)
    for i in range(n):
        person1 = arrangement[i]
        person2 = arrangement[(i + 1) % n]  # Circular table
        total_happiness += happiness.get((person1, person2), 0)
        total_happiness += happiness.get((person2, person1), 0)

    return total_happiness

def find_optimal_seating(happiness):
    guests = set(person for pair in happiness.keys() for person in pair)
    max_happiness = float('-inf')
    for arrangement in itertools.permutations(guests):
        total_happiness = calculate_total_happiness(arrangement, happiness)
        max_happiness = max(max_happiness, total_happiness)
    return max_happiness

filename = 'input.txt'
happiness_lines = parse_data(filename)
#print(happiness_lines)

happiness = parse_happiness_data(happiness_lines=happiness_lines)

result = find_optimal_seating(happiness)
print(result)
# answer is 664
