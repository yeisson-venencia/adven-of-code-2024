def load_matrix():
    with open('input_04.txt') as f:
        matrix = f.read().splitlines()
    return matrix

def is_scanable(vertical_index, horizontal_index, vertical_limit, horizontal_limit):
    is_possible_vertical = vertical_index > 0 and vertical_index < vertical_limit - 1
    is_possible_horizontal = horizontal_index > 0 and horizontal_index < horizontal_limit - 1
    return is_possible_vertical and is_possible_horizontal

def get_first_word_coordinates(vertical_index, horizontal_index):
    coordinates = []
    coordinates.append((vertical_index + 1,horizontal_index - 1))
    coordinates.append((vertical_index,horizontal_index))
    coordinates.append((vertical_index - 1,horizontal_index + 1))
    return coordinates

def get_second_word_coordinates(vertical_index, horizontal_index):
    coordinates = []
    coordinates.append((vertical_index - 1,horizontal_index - 1))
    coordinates.append((vertical_index,horizontal_index))
    coordinates.append((vertical_index + 1,horizontal_index + 1))
    return coordinates

def get_word_from_coordinates(coordinates, matrix):
    word = ''
    for coordinate in coordinates:
        v_coordinate, h_coordinate = coordinate
        word += matrix[v_coordinate][h_coordinate]
    return word

def is_valid_word(word):
    return word == 'MAS' or word == 'SAM'

def is_coordinate_xmas(vertical_index, horizontal_index, vertical_limit, horizontal_limit, matrix):
    if not is_scanable(vertical_index, horizontal_index, vertical_limit, horizontal_limit):
        return False
    first_word = get_word_from_coordinates(get_first_word_coordinates(vertical_index, horizontal_index), matrix)
    second_word = get_word_from_coordinates(get_second_word_coordinates(vertical_index, horizontal_index), matrix)
    return is_valid_word(first_word) and is_valid_word(second_word)

def main():
    matrix = load_matrix()
    matrix_horizontal_length = len(matrix[0])
    matrix_vertical_length = len(matrix)
    total_xmas = 0
    for j in range(matrix_vertical_length):
        for i in range(matrix_horizontal_length):
            if matrix[j][i] == 'A':
                total_xmas += 1 if is_coordinate_xmas(j, i, matrix_vertical_length, matrix_horizontal_length, matrix) else 0
    print(total_xmas)

main()