
import re

def get_input(input):
	with open('input.txt', 'r') as file:
		data = file.read()

	return data


def process_memory(memory):

	# Regular expression to match valid mul(X,Y) where X and Y are integers
	# Allows any non-numeric characters inside the parentheses but not between the digits.
	pattern = r'mul\((\d+),(\d+)\)'

	# Find all matches in the memory string
	matches = re.findall(pattern, memory)

	# Calculate the sum of the multiplication
	total_sum = 0
	for match in matches:
		# Extract numbers from the match
		x, y = int(match[0]), int(match[1])

		# Perform multiplication and add to the total sum
		total_sum += x * y

	return total_sum

filename = 'input.txt'

#memory = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'
memory = get_input(filename)
result = process_memory(memory)
print(result)
# answer is 183669043
