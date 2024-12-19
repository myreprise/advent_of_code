# Directly provided input as string
towel_patterns = ["r", "wr", "b", "g", "bwu", "rb", "gb", "br"]
designs = [
    "brwrr",
    "bggr",
    "gbbr",
    "rrbgbr",
    "ubwu",
    "bwurrg",
    "brgr",
    "bbrgwb"
]

# Function to count possible designs
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
            possible_count += 1
    
    return possible_count

# Print out inputs
print(towel_patterns)
print(designs)

# Calculate the number of possible designs
possible_designs_count = count_possible_designs(towel_patterns, designs)
print(possible_designs_count)  # Should output 6
