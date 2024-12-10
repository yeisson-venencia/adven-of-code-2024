import re

def get_instructions_matches(text):
    pattern = re.compile(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)")
    return  pattern.findall(text)

def calculate_multiplication(multiplication_text):
    values = multiplication_text.replace("mul(", "").replace(")", "").split(',')
    return int(values[0])*int(values[1])

def process_text(text):
    instructions_list = get_instructions_matches(text)
    total_value = 0
    operation_enabled = True
    for instruction in instructions_list:
        if instruction == "do()":
            operation_enabled = True
        elif instruction == "don't()":
            operation_enabled = False
        else:
            total_value += calculate_multiplication(instruction) if operation_enabled else 0
    return total_value

with open('input_03.txt') as file:
    text = file.read()
    print(process_text(text))

# sample = "(who() what())do()>when()why()'mul(454,153)mul(565,994)don't()(mul(890,533)#mul(875,768)+'-^where()}when()mul(103,598)[mul(401,600)"
# pattern = re.compile(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)")
# matches = pattern.findall(sample)
# print(matches)
