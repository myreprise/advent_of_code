
left_list = []
right_list = []

filename = "input.txt"

# import the data, separate list values to left and right lists

with open(filename, 'r') as file:
	for line in file:
		line = line.strip()
		left, right = line.split()
		left_list.append(int(left))
		right_list.append(int(right))


# sort the lists
sorted_left = sorted(left_list)
sorted_right = sorted(right_list)


# pairing the values
total_distance = 0

for left, right in zip(sorted_left, sorted_right):
	distance = abs(left - right)
	total_distance += distance

print(total_distance)
# answer is 2285373
