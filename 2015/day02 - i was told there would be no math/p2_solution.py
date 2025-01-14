
def parse_dimensions(filename):
    with open(filename, 'r') as file:
        lines = file.read().strip().split("\n")  # split into lines
    
    dimensions = [tuple(map(int, line.split("x"))) for line in lines]
    return dimensions

def get_dimensions(data):
    return [tuple(map(int, line.split('x'))) for line in data]

def calculate_ribbon(l, w, h):
    # find the smallest perimeter of any side
    perimeters = [2 * (l + w), 2 * (w + h), 2 * (h + l)]
    smallest_perimeter = min(perimeters)

    # volume of the present
    volume = l * w * h

    # total ribbon required
    return smallest_perimeter + volume

def total_ribbon(dimensions_list):
    total = 0
    for dimensions in dimensions_list:
        l, w, h = dimensions
        total += calculate_ribbon(l, w, h)
    return total


filename = 'input.txt'
dimensions_list = parse_dimensions(filename)
result = total_ribbon(dimensions_list=dimensions_list)
print(result)
# answer is 3783758