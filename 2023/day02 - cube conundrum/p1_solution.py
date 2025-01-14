
constraints = {
	"red": 12,
	"green": 13,
	"blue": 14
}


def is_game_possible(game, constraints):
	"""
	Check if a game is possible given the constraints
	"""

	check = 0
	for subset in game:
		for color, count in subset.items():
			if count > constraints[color]:
				check += 1

	if check > 0:
		return False
	return True


games = []
total = 0

with open('input.txt', 'r') as file:
	for line in file:
		line = line.strip()

		# split hte line into game id and cube sets
		game_id, subsets = line.split(": ")
		game_id = int(game_id.split(" ")[1])

		# parse the subsets
		subsets = subsets.split("; ")

		cube_sets = []
		for subset in subsets:
			cubes = {}
			for part in subset.split(", "):
				count, color = part.split(" ")
				cubes[color] = int(count)
			cube_sets.append(cubes)

			games.append((game_id, cube_sets))


game_ids = []
for game_id, cube_sets in games:
	if is_game_possible(cube_sets, constraints):
		game_ids.append(game_id)

total = sum(list(set(game_ids)))
print(total)
# answer is 3035