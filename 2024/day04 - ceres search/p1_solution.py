# Now let's apply the word search function to the grid we just loaded.

def count_xmas_occurrences(grid):
    rows = len(grid)
    cols = len(grid[0])
    target = "XMAS"
    target_len = len(target)
    count = 0

    # Helper function to check if a word can be formed starting from a position in a direction
    def check_word(x, y, dx, dy):
        # Check if the word "XMAS" fits in the grid starting at (x, y) in direction (dx, dy)
        for i in range(target_len):
            nx, ny = x + i * dx, y + i * dy
            if not (0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == target[i]):
                return False
        return True

    # Iterate through every cell and check all directions
    for i in range(rows):
        for j in range(cols):
            # Horizontal (left to right)
            if check_word(i, j, 0, 1):
                count += 1
            # Horizontal (right to left)
            if check_word(i, j, 0, -1):
                count += 1
            # Vertical (top to bottom)
            if check_word(i, j, 1, 0):
                count += 1
            # Vertical (bottom to top)
            if check_word(i, j, -1, 0):
                count += 1
            # Diagonal (top-left to bottom-right)
            if check_word(i, j, 1, 1):
                count += 1
            # Diagonal (bottom-right to top-left)
            if check_word(i, j, -1, -1):
                count += 1
            # Diagonal (top-right to bottom-left)
            if check_word(i, j, 1, -1):
                count += 1
            # Diagonal (bottom-left to top-right)
            if check_word(i, j, -1, 1):
                count += 1

    return count


with open('input.txt', 'r') as file:
    grid = file.read().splitlines()

# Applying the function to the grid
result = count_xmas_occurrences(grid)
print(result)
# answer is 2593
