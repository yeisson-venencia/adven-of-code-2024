def load_bytes_locations():
    with open('input_18.txt') as file:
        lines = file.read().splitlines()
        bytes_locations = []
        for line in lines:
            coordinates = line.split(',')
            bytes_locations.append((int(coordinates[0]),int(coordinates[1])))
    return bytes_locations

def generate_layout(bytes_locations, width, height, timestamp):
    layout = [['.' for _ in range(width)] for _ in range(height)]
    for second in range(timestamp):
        x,y = bytes_locations[second]
        layout[y][x] = '#'
    return layout

def print_layout(layout):
    for i in range(len(layout)):
        print(''.join(layout[i]))

def process_location(layout, instructions, location_map, x_limit, y_limit):
    location, cost = instructions
    x,y = location
    if layout[y][x] == '#':
        return []

    if location in location_map and location_map[location] <= cost:
        return []

    location_map[location] = cost
    if layout[y][x] == 'E':
        return []

    new_instructions = []
    for direction in [(0,1),(1,0),(-1,0),(0,-1)]:
        dx,dy = direction
        nx = x + dx
        ny = y + dy
        if nx in range(x_limit) and ny in range(y_limit):
            new_instructions.append(((x+dx,y+dy),cost+1))
    return new_instructions

def is_exit_possible(bytes_locations, timestamp):
    LAYOUT_DIMENSION = 71
    layout = generate_layout(bytes_locations, LAYOUT_DIMENSION, LAYOUT_DIMENSION, timestamp)
    layout[LAYOUT_DIMENSION - 1][LAYOUT_DIMENSION - 1] = 'E'
    exit_location = LAYOUT_DIMENSION-1,LAYOUT_DIMENSION -1

    location_map = dict()
    instruction_pile = [((0,0),0)]
    exit_found = False
    while len(instruction_pile) > 0 and not exit_found:
        current_instruction = instruction_pile.pop(0)
        new_instructions = process_location(layout, current_instruction, location_map,LAYOUT_DIMENSION,LAYOUT_DIMENSION)
        for instruction in new_instructions:
            instruction_pile.append(instruction)
        if exit_location in location_map:
            exit_found = True
    return exit_found

def main():
    bytes_locations = load_bytes_locations()
    possible_limit = 0
    impossible_limit = len(bytes_locations)
    while impossible_limit - possible_limit > 1:
        test_case = possible_limit + (impossible_limit - possible_limit) // 2
        if is_exit_possible(bytes_locations, test_case):
            possible_limit = test_case
        else:
            impossible_limit = test_case
    print(f"possible_limit = {possible_limit} - impossible_limit = {impossible_limit}")
    print(f"impossible limit coordinates = {bytes_locations[possible_limit]}")

main()