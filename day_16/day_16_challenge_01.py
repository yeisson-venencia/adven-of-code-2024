def load_layout():
    with open('input_16.txt') as file:
        lines = file.read().splitlines()
        lines.reverse()
    return lines

def get_map_location(layout,box_content):
    for j, line in enumerate(layout):
        for i, char in enumerate(line):
            if char == box_content:
                return i,j
    return 0,0

def get_possible_directions(heading):
    all_directions = [(0,1),(1,0),(-1,0),(0,-1)]
    x,y = heading
    impossible_direction = -1*x,-1*y
    return [direction for direction in all_directions if direction != impossible_direction]

def get_additional_cost(heading, direction):
    xa,ya = heading
    xb,yb = direction
    product = xa*xb + ya*yb
    if product == 1:
        return 1
    return 1001

def process_location(layout, instructions, location_map):
    location, heading, cost = instructions
    x,y = location
    if layout[y][x] == '#':
        return []

    if location in location_map and location_map[location] <= cost:
        return []

    location_map[location] = cost
    if layout[y][x] == 'E':
        return []

    new_instructions = []
    for direction in get_possible_directions(heading):
        dx,dy = direction
        new_instructions.append(((x+dx,y+dy),direction,cost+get_additional_cost(heading,direction)))
    return new_instructions

def main():
    layout = load_layout()
    start_location = get_map_location(layout,'S')
    location_map = dict()
    instruction_pile = [(start_location,(1,0),0)]
    while len(instruction_pile) > 0:
        current_instruction = instruction_pile.pop(0)
        new_instructions = process_location(layout, current_instruction, location_map)
        for instruction in new_instructions:
            instruction_pile.append(instruction)
    end_location = get_map_location(layout,'E')
    print(location_map[end_location])

main()
