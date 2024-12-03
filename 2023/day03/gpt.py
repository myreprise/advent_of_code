# Let's load the data from the uploaded file and process it to calculate the sum of part numbers.

# File path
file_path = 'input.txt'

# Read the data from the file
with open(file_path, 'r') as file:
    schematic = file.read()

# Function to parse the schematic and find part numbers based on adjacency to symbols
import re

def parse_schematic(schematic):
    """
    Parse the schematic into a list of rows.
    """
    return schematic.splitlines()

def find_numbers_and_symbols(grid):
    """
    Extract numbers and symbols from each row.
    """
    numbers = []  # List of tuples (row_index, start_index, end_index, number)
    symbols = []  # List of tuples (row_index, col_index)
    for row_index, row in enumerate(grid):
        # Find numbers using regex
        for match in re.finditer(r"\d+", row):
            start, end = match.start(), match.end()
            number = int(match.group())
            numbers.append((row_index, start, end, number))
        # Find symbols
        for col_index, char in enumerate(row):
            if char in "*#+$":  # Define symbols
                symbols.append((row_index, col_index))
    return numbers, symbols

def is_adjacent(num_row, num_start, num_end, sym_row, sym_col):
    """
    Check if a number is adjacent to a symbol.
    """
    # Check if the rows are adjacent
    if abs(num_row - sym_row) > 1:
        return False
    # Check if the symbol is within or next to the number horizontally
    return num_start - 1 <= sym_col <= num_end

def calculate_part_numbers(schematic):
    """
    Recalculate part numbers based on corrected adjacency logic.
    """
    grid = parse_schematic(schematic)
    numbers, symbols = find_numbers_and_symbols(grid)
    valid_numbers = set()

    # Check each number against all symbols with corrected logic
    for num_row, num_start, num_end, number in numbers:
        for sym_row, sym_col in symbols:
            # Ensure horizontal alignment or immediate row adjacency with alignment
            if num_row == sym_row and num_start - 1 <= sym_col <= num_end + 1:
                valid_numbers.add(number)
                break  # Found a valid adjacency
            elif abs(num_row - sym_row) == 1 and num_start <= sym_col <= num_end:
                valid_numbers.add(number)
                break  # Adjacent rows with alignment

    # Return the sum of all valid numbers
    return sum(valid_numbers)

# Calculate the result
result = calculate_part_numbers(schematic)

print(result)
