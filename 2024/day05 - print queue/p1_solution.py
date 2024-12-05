
def parse_input(input_text):
    """
    Parse the input into ordering rules and updates
    """

    sections = input_text.strip().split("\n\n")

    # parse the ordering rules
    ordering_rules = [tuple(map(int, line.split("|"))) for line in sections[0].splitlines()]

    # parse updates
    updates = [list(map(int, line.split(","))) for line in sections[1].splitlines()]
    return ordering_rules, updates


def is_update_valid(update, rules):
    """
    Check if a given update is valid based on the ordering rules
    """

    for x, y in rules:
        # if both x and y are in the update, ensure x is before y
        if x in update and y in update:
            if update.index(x) > update.index(y):
                return False
    return True


def find_middle_page(update):
    """
    Find the middle page of an update (of a valid update only)
    """
    return update[len(update) // 2]


filename = 'input.txt'

with open(filename, 'r') as file:
    input_text = file.read()

ordering_rules, updates = parse_input(input_text)
valid_middle_sum = 0

# check each update
for update in updates:
    if is_update_valid(update, ordering_rules):
        valid_middle_sum += find_middle_page(update)

print(valid_middle_sum)
# answer is 7024
