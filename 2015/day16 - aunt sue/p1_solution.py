import re

def parse_data(filename):
    with open(filename, 'r') as file:
        lines = file.read()
    return lines


def parse_aunt_sue_data(text):

    aunt_sue_list = []
    pattern = re.compile(r"Sue (\d+): (.+)")

    compounds = {}
    for line in text.splitlines():
        match = pattern.match(line)
        if match:
            sue_number = int(match.group(1))
            attributes = match.group(2).split(', ')
            attribute_dict = {}
            for attr in attributes:
                name, value = attr.split(': ')
                attribute_dict[name] = int(value)
            aunt_sue_list.append((sue_number, attribute_dict))

    return aunt_sue_list


def parse_mfcsam_data(mfcsam_data):
    compounds = {}
    for line in mfcsam_data.splitlines():
        name, value = line.split(': ')
        compounds[name] = int(value)
    return compounds


def find_aunt(sue_data, mfcsam_data):
    for s in sue_data:
        matches = 0
        for item in s[1].items():
            key = item[0]
            val = item[1]
            if mfcsam_data[key] == val:
                matches += 1
            if matches == 3:
                return s[0]
    return None

# MFCSAM output
mfcsam_data = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1
}

filename = 'input.txt'
text = parse_data(filename)
sue_data = parse_aunt_sue_data(text)
result = find_aunt(sue_data, mfcsam_data)

print(result)
# answer is 103
