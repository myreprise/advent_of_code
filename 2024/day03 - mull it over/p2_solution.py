import re


def get_input(input):
	with open('input.txt', 'r') as file:
		data = file.read()

	return data


def process_memory(memory):

	# Regular expression to match valid mul(X,Y) where X and Y are integers
	pattern = r'mul\((\d+),(\d+)\)'

	# Regular expressions to match do() and don't() instructions
	do_pattern = r'do\(\)'       # Matches 'do()' instructions
	dont_pattern = r"don't\(\)"  # Matches "don't()" instructions

	# Track the state of multiplication
	mul_enabled = True
	total_sum = 0

	parts = re.split(r"(do\(\)|don\'t\(\))", memory)

	for part in parts:
		if re.match(do_pattern, part):

			# Enable future mul instructions
			mul_enabled = True
		elif re.match(dont_pattern, part):

			# Disable future mul instructions
			mul_enabled = False
		else:
			# Find valid mul instructions
			matches = re.findall(pattern, part)
			for match in matches:
				if mul_enabled:
					# Extract numbers from the match
					x, y = int(match[0]), int(match[1])

					# Perform multiplication and add to the total sum
					total_sum += x * y

	return total_sum


filename = 'input.txt'
#memory = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
memory = get_input(filename)

result = process_memory(memory)
print(result)
# answer is 59097164