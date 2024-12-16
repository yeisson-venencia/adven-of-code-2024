def load_data():
    with open('input_01.txt') as file:
        lines = file.read().splitlines()
        first_array = []
        second_array = []
        for line in lines:
            values = line.split()
            first_array.append(int(values[0]))
            second_array.append(int(values[1]))
    return first_array, second_array

def calculate_similarity(first_array, second_array):
    total_similarity = 0
    for item in first_array:
        total_appears = second_array.count(item)
        total_similarity += item * total_appears

    print(total_similarity)


def main():
    fa, sa = load_data()
    calculate_similarity(fa,sa)

main()

