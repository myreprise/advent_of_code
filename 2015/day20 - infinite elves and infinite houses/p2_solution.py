
def parse_input(filename):
    with open(filename, 'r') as f:
        line = f.read()
    return int(line)


def find_min_house_part2(target_presents):
    """Find the smallest house number that gets at least target_presents, considering the new rules."""
    max_house = target_presents // 11  # Reasonable upper bound
    presents = [0] * (max_house + 1)  # Array to store presents per house

    for elf in range(1, max_house + 1):
        # Each elf delivers to at most 50 houses
        for house in range(elf, min(max_house + 1, elf * 50 + 1), elf):
            presents[house] += 11 * elf

    # Find the smallest house meeting the target
    for house, total in enumerate(presents):
        if total >= target_presents:
            return house


# Input
target_presents = parse_input(filename='input.txt')

# Find the result for Part 2
result = find_min_house_part2(target_presents)
print(result)
# answer is 831600
