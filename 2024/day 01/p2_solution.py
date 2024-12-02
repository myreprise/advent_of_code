from collections import Counter

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

# calculate how often each number from the left list appears in the right
right_counter = Counter(right_list)


similarity_score = 0
	
for number in left_list:

	# get the frequency of the current number in the right list
	frequency = right_counter.get(number, 0)

	# update the similarity score
	similarity_score += number * frequency

print("Similarity score:", similarity_score)

