def load_data():
    with open('input_15.txt') as file:
        lines = file.read().splitlines()
        layout = []
        instructions = []
        for line in lines:
            if len(line) == 0:
                continue
            if line[0] == '#':
                layout.append([x for x in line])
            else:
                instructions.append(line)
        layout.reverse()
    return layout, instructions,

def find_robot_location(layout):
    for j in range(len(layout)):
        for i in range(len(layout[0])):
            if layout[j][i] == '@':
                return i,j
    return None

movement_dic = {
    '^': (0,1),
    'v': (0,-1),
    '<': (-1,0),
    '>': (1,0),
}

def  print_layout(layout):
    for i in range(len(layout)):
        print(layout[len(layout) -1 -i])

def main():
    layout, instructions = load_data()
    robot_location = find_robot_location(layout)

    for instruction_batch in instructions:
        for instruction in instruction_batch:
            rx,ry = robot_location
            if instruction not in movement_dic:
                continue
            movement = movement_dic[instruction]
            mx,my = movement
            distance_to_space = -1
            for x in range(1,1000):
                content = layout[ry+my*x][rx+mx*x]
                if content == '.':
                    distance_to_space = x
                    break
                if content == '#':
                    break

            if distance_to_space > 0:
                layout[ry + my*distance_to_space][rx + mx*distance_to_space] = 'O'
                layout[ry + my][rx + mx] = '@'
                layout[ry][rx] = '.'
                robot_location = rx + mx, ry + my

        # print_layout(layout)

    total_value = 0
    for j in range(len(layout)):
        for i in range(len(layout[0])):
            if layout[j][i] == 'O':
                total_value += 100 * (len(layout) - j - 1) + i
    print(total_value)

main()
