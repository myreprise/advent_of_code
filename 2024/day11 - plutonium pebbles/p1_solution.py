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

    stones = initial_stones
    
    for i in range(blinks):
        stones = transform_stones(stones)
    
    return len(stones)





# parse input
filename = 'input.txt'
inital_stones = parse_input(filename)
print(inital_stones)

# simulate blinking
blinks = 25

# count the stones
result = simulate_stones(initial_stones=inital_stones, blinks=blinks)

# print result
print(result)

# answer is 203228