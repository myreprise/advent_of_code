


def calculate_code_memory_difference(file_path):
    total_code_characters = 0
    total_memory_characters = 0

    with open(filename, 'r') as file:
        for line in file:
            # string newline and whitespace
            string_literal = line.strip()

            # total code representation count
            total_code_characters += len(string_literal)

            # evaluate the string to get its in-memory representaiton
            in_memory_string = eval(string_literal)
            total_memory_characters += len(in_memory_string)
        
    # compute the difference
    difference = total_code_characters - total_memory_characters
    return difference


filename = 'input.txt'
result = calculate_code_memory_difference(filename)
print(result)
# answer is 