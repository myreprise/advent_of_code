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


def count_possible_designs(towel_patterns, designs):
    # Convert towel patterns to a set for fast lookup
    patterns = set(towel_patterns)
    
    def can_construct_design(design):
        n = len(design)
        dp = [False] * (n + 1)
        dp[0] = True  # Base case: empty design can be constructed
        
        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and design[j:i] in patterns:
                    dp[i] = True
                    break
        return dp[n]
    
    # Count designs that can be constructed
    possible_count = 0
    for design in designs:
        if can_construct_design(design):
            #print(f'{design} is possible')
            possible_count += 1
        else:
            #print(f'NOT {design}')
            pass
    
    return possible_count


filename = "input.txt"

towel_patterns, designs = parse_input(filename)
#print(towel_patterns)
print(designs)

result = count_possible_designs(towel_patterns=towel_patterns, designs=designs)
print(result)
# answer is 226