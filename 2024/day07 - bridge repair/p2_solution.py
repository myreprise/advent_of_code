from itertools import product

def read_input(file_path):
    """
    Reads the input file
    """

    with open(file_path, 'r') as file:
        data = file.read()
    
    return data

def parse_input(input_text):
    """
    Parse input into a list of equations
    Each equation is represented as (test_value, numbers)
    """


    equations = []

    for line in input_text.strip().splitlines():
        test_value, numbers = line.split(':')
        test_value = int(test_value.strip())
        numbers = list(map(int, numbers.strip().split()))
        equations.append((test_value, numbers))
    
    return equations


def evaluate_expression(numbers, operators):
    """
    Evaluate the expression given the numbers and operators
    Operators are applied left to right
    """

    result = numbers[0]
    for i, op in enumerate(operators):
        if op == '+':
            result += numbers[i + 1]
        elif op == '*':
            result *= numbers[i+1]
        elif op == '||':
            # concatenate the current result with the next number
            result = int(str(result) + str(numbers[i+1]))
    return result


def is_valid_equation(test_value, numbers):
    """
    Check if the test value can be produced by inserting operators into numbers
    """

    operator_combinations = product(['+','*','||'], repeat = len(numbers) - 1)
    
    # Generate all possible combinations of '+' and '*' for (n-1) gaps
    for operators in operator_combinations:
        result = evaluate_expression(numbers=numbers, operators=operators)
        if result == test_value:
            return True
    return False

def total_calibration_result(equations):
    """
    Determine the total calibration result by summing valid test values
    """

    equations = parse_input(input_text=input_text)
    total_sum = 0
    count = len(equations)

    for test_value, numbers in equations:
        print(count)
        if is_valid_equation(test_value, numbers):
            total_sum += test_value
        count -= 1

    return total_sum

input_text = read_input('input.txt')
equations = parse_input(input_text)

result = total_calibration_result(equations)
print(result)
# answer is 110365987435001