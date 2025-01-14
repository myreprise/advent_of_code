def parse_data(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    return [int(l.strip()) for l in lines]

def count_combinations(containers, target):
    combinations = 0
    for i in range(1, 2**len(containers)):
        total = 0
        for j in range(len(containers)):
            if i & (1 << j):
                total += containers[j]
        if total == target:
            combinations += 1
    return combinations

filename = 'input.txt'
container_sizes = parse_data(filename)
target = 150

result = count_combinations(containers=container_sizes, target=target)
print(result)
# answer is 1638