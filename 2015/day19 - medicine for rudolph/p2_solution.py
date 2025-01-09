from random import shuffle

# Initialize variables
transforms = []
molecule = ''

# Read input file
with open('input.txt', 'r') as fd:
    lines = [line.strip() for line in fd]
    for line in lines:
        if '=>' in line:
            frm, _, to = line.split()
            transforms.append((frm, to))
        elif line:  # Non-empty line, assume it's the molecule
            molecule = line

# Initialize counters
count = shuffles = 0
mol = molecule

# Main loop for reverse engineering
while len(mol) > 1:
    start = mol
    for frm, to in transforms:
        while to in mol:
            count += mol.count(to)
            mol = mol.replace(to, frm)

    # Restart the process if no progress is made
    if start == mol:
        shuffle(transforms)
        mol = molecule
        count = 0
        shuffles += 1

# Output results
print(f'{count} transforms after {shuffles} shuffles')


# answer is 207
