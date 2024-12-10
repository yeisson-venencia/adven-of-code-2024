def load_layout():
    with open("input_08.txt") as input_file:
        lines = input_file.read().splitlines()
        lines.reverse()
    return lines

def is_antenna(element):
    return element != '.'

def is_inside_layout(current_position, layout):
    vertical_limit = len(layout)
    horizontal_limit = len(layout[0])
    is_between_horizontal = current_position[0] >= 0 and current_position[0] < horizontal_limit
    is_between_vertical = current_position[1] >= 0 and current_position[1] < vertical_limit
    return is_between_horizontal and is_between_vertical

def get_slope_parameters(fist_position, second_position):
    dx = fist_position[0] - second_position[0]
    dy = fist_position[1] - second_position[1]
    return dx, dy

def look_for_antinodes(original_antenna, antenna_family_array, antinode_set, layout):
    for antenna in antenna_family_array:
        dx, dy = get_slope_parameters(original_antenna, antenna)
        first_antinode = original_antenna[0] + dx, original_antenna[1] + dy
        second_antinode = antenna[0] - dx, antenna[1] - dy
        if is_inside_layout(first_antinode, layout):
            antinode_set.add(first_antinode)
        if is_inside_layout(second_antinode, layout):
            antinode_set.add(second_antinode)

def analyze_antenna(antenna_code, antenna_position, antenna_dictionary, antinode_set, layout):
    if antenna_code in antenna_dictionary.keys():
        antenna_family_array = antenna_dictionary.get(antenna_code)
        look_for_antinodes(antenna_position, antenna_family_array, antinode_set, layout)
        antenna_family_array.append(antenna_position)
    else:
        antenna_dictionary[antenna_code] = [antenna_position]

def main():
    layout = load_layout()
    vertical_limit = len(layout)
    horizontal_limit = len(layout[0])
    antenna_dictionary = dict()
    antinode_set = set()
    for j in range(vertical_limit):
        for i in range(horizontal_limit):
            element = layout[j][i]
            if is_antenna(element):
                analyze_antenna(element, (i, j), antenna_dictionary, antinode_set, layout)
    print(len(antinode_set))

main()  