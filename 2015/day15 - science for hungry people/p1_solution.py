from itertools import product


def parse_input(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    return [line.strip() for line in lines]

def parse_ingredient_data(ingredient_lines):
    ingredients = {}
    for line in ingredient_lines:
        parts = line.split(": ")
        name = parts[0]
        properties = {}
        for prop in parts[1].split(", "):
            prop_name, value = prop.split(" ")
            properties[prop_name] = int(value)
        ingredients[name] = properties
    return ingredients


def calculate_score(ingredients, combination):
    # Initialize totals for each property
    capacity, durability, flavor, texture = 0, 0, 0, 0

    # Sum properties based on combination
    for i, ingredient in enumerate(ingredients):
        qty = combination[i]
        capacity += ingredients[ingredient]["capacity"] * qty
        durability += ingredients[ingredient]["durability"] * qty
        flavor += ingredients[ingredient]["flavor"] * qty
        texture += ingredients[ingredient]["texture"] * qty
    
    # Apply constraints (negative totals become zero)
    capacity = max(0, capacity)
    durability = max(0, durability)
    flavor = max(0, flavor)
    texture = max(0, texture)

    # Calculate total score
    return capacity * durability * flavor * texture


def find_best_cookie_score(ingredients, quantities, total, idx, current_combination):
    if idx == len(quantities) - 1:
        # Assign remaining quantity to the last ingredient
        current_combination[idx] = total
        score = calculate_score(ingredients, current_combination)
        return score

    max_score = 0
    for qty in range(total + 1):
        current_combination[idx] = qty
        max_score = max(max_score, find_best_cookie_score(ingredients, quantities, total - qty, idx + 1, current_combination))
    
    return max_score

def calculate(ingredients):
    quantities = [0] * len(ingredients)  # Initialize quantities for each ingredient
    total = 100  # total teaspoons
    return find_best_cookie_score(ingredients, quantities, total, 0, quantities)


filename = 'input.txt'
ingredient_lines = parse_input(filename)
ingredients = parse_ingredient_data(ingredient_lines)

result = calculate(ingredients)
print(result)
# answer is 13882464