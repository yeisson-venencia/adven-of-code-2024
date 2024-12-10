import re

def get_multiplication_matches(text):
    pattern = re.compile(r'mul\(\d{1,3},\d{1,3}\)')
    return  pattern.findall(text)

def calculate_multiplication(multiplication_text):
    values = multiplication_text.replace("mul(", "").replace(")", "").split(',')
    return int(values[0])*int(values[1])

def process_text(text):
    multiplication_instructions = get_multiplication_matches(text)
    total_value = 0
    for instruction in multiplication_instructions:
        total_value += calculate_multiplication(instruction)
    return total_value

with open('input_03.txt') as file:
    text = file.read()
    print(process_text(text))