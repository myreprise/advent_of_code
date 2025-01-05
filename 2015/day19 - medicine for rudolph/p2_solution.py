from collections import deque
from collections import defaultdict
import re

def parse_data(filename):
    with open(filename, 'r') as file:
        rules, molecules = file.read().split('\n\n')
    
    rules = parse_rules(rules)
    
    return rules, molecules


def parse_rules(rules):
    rules = rules.split("\n")
    data = []
    for rule in rules:
        pre, ant = rule.split(" => ")
        data.append((pre, ant))

    return data


def fewest_steps_to_e(replacement_rules, medicine_molecule):
    # Reverse the replacement rules
    reverse_rules = {}
    for from_molecule, to_molecule in replacement_rules:
        if to_molecule not in reverse_rules:
            reverse_rules[to_molecule] = []
        reverse_rules[to_molecule].append(from_molecule)

    # BFS setup: start from the medicine molecule and reduce to 'e'
    queue = deque([(medicine_molecule, 0)])  # (current molecule, steps taken)
    visited = set([medicine_molecule])  # Keep track of visited molecules to avoid cycles

    while queue:
        current_molecule, steps = queue.popleft()
        print(current_molecule, steps)

        # If we've reduced the molecule to 'e', return the number of steps
        if current_molecule == "e":
            return steps

        # Try applying each reverse replacement rule
        for to_molecule, from_molecules in reverse_rules.items():
            if to_molecule in current_molecule:
                for from_molecule in from_molecules:
                    # Replace 'to_molecule' with 'from_molecule' in the current molecule
                    new_molecule = current_molecule.replace(to_molecule, from_molecule, 1)

                    # To avoid revisiting the same molecule, check if it has already been visited
                    if new_molecule not in visited:
                        visited.add(new_molecule)
                        queue.append((new_molecule, steps + 1))

    return -1  # If no solution is found


def generate_next(starter, replacements):
    molecules = set()

    for i, char in enumerate(starter):
        try:
            if char in replacements:
                for replacement in replacements[char]:
                    molecules.add(starter[:i] + replacement + starter[i + 1:])
            else:
                for replacement in replacements[starter[i:i + 2]]:
                    molecules.add(starter[:i] + replacement + starter[i + 2:])
        except KeyError:
            continue

    return molecules


def generate_prev(target, replacements):
    molecules = set()

    for k, v in replacements.items():
        idx = target.find(k)
        while idx >= 0:
            for i in v:
                if i == "e":
                    continue
                try:
                    molecules.add(target[:idx] + i + target[idx + len(k):])
                except IndexError:
                    molecules.add(target[:idx] + i)
            idx = target.find(k, idx+1)

    if not molecules:
        molecules = {"e"}
    return molecules


def reverse_dict(d):
    reverse = defaultdict(list)
    for k, v in d.items():
        for i in v:
            reverse[i].append(k)
    return reverse


def read_data(filename):
    with open(filename, 'r') as file:
        data = file.read()
    return data

def parse(stream):
    replacements = defaultdict(list)
    for k, v in re.findall(r"(\w+) => (\w+)", stream):
        replacements[k].append(v)
    return replacements, stream.strip().split("\n")[-1]


def steps_to_generate(target, replacements):
    replacements = reverse_dict(replacements)
    seen = {}
    last_generation = generate_prev(target, replacements)
    n_steps = 1

    while last_generation != {"e"}:
        current_generation = set()
        molecule = min(last_generation, key=len)

        try:
            new_molecules = seen[molecule]

        except KeyError:
            new_molecules = generate_prev(molecule, replacements)
            seen[molecule] = new_molecules
        current_generation |= new_molecules
        last_generation = current_generation

        n_steps += 1

    return n_steps

filename = 'input.txt'

with open(filename, 'r') as file:
    replacements, target = parse(file.read())

result = steps_to_generate(target, replacements)
print(result)
# answer is 