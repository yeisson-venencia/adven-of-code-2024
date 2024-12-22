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


best_direction_movements = {
    ("A", "^"): "<",
    ("A", ">"): "v",
    ("A", "v"): "<v",
    ("A", "<"): "v<<",
    ("A", "A"): "",
    ("v", "^"): "^",
    ("v", ">"): ">",
    ("v", "v"): "",
    ("v", "<"): "<",
    ("v", "A"): "^>",
    ("^", "^"): "",
    ("^", ">"): "v>",
    ("^", "v"): "v",
    ("^", "<"): "v<",
    ("^", "A"): ">",
    (">", "^"): "<^",
    (">", ">"): "",
    (">", "v"): "<",
    (">", "<"): "<<",
    (">", "A"): "^",
    ("<", "^"): ">^",
    ("<", ">"): ">>",
    ("<", "v"): ">",
    ("<", "<"): "",
    ("<", "A"): ">>^",
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


def generate_code_movement_sequences(code, keypad):
    movement_sequences = []
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


def get_interesting_options(options):
    min_len = min([len(x) for x in options])
    return [x for x in options if len(x) == min_len]


def get_dict_from_seq(seq):
    previous = 'A'
    seq_dict = dict()
    for symbol in seq:
        if (previous, symbol) in seq_dict:
            seq_dict[(previous, symbol)] += 1
        else:
            seq_dict[(previous, symbol)] = 1
        previous = symbol
    return seq_dict


def reduce_seq_dict(seq_dict):
    reduced_seq_dict = dict()
    for key, value in seq_dict.items():
        aux_dict = get_dict_from_seq(best_direction_movements[key] + "A")
        for aux_key, aux_value in aux_dict.items():
            if aux_key in reduced_seq_dict:
                reduced_seq_dict[aux_key] += value * aux_value
            else:
                reduced_seq_dict[aux_key] = value * aux_value
    return reduced_seq_dict


def get_seq_dict_value(seq_dict):
    total = 0
    for value in seq_dict.values():
        total += value
    return total


def get_interesting_dicts(option_dicts):
    min_len = min([get_seq_dict_value(x) for x in option_dicts])
    return [x for x in option_dicts if get_seq_dict_value(x) == min_len]


def get_best_movement_len(code, complexity_level):
    options = generate_code_movement_sequences(code, numeric_keypad)
    options = get_interesting_options(options)
    option_dicts = []
    for option in options:
        option_dicts.append(get_dict_from_seq(option))
    for i in range(complexity_level):
        new_option_dicts = []
        for option_dict in option_dicts:
            new_option_dicts.append(reduce_seq_dict(option_dict))
        option_dicts = get_interesting_dicts(new_option_dicts)
    min_len = min([get_seq_dict_value(x) for x in option_dicts])
    return min_len


def get_code_value(code):
    value_re = r"\d+"
    options = re.findall(value_re, code)
    return int(options[0])


def calculate_code_complexity(code, complexity_level):
    code_value = get_code_value(code)
    min_movement = get_best_movement_len(code, complexity_level)
    return code_value * min_movement


def main():
    codes = load_data()
    total_complexity = 0
    complexity_level = 25
    for code in codes:
        total_complexity += calculate_code_complexity(code, complexity_level)
    print(total_complexity)


main()
