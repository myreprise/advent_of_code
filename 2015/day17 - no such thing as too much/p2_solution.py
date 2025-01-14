def parse_data(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    return [int(l.strip()) for l in lines]

def min_containers_and_ways(container_sizes, target):
    # dp[i] will store the minimum number of containers to achieve i liters
    dp = [float('inf')] * (target + 1)
    dp[0] = 0  # 0 liters requires 0 containers
    
    # dp[i] will store the minimum number of containers to achieve i liters
    dp = [float('inf')] * (target + 1)
    dp[0] = 0  # 0 liters requires 0 containers
    
    # count[i] will store the number of ways to achieve i liters using the minimum number of containers
    count = [0] * (target + 1)
    count[0] = 1  # There's one way to store 0 liters: using no containers
    
    # Dynamic programming to calculate minimum containers and ways to achieve each target
    for size in container_sizes:
        for i in range(target, size - 1, -1):  # Loop from target to size to avoid overwriting
            # If using the current container size gives us fewer containers, update dp and count
            if dp[i - size] + 1 < dp[i]:
                dp[i] = dp[i - size] + 1
                count[i] = count[i - size]  # Reset the count to the ways we achieve i - size liters
            elif dp[i - size] + 1 == dp[i]:
                count[i] += count[i - size]  # Add the ways to achieve i - size liters
    
    return dp[target], count[target]


filename = 'input.txt'
container_sizes = parse_data(filename)
target = 150

min_containers, ways = min_containers_and_ways(container_sizes, target)
print(ways)
# answer is 17