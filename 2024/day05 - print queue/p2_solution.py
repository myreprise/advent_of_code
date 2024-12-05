from collections import defaultdict, deque

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

def topological_sort(subset_pages, rules):
    """
    Perform a topological sort on the subset of pages based on ordering rules
    """

    # build a graph from the subset of pages and rules
    graph = defaultdict(list)
    in_degree = defaultdict(int)

    for x, y in rules:
        if x in subset_pages and y in subset_pages:
            graph[x].append(y)
            in_degree[y] += 1
            in_degree[x] += 0 # ensures all the nodes are in the in-degree map

    # collect nodes with zero in-degree
    zero_in_degree = deque([node for node in subset_pages if in_degree[node] == 0])
    sorted_pages = []

    while zero_in_degree:
        current = zero_in_degree.popleft()
        sorted_pages.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                zero_in_degree.append(neighbor)

    return sorted_pages


filename = 'input.txt'

with open(filename, 'r') as file:
    input_text = file.read()

ordering_rules, updates = parse_input(input_text)
reordered_middle_sum = 0

for update in updates:
    if not is_update_valid(update, ordering_rules):

        # reorder the update using topological sort
        sorted_update = topological_sort(set(update), ordering_rules)

        # add the middle page of the sorted update to the sum
        reordered_middle_sum += find_middle_page(sorted_update)

print(reordered_middle_sum)
# answer is 4151
