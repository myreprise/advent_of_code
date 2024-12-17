
def calculate_encoded_difference(filename):

    total_code_characters = 0
    total_encoded_characters = 0

    with open(filename, 'r') as file:
        for line in file:

            # string newline and whitespace
            string_literal = line.strip()

            # original code length
            total_code_characters += len(string_literal)

            # encode the string: escape backslashes and double quotes, add outer quotes
            encoded_string = string_literal.replace("\\", "\\\\").replace('"','\\"')
            encoded_string = f'"{encoded_string}"'

            # Encoded string length
            total_encoded_characters += len(encoded_string)
    
    difference = total_encoded_characters - total_code_characters

    return difference

filename = "input.txt"
result = calculate_encoded_difference(filename)
print(result)
# answer is 