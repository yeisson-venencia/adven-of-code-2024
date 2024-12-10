def transform_line_to_operation(line):
    sides = line.split(':')
    result = int(sides[0])
    operands = [int(x) for x in sides[1].split()]
    return result, operands

def load_operations():
    with open("input_07.txt") as file:
        lines = file.read().splitlines()
        operations = [transform_line_to_operation(x) for x in lines]
    return operations

def base3number (n):
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    return ''.join(reversed(nums))

def compute_operation(operands, operators):
    result = operands[0]
    for index in range(len(operators)):
        if operators[index] == '+':
            result += operands[index + 1]
        elif operators[index] == '*':
            result *= operands[index + 1]
        else:
            result = int(f"{result}{operands[index + 1]}")
    return result

def generate_operator_array(option, number_of_operators):
    operations = ['+' for _ in range(number_of_operators)]
    base3_string = base3number(option)
    string_length = len(base3_string)
    for index in range(string_length):
        if base3_string[string_length -1-index] == '1':
            operations[index] = '*'
        if base3_string[string_length -1-index] == '2':
            operations[index] = '||'
    return operations

def is_solvable(operation):
    result = operation[0]
    operands = operation[1]
    number_of_operands = len(operands)
    number_of_operators = number_of_operands -1
    total_options = int(3 ** number_of_operators)
    for option in range(total_options):
        operators = generate_operator_array(option, number_of_operators)
        computation = compute_operation(operands, operators)
        if result == computation:
            return True
    return False

def main():
    operations = load_operations()
    total = 0
    for operation in operations:
        if is_solvable(operation):
            total += operation[0]
    print(f"total: {total}")

main()
