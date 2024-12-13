
def parse_dimensions(filename):
    with open(filename, 'r') as file:
        lines = file.read().strip().split("\n")  # split into lines
    
    dimensions = [tuple(map(int, line.split("x"))) for line in lines]
    return dimensions

def parse_input(filename):
    with open(filename, 'r') as file:
        data = file.readlines()
    
    return [line.strip() for line in data]

def get_dimensions(data):
    return [tuple(map(int, line.split('x'))) for line in data]

def calculate_wrapping_paper(l, w, h):
    # Surface area of the box
    surface_area = 2 * (l * w + w * h + h * l)
    
    # Slack (the area of the smallest side)
    slack = min(l * w, w * h, h * l)
    
    # Total wrapping paper needed for the present
    return surface_area + slack





def total_wrapping_paper(dimensions_list):
    total = 0
    for dimensions in dimensions_list:
        l, w, h = dimensions
        total += calculate_wrapping_paper(l, w, h)
    return total


filename = 'input.txt'
dimensions_list = parse_dimensions(filename)
result = total_wrapping_paper(dimensions_list=dimensions_list)
print(result)
# answer is 1588178