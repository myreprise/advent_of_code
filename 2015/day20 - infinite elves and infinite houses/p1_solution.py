

def parse_input(filename):
    with open(filename, 'r') as f:
        line = f.read()
    return int(line)


def sum_of_divisors(n):
    """Calculate the sum of divisors of a number n."""
    total = 0
    sqrt_n = int(n**0.5)
    for i in range(1, sqrt_n + 1):
        if n % i == 0:
            total += i  # Add the divisor
            if i != n // i:  # Add the complement divisor if it's different
                total += n // i
    return total


def find_min_house(target_presents):
    """Find the smallest house number that gets at least target_presents."""
    house = 1
    while True:
        # Calculate the total presents for the current house
        total_presents = 10 * sum_of_divisors(house)
        if total_presents >= target_presents:
            return house
        house += 1


target_presents = parse_input(filename='input.txt')

# Find the result
min_house = find_min_house(target_presents)
print(f"The smallest house number is {min_house}")
# answer is 786240