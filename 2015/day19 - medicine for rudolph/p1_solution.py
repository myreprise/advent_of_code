import re


def parse_data(filename):
    with open(filename, 'r') as file:
        rules, molecules = file.read().split('\n\n')
    
    return rules, molecules

def parse_rules(rules):
    rules = rules.split("\n")
    data = []
    for rule in rules:
        pre, ant = rule.split(" => ")
        data.append((pre, ant))

    return data

def count_distinct_molecules(rules, molecule):
    distinct_molecules = set()

    for from_molecule, to_molecule in rules:
        for match in re.finditer(from_molecule, molecule):
            distinct_molecules.add(molecule[:match.start()] + to_molecule + molecule[match.end():])
        
    return len(distinct_molecules)

filename = 'input.txt'

rules, molecules = parse_data(filename)
rules = parse_rules(rules)

result = count_distinct_molecules(rules, molecules)
print(result)
# answer is 576