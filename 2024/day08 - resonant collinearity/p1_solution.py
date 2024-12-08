import itertools

# Function to read the grid from a text file
def read_grid_from_file(file_path):
    with open(file_path, 'r') as file:
        # Read each line and remove trailing newline characters
        map_grid = [line.strip() for line in file.readlines()]
    return map_grid


def find_antinodes(grid):
    # Get map dimensions
    rows = len(grid)
    cols = len(grid[0])
    
    # Step 1: Store the coordinates of antennas for each frequency
    antennas = {}
    for r in range(rows):
        for c in range(cols):
            char = grid[r][c]
            if char != '.':
                if char not in antennas:
                    antennas[char] = []
                antennas[char].append((r, c))
    
    # Function to check if an antinode is within bounds
    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols
    
    # Find all the antinode locations
    antinodes = set()
    
    # For each frequency, compare every pair of antennas
    for freq, locations in antennas.items():
        for (x1, y1), (x2, y2) in itertools.combinations(locations, 2):
            dx, dy = x2 - x1, y2 - y1

            antinode1 = (x1 + 2*dx, y1 + 2*dy)
            antinode2 = (x1 - dx, y1 - dy)

            for ax, ay in [antinode1, antinode2]:
                if (0 <= ax < len(grid[0]) and 0 <= ay < len(grid)):
                    antinodes.add((int(ax), int(ay)))

    return len(antinodes)

# Example usage:
file_path = 'input.txt'  # Replace with your actual file path
map_grid = read_grid_from_file(file_path)

# Calculate and print the number of unique antinode locations
result = find_antinodes(map_grid)
print(result)  # The expected output should be the count of unique antinode locations
# answer is 269