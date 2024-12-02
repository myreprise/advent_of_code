import re

word_to_digit = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}


# initiatize total sum to 0
total_sum = 0

# load the data
with open('input.txt', 'r') as file:

	# loop through each line
	for line in file:
		line = line.strip().lower()

		first_digit = None
		last_digit = None

		"""
		This finds all occurrences of either spelled-out numbers (one, two, etc.) or numeric digits (\d).
		\b ensures we match complete words to avoid partial matches.
		"""

		#tokens = re.findall(r'\bone|two|three|four|five|six|seven|eight|nine|\d', line)
		tokens = re.findall(r'(?:one|two|three|four|five|six|seven|eight|nine|\d)', line)
		#tokens = re.findall(r'one|two|three|four|five|six|seven|eight|nine|\d', line)

		for token in tokens:
			if token in word_to_digit:
				token = word_to_digit[token]

			if first_digit is None:
				first_digit = token

			last_digit = token

		if first_digit is not None and last_digit is not None:
			calibration_value = int(first_digit + last_digit)
			total_sum += calibration_value

		print(line, tokens, first_digit, last_digit)


print(total_sum)



