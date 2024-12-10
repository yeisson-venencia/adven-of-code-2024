with open('input_01.txt') as file:
    lines = file.read().splitlines()
    first_array = []
    second_array = []
    for line in lines:
        values = line.split()
        first_array.append(int(values[0]))
        second_array.append(int(values[1]))

    first_array.sort()
    second_array.sort()

    total_distance = 0
    for i in range(len(first_array)):
        distance = abs(second_array[i] - first_array[i])
        total_distance += distance

    print(total_distance)