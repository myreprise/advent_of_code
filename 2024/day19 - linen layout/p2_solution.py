import numpy as np

def parse_input(filename):
    with open(filename, 'r') as file:
        data = file.read()

    # parse towel patterns
    towel_patterns, designs = data.split("\n\n")
    towel_patterns = np.sort(towel_patterns.split(', '))

    # parse designs
    designs = np.sort(designs.split('\n'))
    designs = [d for d in designs if len(d) > 0]

    return towel_patterns, designs


def count_all_arrangements(towel_patterns, designs):
    # Convert towel patterns to a set for fast lookup
    patterns = set(towel_patterns)

    def count_ways_to_construct(design):
        n = len(design)
        dp = [0] * (n + 1)
        dp[0] = 1  # Base case: there's 1 way to construct an empty design

        for i in range(1, n + 1):
            for j in range(i):
                if design[j:i] in patterns:
                    dp[i] += dp[j]
        
        return dp[n]

    # total arrangements for each design
    total_arrangements = 0
    for design in designs:
        total_arrangements += count_ways_to_construct(design)
    
    return total_arrangements



filename = "input.txt"

towel_patterns, designs = parse_input(filename)
#print(towel_patterns)
#print(designs)

result = count_all_arrangements(towel_patterns=towel_patterns, designs=designs)
print(result)
# answer is 601201576113503