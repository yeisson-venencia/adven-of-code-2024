def load_data():
    with open('input_15.txt') as file:
        lines = file.read().splitlines()
        layout = []
        instructions = []
        for line in lines:
            if len(line) == 0:
                continue
            if line[0] == '#':
                layout_line = []
                for x in line:
                    if x == 'O':
                        layout_line.append('[')
                        layout_line.append(']')
                    elif x == '@':
                        layout_line.append('@')
                        layout_line.append('.')
                    else:
                        layout_line.append(x)
                        layout_line.append(x)

                layout.append(layout_line)
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
    '^': 1,
    'v': -1,
    '<': -1,
    '>': 1,
}

def  print_layout(layout):
    print()
    for i in range(len(layout)):
        print(''.join(layout[len(layout) -1 -i]))

def get_box_vertical_move_analysis(box,layout,move):
    bx,by = box
    in_front = [layout[by+move][bx], layout[by+move][bx+1]]
    if '#' in in_front:
        return True, False, set()
    if in_front[0] == '.' and in_front[1] == '.':
        return False, True, set()
    to_check = set()
    if in_front[0] == '[':
        to_check.add((bx,by+move))
    elif in_front[0] == ']':
        to_check.add((bx-1,by+move))

    if in_front[1] == '[':
        to_check.add((bx+1,by+move))
    elif in_front[1] == ']':
        to_check.add((bx, by + move))

    return False, False, to_check

def calculate_total(layout):
    total_value = 0
    for j in range(len(layout)):
        for i in range(len(layout[0])):
            if layout[j][i] == '[':
                total_value += 100 * (len(layout) - j - 1) + i
    print(total_value)

def execute_instructions(layout,instructions):
    robot_location = find_robot_location(layout)
    # print_layout(layout)
    for instruction_batch in instructions:
        for instruction in instruction_batch:
            if instruction not in movement_dic:
                continue
            rx, ry = robot_location
            if instruction  in ['<','>']:
                movement = movement_dic[instruction]
                distance_to_space = -1
                for x in range(1, 1000):
                    content = layout[ry][rx + movement * x]
                    if content == '.':
                        distance_to_space = x
                        break
                    if content == '#':
                        break
                if distance_to_space > 0:
                    for x in range(0,distance_to_space):
                        layout[ry][rx + movement * (distance_to_space - x)] = layout[ry][rx + movement * (distance_to_space - x -1)]
                    layout[ry][rx] = '.'
                    robot_location = rx + movement, ry
            else:
                movement = movement_dic[instruction]
                content = layout[ry + movement ][rx]
                if content == '.':
                    layout[ry + movement ][rx] = '@'
                    layout[ry][rx] = '.'
                    robot_location = rx , ry + movement
                elif content == '#':
                    pass
                else:
                    to_check_list = []
                    if content == '[':
                        to_check_list.append({(rx,ry+movement)})
                    else:
                        to_check_list.append({(rx-1, ry + movement)})
                    able_to_move = False
                    for level in range(0, 1000):
                        boxes = to_check_list[level]
                        analysis = [get_box_vertical_move_analysis(box,layout, movement) for box in boxes]
                        if True in [x[0] for x in analysis]:
                            break
                        if False not in [x[1] for x in analysis]:
                            able_to_move = True
                            break
                        boxs_to_check = set()
                        for result in analysis:
                            for box in result[2]:
                                boxs_to_check.add(box)
                        to_check_list.append(boxs_to_check)

                    if able_to_move:
                        to_check_list.reverse()
                        for level in range(len(to_check_list)):
                            for box in to_check_list[level]:
                                bx,by = box
                                layout[by + movement][bx] = '['
                                layout[by + movement][bx + 1] = ']'
                                layout[by][bx] = '.'
                                layout[by][bx + 1] = '.'
                        layout[ry + movement][rx] = '@'
                        layout[ry][rx] = '.'
                        robot_location = rx, ry + movement

def main():
    layout, instructions = load_data()
    execute_instructions(layout,instructions)
    calculate_total(layout)

main()
