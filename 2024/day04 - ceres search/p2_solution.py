# Updated approach: search for 'A', then check for 2 M's and 2 S's in diagonals

def count_xmas_pattern(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    # Helper function to check for 2 M's and 2 S's around 'A' in diagonals
    def check_xmas(x, y):

        upper_left = grid[i-1][j+1]
        lower_left = grid[i-1][j-1]
        upper_right = grid[i+1][j+1]
        lower_right = grid[i+1][j-1]

        code = upper_left + lower_right + upper_right + lower_left
        configurations = ['MSMS','SMSM','SMMS','MSSM']
        if code in configurations:
            return True

        return False

    # Iterate through the grid and check for the X-MAS pattern
    for i in range(1, rows):  # Start at 1 and stop at rows-1 to prevent out-of-bounds for diagonals
        for j in range(1, cols):  # Same for columns
            if grid[i][j] == 'A':  # Look for 'A' and check diagonals for the pattern
                try:
                    if check_xmas(i, j):
                        count += 1
                except:
                    pass
    return count

with open('input.txt', 'r') as file:
    grid = file.read().splitlines()

# Apply the function to the test grid and print the result
result = count_xmas_pattern(grid)
print(result)
# answer is 1950
