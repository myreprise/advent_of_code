import hashlib

def parse_input(filename):
    with open(filename, 'r') as file:
        data = file.read().strip()

    return data

def find_lowest_number_with_prefix(secret_key: str, prefix: str = "000000") -> int:
    number = 1  # Start with the lowest positive number
    while True:
        # Concatenate the secret key and the current number
        combined = f"{secret_key}{number}"

        # Compute the MD5 hash of the concatenated string
        hash_result = hashlib.md5(combined.encode()).hexdigest()

        # Check if the hash starts with the given prefix
        if hash_result.startswith(prefix):
            return number  # Return the number if condition is met

        number += 1  # Increment the number

filename = 'input.txt'
secret_key = parse_input(filename)

lowest_number = find_lowest_number_with_prefix(secret_key=secret_key)
print(lowest_number)
# answer is 9958218
