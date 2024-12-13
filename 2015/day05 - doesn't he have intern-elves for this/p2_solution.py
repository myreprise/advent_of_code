
def parse_input(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    return [line.strip() for line in lines]

def is_nice_string(s):
    # condition 1: contains a pair of any two letters that appear at least twice without overlap
    has_pair = any(s[i:i+2] in s[i+2:] for i in range(len(s) - 1))

    # condition 2: Contains at least one letter which repeats with exactly one letter between them
    has_repeating_letter = any(s[i] == s[i + 2] for i in range(len(s) - 2))

    return has_pair and has_repeating_letter

def count_nice_strings(strings):
    return sum(1 for s in strings if is_nice_string(s))


filename = 'input.txt'
strings = parse_input(filename)
result = count_nice_strings(strings)
print(result)
# answer is 51
