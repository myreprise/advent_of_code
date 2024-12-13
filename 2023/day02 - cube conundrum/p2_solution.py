
games = []

with open('input.txt', 'r') as file:
	for line in file:
		line = line.strip()

		game_id, subsets = line.split(": ")
		game_id = int(game_id.split(" ")[1])

		# parse the subsets
		subsets = subsets.split("; ")

		cube_sets = []
		for subset in subsets:
			# parse the colors
			cubes = {}
			for part in subset.split(", "):
				count, color = part.split(" ")
				cubes[color] = int(count)
			cube_sets.append(cubes)
		games.append((game_id, cube_sets))

total_power = 0

for _, cube_sets in games:
	
	min_cubes = {
		"red": 0,
		"green": 0,
		"blue": 0
	}

	for subset in cube_sets:
		for color in min_cubes.keys():
			min_cubes[color] = max(min_cubes[color], subset.get(color, 0))

	power = min_cubes["red"] * min_cubes["blue"] * min_cubes["green"]
	total_power += power

print(total_power)
# answer is 66027