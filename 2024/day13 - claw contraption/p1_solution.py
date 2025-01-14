import re

def import_data(filename):

    with open(filename, 'r') as file:
        data = file.read()
    
    return data

def parse_data(content):
    machines = []

    # Regex pattern to match the block, extract values for Button A/B and Prize
    pattern = r"Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)"

    matches = re.findall(pattern, content)

    for match in matches:
        ax, ay, bx, by, px, py = map(int, match)
        machines.append((ax, ay, bx, by, px, py))
    
    return machines


def find_min_cost(machinese):
    prizes_won = 0
    total_cost = 0

    for machine in machines:
        ax, ay, bx, by, px, py = machine
        min_cost = float('inf')
        prize_won = False

        for a in range(101):
            for b in range(101):
                if a * ax + b * bx == px and a * ay + b * by == py:
                    cost = 3 * a + 1 * b
                    if cost < min_cost:
                        min_cost = cost
                        prize_won = True
                        print(f"Prize won @ cost of", min_cost)
        
        if prize_won:
            prizes_won += 1
            total_cost += min_cost
        
    return prizes_won, total_cost

filename = 'input.txt'
content = import_data(filename=filename)

machines = parse_data(content)
print(machines)

prizes, cost = find_min_cost(machines)
print(f"You can win {prizes} prizes at a cost of {cost}")
print(cost)
# answer is 35729