

def get_code(row, column):
    # Calculate the diagonal index
    diagonal = row + column - 1
    position = (diagonal * (diagonal - 1)) // 2 + column

    # Start with the first code
    code = 20151125
    for _ in range(1, position):
        code = (code * 252533) % 33554393
    
    return code

# Puzzle input
puzzle_row, puzzle_column = 3010, 3019
print(f"Code at ({puzzle_row}, {puzzle_column}): {get_code(puzzle_row, puzzle_column)}")
# answer is 8997277