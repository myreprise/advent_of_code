
def parse_data(filename):
	"""
	Read input data and export as array of text
	"""
	with open(filename, 'r') as file:
		lines = file.readlines()
	
	file.close()
	return [line.strip() for line in lines]


def extract_first_last_digits(text):
	"""
	Extract first and last digits of string value
	"""
	first_digit = None
	last_digit = None

	for char in text:
		if char.isdigit():
			if first_digit is None:
				first_digit = char  # Set first digit
			last_digit = char  # Update last digit
	
	return first_digit, last_digit


def calculate_calibration_value(text_list):
	"""
	Calculate calibration value per prompt
	"""
	total = 0
	for text in text_list:
		first, last = extract_first_last_digits(text)

		if first is not None and last is not None:
			calibration_value = int(first + last)
			total += calibration_value
		
	return total


filename = 'input.txt'
text_list = parse_data(filename)

result = calculate_calibration_value(text_list=text_list)
print(result)
# answer is 55017