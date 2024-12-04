


def is_safe(report):
    """
    Determine if a single report is safe based on the given criteria.
    """

    differences = [report[i+1] - report[i] for i in range(len(report) - 1)]

    all_increasing = all(1 <= diff <=3 for diff in differences)
    all_decreasing = all(-3 <= diff <= -1 for diff in differences)

    return all_increasing or all_decreasing


def is_safe_dampener(report):
	if is_safe(report):
		return True

	for i in range(len(report)):
		modified_report = report[:i] + report[i+1:]
		if is_safe(modified_report):
			return True

	return False


safe_count = 0

with open("input.txt", "r") as file:
	for line in file:
		line = line.strip()

		report = list(map(int, line.split()))

		if is_safe_dampener(report):
			safe_count += 1

print(safe_count)

# answer is 601