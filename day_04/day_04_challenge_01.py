def load_matrix():
    with open('input_04.txt') as f:
        matrix = f.read().splitlines()
    return matrix

def is_possible_detail(vertical_index, horizontal_index, vertical_limit, horizontal_limit):
    is_possible_down = vertical_index > 2
    is_possible_up = vertical_index < vertical_limit - 3
    is_possible_right = horizontal_index < horizontal_limit - 3
    is_possible_left = horizontal_index > 2
    return is_possible_up, is_possible_down, is_possible_right, is_possible_left

def get_word_coordinates(vertical_index, horizontal_index, vertical_scale, horizontal_scale):
    coordinates = []
    for increment in range(4):
        coordinates.append((vertical_index + vertical_scale * increment , horizontal_index + horizontal_scale * increment))
    return coordinates

def get_first_word_coordinates(vertical_index, horizontal_index):
    return get_word_coordinates(vertical_index, horizontal_index, 0, 1)

def get_second_word_coordinates(vertical_index, horizontal_index):
    return get_word_coordinates(vertical_index, horizontal_index, 1, 1)

def get_third_word_coordinates(vertical_index, horizontal_index):
    return get_word_coordinates(vertical_index, horizontal_index, 1, 0)

def get_fourth_word_coordinates(vertical_index, horizontal_index):
    return get_word_coordinates(vertical_index, horizontal_index, 1, -1)

def get_fifth_word_coordinates(vertical_index, horizontal_index):
    return get_word_coordinates(vertical_index, horizontal_index, 0, -1)

def get_sixth_word_coordinates(vertical_index, horizontal_index):
    return get_word_coordinates(vertical_index, horizontal_index, -1, -1)

def get_seventh_word_coordinates(vertical_index, horizontal_index):
    return get_word_coordinates(vertical_index, horizontal_index, -1, 0)

def get_eighth_word_coordinates(vertical_index, horizontal_index):
    return get_word_coordinates(vertical_index, horizontal_index, -1, 1)

def get_word_from_coordinates(coordinates, matrix):
    word = ''
    for coordinate in coordinates:
        v_coordinate, h_coordinate = coordinate
        word += matrix[v_coordinate][h_coordinate]
    return word

def scan_coordinate(vertical_index, horizontal_index, vertical_limit, horizontal_limit, matrix):
    words = []
    is_possible_up, is_possible_down, is_possible_right, is_possible_left = is_possible_detail(vertical_index, horizontal_index, vertical_limit, horizontal_limit)
    if is_possible_right:
        words.append(get_word_from_coordinates(get_first_word_coordinates(vertical_index, horizontal_index), matrix))
    if is_possible_right and is_possible_up:
        words.append(get_word_from_coordinates(get_second_word_coordinates(vertical_index, horizontal_index), matrix))
    if is_possible_up:
        words.append(get_word_from_coordinates(get_third_word_coordinates(vertical_index, horizontal_index), matrix))
    if is_possible_up and is_possible_left:
        words.append(get_word_from_coordinates(get_fourth_word_coordinates(vertical_index, horizontal_index), matrix))
    if is_possible_left:
        words.append(get_word_from_coordinates(get_fifth_word_coordinates(vertical_index, horizontal_index), matrix))
    if is_possible_left and is_possible_down:
        words.append(get_word_from_coordinates(get_sixth_word_coordinates(vertical_index, horizontal_index), matrix))
    if is_possible_down:
        words.append(get_word_from_coordinates(get_seventh_word_coordinates(vertical_index, horizontal_index), matrix))
    if is_possible_down and is_possible_right:
        words.append(get_word_from_coordinates(get_eighth_word_coordinates(vertical_index, horizontal_index), matrix))
    total_valid_word = len([x for x in words if x == 'XMAS'])
    return total_valid_word

def main():
    matrix = load_matrix()
    matrix_horizontal_length = len(matrix[0])
    matrix_vertical_length = len(matrix)
    total_xmas = 0
    for j in range(matrix_vertical_length):
        for i in range(matrix_horizontal_length):
            if matrix[j][i] == 'X':
                total_xmas += scan_coordinate(j, i, matrix_vertical_length, matrix_horizontal_length, matrix)
    print(total_xmas)

main()