
def parse_input(filename):
    with open(filename, 'r') as file:
        data = file.read()

    return "".join([x.strip() for x in data])

def count_unique_houses(directions):
    # start at the origin
    x, y = 0, 0

    # set to track visited houses
    visited_houses = set()
    visited_houses.add((x, y))

    # iterate through the directions
    for move in directions:
        if move == '^':
            y += 1
        elif move == 'v':
            y -= 1
        elif move == '>':
            x += 1
        elif move == '<':
            x -= 1
        else:
            pass
        visited_houses.add((x, y))

    return len(visited_houses)

filename = 'input.txt'
directions = parse_input(filename)
result = count_unique_houses(directions=directions)
print(result)
# answer is 2572
