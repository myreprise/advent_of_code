
def parse_input(filename):
    with open(filename, 'r') as file:
        lines = file.read().strip()
    return lines


def increment_password(password):
    password = list(password)
    i = len(password) - 1
    while i >= 0:
        if password[i] == 'z':
            password[i] = 'a'
            i -= 1
        else:
            password[i] = chr(ord(password[i]) + 1)
            break
    return ''.join(password)

def contains_increasing_straight(password):
    for i in range(len(password) - 2):
        if ord(password[i]) + 1 == ord(password[i + 1]) and ord(password[i + 1]) + 1 == ord(password[i + 2]):
            return True
    return False

def does_not_contain_forbidden(password):
    return not any(char in password for char in 'iol')

def contains_two_pairs(password):
    pairs = set()
    i = 0
    while i < len(password) - 1:
        if password[i] == password[i + 1]:
            pairs.add(password[i])
            i += 2
        else:
            i += 1
    return len(pairs) >= 2

def is_valid_password(password):
    return (
        contains_increasing_straight(password) and
        does_not_contain_forbidden(password) and
        contains_two_pairs(password)
    )

def find_next_password(current_password):
    current_password = increment_password(current_password)
    while not is_valid_password(current_password):
        current_password = increment_password(current_password)
    return current_password

filename = 'input2.txt'
current_password = parse_input(filename=filename)

result = find_next_password(current_password=current_password)
print(result)
# answer is hxcaabcc
