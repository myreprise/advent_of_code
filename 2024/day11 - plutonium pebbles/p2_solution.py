from collections import Counter

def parse_input(filename):

    with open(filename, 'r') as file:
        data = file.read()

    file.close()

    inital_stones = data.split()
    inital_stones = [int(s) for s in inital_stones]
    
    return inital_stones

def split_stone(number):
    """
    Splits the number into halves
    """

    number_str = str(number)
    mid = len(number_str) // 2
    left = int(number_str[:mid])
    right = int(number_str[mid:])
    return left, right

def transform_stones(stones):
    """
    Apply the transformation rules to a list of stones
    """

    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        elif len(str(stone)) % 2 == 0:  # Even number of digits
            left, right = split_stone(stone)
            new_stones.extend([left, right])
        else:
            new_stones.append(stone * 2024)
    
    return new_stones


def simulate_stones(initial_stones, blinks):
    """
    Simulate the evolution of stones over a given number of blinks.
    """

    stone_counts = Counter(initial_stones)

    for i in range(blinks):

        new_counts = Counter()

        for stone, count in stone_counts.items():
            if stone == 0:
                new_counts[1] += count  # Rule 1

            elif len(str(stone)) % 2 == 0:
                # Rule 2
                left, right = split_stone(stone)
                new_counts[left] += count
                new_counts[right] += count

            else:
                # Rule 3
                new_counts[stone * 2024] += count
        
        # Update stone counts for the next blink
        stone_counts = new_counts
        print(f"Blink {i+1} | Stones: {sum(stone_counts.values())}")
    
    return sum(stone_counts.values())

# parse input
filename = 'input.txt'
inital_stones = parse_input(filename)
print(inital_stones)

# simulate blinking
blinks = 75

# count the stones
result = simulate_stones(initial_stones=inital_stones, blinks=blinks)

# print result
print(result)

# answer is 240884656550923