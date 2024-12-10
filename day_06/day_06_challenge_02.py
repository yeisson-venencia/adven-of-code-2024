def load_layout():
    with open("input_06.txt") as file:
        lines = file.read().splitlines()
        lines.reverse()
    return lines

def get_initial_position(layout):
    for line,vertical_index in zip(layout,range(len(layout))):
        if '^' in line:
            horizontal_index = line.index('^')
            return horizontal_index, vertical_index
    return -1,-1

def is_inside_layout(current_position, layout):
    vertical_limit = len(layout)
    horizontal_limit = len(layout[0])
    is_between_horizontal = current_position[0] >= 0 and current_position[0] < horizontal_limit
    is_between_vertical = current_position[1] >= 0 and current_position[1] < vertical_limit
    return is_between_horizontal and is_between_vertical

def get_next_direction(direction):
    direction_map = {'N': 'E', 'S': 'W', 'E': 'S', 'W': 'N'}
    return direction_map[direction]

def get_vertical_variation(direction):
    vertical_variation_map = {'N': 1, 'S': -1, 'E': 0, 'W': 0}
    return vertical_variation_map[direction]

def get_horizontal_variation(direction):
    horizontal_variation_map = {'N': 0, 'S': 0, 'E': 1, 'W': -1}
    return horizontal_variation_map[direction]

def is_available_position(layout, position):
    if not is_inside_layout(position, layout):
        return True
    vertical_index = position[1]
    horizontal_index = position[0]
    return not layout[vertical_index][horizontal_index] == '#'

def is_available_position_with_obstruction(layout, obstruction, position):
    if not is_inside_layout(position, layout):
        return True
    if obstruction == position:
        return False
    vertical_index = position[1]
    horizontal_index = position[0]
    return not layout[vertical_index][horizontal_index] == '#'

def get_next_position(position, direction):
    next_position = position[0] + get_horizontal_variation(direction), position[1] + get_vertical_variation(direction)
    return next_position

def is_loopable_position(possible_loop_position, position, direction, moves, layout):
    current_position = position
    current_direction = direction
    completed_moves = moves.copy()
    while is_inside_layout(current_position, layout) :
        next_position = get_next_position(current_position, current_direction)
        if is_available_position_with_obstruction(layout,possible_loop_position, next_position):
            if (current_position, current_direction) in completed_moves:
                return True
            completed_moves.add((current_position, current_direction))
            current_position = next_position
        else:
            current_direction = get_next_direction(current_direction)
    return False

def main():
    layout = load_layout()
    initial_position = get_initial_position(layout)
    current_position = initial_position
    current_direction = 'N'
    completed_moves = set()
    studied_locations = set()
    total_loopable_positions = 0
    while is_inside_layout(current_position, layout):
        next_position = get_next_position(current_position, current_direction)
        if is_available_position(layout, next_position):
            if next_position not in studied_locations:
                studied_locations.add(next_position)
                total_loopable_positions += 1 if is_loopable_position(next_position,current_position,current_direction,completed_moves,layout) else 0
            completed_moves.add((current_position,current_direction))
            current_position = next_position
        else:
            current_direction = get_next_direction(current_direction)
    print(f"Total loopable positions: {total_loopable_positions}")

main()