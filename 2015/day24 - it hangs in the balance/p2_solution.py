from itertools import combinations
from math import prod

def can_divide_into_groups(packages, group_weight, num_groups):
    """Check if the packages can be divided into `num_groups` groups of `group_weight`."""
    if num_groups == 1:
        return sum(packages) == group_weight
    for r in range(1, len(packages) + 1):
        for group in combinations(packages, r):
            if sum(group) == group_weight:
                remaining = list(packages)
                for item in group:
                    remaining.remove(item)
                if can_divide_into_groups(remaining, group_weight, num_groups - 1):
                    return True
    return False

def find_optimal_group(packages, num_groups):
    total_weight = sum(packages)
    group_weight = total_weight // num_groups

    # Check if the division is possible
    if total_weight % num_groups != 0:
        raise ValueError("Packages cannot be evenly divided into groups")

    # Generate all subsets and filter those with the target weight
    valid_groups = []
    for r in range(1, len(packages) + 1):  # Fewest number of packages first
        for group in combinations(packages, r):
            if sum(group) == group_weight:
                remaining = list(packages)
                for item in group:
                    remaining.remove(item)
                if can_divide_into_groups(remaining, group_weight, num_groups - 1):
                    valid_groups.append(group)
        if valid_groups:  # Stop as soon as we find groups with the smallest size
            break

    # Calculate quantum entanglement for each valid group
    quantum_entanglements = [(prod(group), group) for group in valid_groups]
    quantum_entanglements.sort()  # Sort by QE, then by group

    # Return the smallest QE and its group
    return quantum_entanglements[0]

# Example input
example_packages = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11]

# Solve for example (4 groups)
qe, group = find_optimal_group(example_packages, num_groups=4)
print(f"Quantum Entanglement (example, 4 groups): {qe}, Group: {group}")

def read_data(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    return [int(line.strip()) for line in lines]

# Add your puzzle input here
puzzle_input = read_data('input.txt')
qe, group = find_optimal_group(puzzle_input, num_groups=4)
print(f"Quantum Entanglement (puzzle, 4 groups): {qe}, Group: {group}")
# answer is 72050269