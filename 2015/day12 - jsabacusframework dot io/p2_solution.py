import json

def sum_numbers_exclude_red(data):
    if isinstance(data, int):  # Base case: single number
        return data
    elif isinstance(data, list):  # If its a list, sum the elements
        return sum(sum_numbers_exclude_red(item) for item in data)
    elif isinstance(data, dict):  # If its a dict, sum all the values
        if "red" in data.values():
            return 0
        return sum(sum_numbers_exclude_red(value) for value in data.values())
    else:
        return 0  # Ignore other types

def parse_input(filename):
    with open(filename, 'r') as file:
        json_input = file.read()
    return '[' + json_input + ']'

filename = 'input.txt'

data = parse_input(filename)
parsed_data = json.loads(data)

result = sum_numbers_exclude_red(parsed_data)
print(result)
# answer is 68466
