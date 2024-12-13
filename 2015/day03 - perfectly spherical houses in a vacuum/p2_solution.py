
def parse_input(filename):
    with open(filename, 'r') as file:
        data = file.read()

    return "".join([x.strip() for x in data])

def count_unique_houses_with_robo_santa(directions):
    # start at the origin
    santa_x, santa_y = 0, 0
    robo_x, robo_y = 0, 0

    # set to track visited houses
    visited_houses = set()
    visited_houses.add((0, 0))

    # iterate through the directions
    for i, move in enumerate(directions):
        if i % 2 == 0:  # Santa moves
            if move == '^':
                santa_y += 1
            elif move == 'v':
                santa_y -= 1
            elif move == '>':
                santa_x += 1
            elif move == '<':
                santa_x -= 1
            visited_houses.add((santa_x, santa_y))
        else:
            if move == '^':
                robo_y += 1
            elif move == 'v':
                robo_y -= 1
            elif move == '>':
                robo_x += 1
            elif move == '<':
                robo_x -= 1
            visited_houses.add((robo_x, robo_y))

    # Return the number of unique houses
    return len(visited_houses)

filename = 'input.txt'
directions = parse_input(filename)
result = count_unique_houses_with_robo_santa(directions=directions)
print(result)
# answer is 2631
