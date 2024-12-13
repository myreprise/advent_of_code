def import_data(filename):

    with open(filename) as file:
        scenarios = file.read().split('\n\n')
    
    file.close()
    return scenarios


def parse(scenario):
    output = {}
    a,b,prize = scenario.splitlines()
    output['A'] = [int(item.split('+')[1]) for item in a.split(':')[1].split(', ')]
    output['B'] = [int(item.split('+')[1]) for item in b.split(':')[1].split(', ')]
    output['Prize'] = [10000000000000 + int(item.split('=')[1]) for item in prize.split(':')[1].split(', ')]
    return output


def solve(scenario):
    ax, ay = scenario['A']
    bx, by = scenario['B']
    tx, ty = scenario['Prize']

    try:

        b = (tx * ay - ty * ax) // (ay * bx - by * ax)
        a = (tx * by - ty * bx) // (by * ax - bx * ay)

        if ax * a + bx * b == tx and ay * a + by * b == ty:
            return 3 * a + 1 * b
        else:
            return 0
    
    except ZeroDivisionError:
        return 0


filename = 'input.txt'
scenarios = import_data(filename=filename)

scenarios = [parse(scenario) for scenario in scenarios]

result = [solve(scenario) for scenario in scenarios]
result = sum(result)
print(result)

# answer is 88584689879723