
# 1 read the input data
# 2 extract first and last digits
# 3 form the callibration value
# 4 sum up all the values


total_sum = 0

# load the data
with open('input.txt', 'r') as file:
	for line in file:
		line = line.strip()
		
		first_digit = None
		last_digit = None

		for char in line:
			if char.isdigit():
				if first_digit is None:
					first_digit = char  # Set the first digit
				last_digit = char   # Update the last digit

		if first_digit is not None and last_digit is not None:
			calibration_value = int(first_digit + last_digit)
			total_sum += calibration_value

print(total_sum)