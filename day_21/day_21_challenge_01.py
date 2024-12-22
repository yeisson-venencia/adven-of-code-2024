import re


def load_data():
    with open("input_21.txt") as file:
        lines = file.read().splitlines()
    return lines


numeric_keypad = {
    "F": (0, 0),
    "0": (1, 0),
    "A": (2, 0),
    "1": (0, 1),
    "2": (1, 1),
    "3": (2, 1),
    "4": (0, 2),
    "5": (1, 2),
    "6": (2, 2),
    "7": (0, 3),
    "8": (1, 3),
    "9": (2, 3),
}

directional_keypad = {
    "<": (0, 0),
    "v": (1, 0),
    ">": (2, 0),
    "F": (0, 1),
    "^": (1, 1),
    "A": (2, 1),
}


def generate_movement_sequences(start, end, forbidden_location):
    xs, ys = start
    xe, ye = end
    horizontal_movement_symbol = ">" if xe > xs else "<"
    vertical_movement_symbol = "^" if ye > ys else "v"
    h_part = horizontal_movement_symbol * abs(xe - xs)
    v_part = vertical_movement_symbol * abs(ye - ys)
    possibilities = set()
    if (xe, ys) != forbidden_location:
        possibilities.add(h_part + v_part + "A")
    if (xs, ye) != forbidden_location:
        possibilities.add(v_part + h_part + "A")
    return possibilities


def generate_code_movement_sequences(codes, keypad):
    movement_sequences = []
    for code in codes:
        current_position = keypad["A"]
        code_sequences = [""]
        for symbol in code:
            end_position = keypad[symbol]
            possibilities = generate_movement_sequences(
                current_position, end_position, keypad["F"]
            )
            aux = code_sequences
            code_sequences = []
            for word in aux:
                for possibility in possibilities:
                    code_sequences.append(word + possibility)
            current_position = end_position
        for sequence in code_sequences:
            movement_sequences.append(sequence)
    min_len = min([len(x) for x in movement_sequences])
    interesting_movements = [x for x in movement_sequences if len(x) == min_len]
    return interesting_movements


def get_best_movement_len(code):
    first_sequence = generate_code_movement_sequences([code], numeric_keypad)
    second_sequence = generate_code_movement_sequences(
        first_sequence, directional_keypad
    )
    third_sequence = generate_code_movement_sequences(
        second_sequence, directional_keypad
    )
    min_len = min([len(x) for x in third_sequence])
    return min_len


def get_code_value(code):
    value_re = r"\d+"
    options = re.findall(value_re, code)
    return int(options[0])


def calculate_code_complexity(code):
    code_value = get_code_value(code)
    min_movement = get_best_movement_len(code)
    print(f"code = {code_value}, min mov = {min_movement}")
    return code_value * min_movement


def main():
    codes = load_data()
    total_complexity = 0
    for code in codes:
        total_complexity += calculate_code_complexity(code)
    print(total_complexity)


main()
