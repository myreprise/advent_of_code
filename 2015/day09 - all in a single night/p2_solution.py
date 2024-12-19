import itertools
from collections import defaultdict
import re


def parse_input(file_contents):
    distances = defaultdict(dict)

    # regex pattern
    pattern = r'(\w+) to (\w+) = (\d+)'

    # find all matches
    matches = re.findall(pattern, file_contents)

    for city1, city2, dist in matches:
        dist = int(dist)
        distances[city1][city2] = dist
        distances[city2][city1] = dist  # bidirectional distances

    return distances

def calculate_route_distance(route, distance_matrix, cities):
    total_distance = 0
    for i in range(len(route) - 1):
        city_from = route[i]
        city_to = route[i + 1]
        total_distance += distance_matrix[cities.index(city_from)][cities.index(city_to)]
    return total_distance

def longest_route_distance(distances):
    cities = list(distances.keys())

    # Build the distance matrix
    n = len(cities)
    distance_matrix = [[0] * n for _ in range(n)]

    # fill the distance matrix with the provided distances
    for i in range(n):
        for j in range(i + 1, n):
            city1 = cities[i]
            city2 = cities[j]
            distance_matrix[i][j] = distances[city1][city2]
            distance_matrix[j][i] = distances[city1][city2]

    # Generate all the permutations of cities
    max_distance = 0
    for route in itertools.permutations(cities):
        # Calculate the distance for this route
        route_distance = calculate_route_distance(route, distance_matrix, cities)
        max_distance = max(max_distance, route_distance)

    return max_distance


filename = 'input.txt'
with open(filename, 'r') as file:
    contents = file.read()

distances = parse_input(contents)

result = longest_route_distance(distances=distances)
print(result)
# answer is 117
