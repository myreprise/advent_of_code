import itertools

# Function to read the grid from a text file
def read_grid_from_file(file_path):
    with open(file_path, 'r') as file:
        # Read each line and remove trailing newline characters
        map_grid = [line.strip() for line in file.readlines()]
    return map_grid


def is_collinear(x1, y1, x2, y2, x3, y3):
    return abs((y2 - y1) * (x3 - x1) - (y3 - y1) * (x2 - x1)) < 1e-10

def find_antinodes(grid):
  antennas = {}
  for y in range(len(grid)):
    for x in range(len(grid[0])):
      if grid[y][x] != '.':
        antennas.setdefault(grid[y][x], []).append((x, y))
  
  antinodes = set()
  
  for freq, locations in antennas.items():      
      for (x1, y1), (x2, y2) in itertools.combinations(locations, 2):
        for y in range(len(grid)):
          for x in range(len(grid[0])):
            if (x, y) == (x1, y1) or (x, y) == (x2, y2):
              continue
                    
            if is_collinear(x1, y1, x2, y2, x, y):
              antinodes.add((x, y))
              
          if len(locations) > 1:
            antinodes.update([(x1, y1), (x2, y2)])
  
  return len(antinodes)

# Example usage:
file_path = 'input.txt'  # Replace with your actual file path
map_grid = read_grid_from_file(file_path)

# Calculate and print the number of unique antinode locations
result = find_antinodes(map_grid)
print(result)  # The expected output should be the count of unique antinode locations
# answer is 949