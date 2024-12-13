
def parse_input(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    return [line.strip() for line in lines]

def is_nice_string(s):
    # condition 1: at least three vowels
    vowels = set("aeiou")
    vowel_count = sum(1 for char in s if char in vowels)
    if vowel_count < 3:
        return False

    # condition 2: at least one double letter
    has_double_letter = any(s[i] == s[i + 1] for i in range(len(s) - 1))
    if not has_double_letter:
        return False

    # condition 3: does not contain disallowed substrings
    disallowed = ["ab", "cd", "pq", "xy"]
    contains_disallowed = any(bad in s for bad in disallowed)
    if contains_disallowed:
        return False

    # return True if all conditions are met
    return True

def count_nice_strings(strings):
    return sum(1 for s in strings if is_nice_string(s))


filename = 'input.txt'
strings = parse_input(filename)
result = count_nice_strings(strings)
print(result)
# answer is 236
