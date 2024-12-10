def load_layout():
    layout = []
    with open("input_10.txt") as file:
        lines = file.read().splitlines()
        lines.reverse()
        for line in lines:
            line_height=list()
            for value in line:
                line_height.append(int(value))
            layout.append(line_height)
    return layout

def is_available_position(position, layout):
    vertical_limit = len(layout)
    horizontal_limit = len(layout[0])
    is_between_horizontal = position[0] >= 0 and position[0] < horizontal_limit
    is_between_vertical = position[1] >= 0 and position[1] < vertical_limit
    return is_between_horizontal and is_between_vertical

def is_adjacent_height(position, layout, reference_height):
    v_coo = position[1]
    h_coo = position[0]
    return layout[v_coo][h_coo] == reference_height - 1

def get_adjacent_heights(position,layout):
    v_coo = position[1]
    h_coo = position[0]
    position_height = layout[v_coo][h_coo]
    adjacent_locations = [(h_coo + 1, v_coo), (h_coo - 1, v_coo), (h_coo, v_coo + 1), (h_coo, v_coo - 1)]
    adjacent_heights = [x for x in adjacent_locations
                        if is_available_position(x, layout)
                        and is_adjacent_height(x, layout, position_height)]
    return adjacent_heights

def locate_height(height,layout):
    locations = []
    for vertical_index, line in enumerate(layout):
        for horizontal_index, terrain_height in enumerate(line):
            if terrain_height == height:
                locations.append((horizontal_index, vertical_index))
    return locations

def initialize_trailhead_dict(nines, layout):
    trailhead_dict = dict()
    for nine in nines:
        adjacent_positions = get_adjacent_heights(nine, layout)
        for position in adjacent_positions:
            position_height = layout[position[1]][position[0]]
            key_name = f"{position_height}-{position[0]}-{position[1]}"
            if key_name in trailhead_dict.keys():
                trailhead_dict[key_name].add(nine)
            else:
                trailhead_dict[key_name] = {nine}

    return trailhead_dict

def downgrade_trailhead_dict(trailhead_dict, layout):
    level = 8
    while level > 0:
        original_level_keys = [x for x in trailhead_dict.keys()]
        for sector_label_key in original_level_keys:
            key_components = sector_label_key.split("-")
            reachable_nine_heights = trailhead_dict[sector_label_key]
            sector_position = int(key_components[1]), int(key_components[2])
            adjacent_positions = get_adjacent_heights(sector_position, layout)
            for adjacent_position in adjacent_positions:
                key_name = f"{level - 1}-{adjacent_position[0]}-{adjacent_position[1]}"
                if not key_name in trailhead_dict.keys():
                    trailhead_dict[key_name] = set()
                for nine in reachable_nine_heights:
                    trailhead_dict[key_name].add(nine)
            trailhead_dict.pop(sector_label_key)
        level -= 1

def valuate_trailhead_dict(trailhead_dict):
    total = 0
    for key in trailhead_dict.keys():
        total += len(trailhead_dict[key])
    print(f"total: {total}")

def main():
    layout = load_layout()
    nine_height_positions = locate_height(9, layout)
    trailhead_dict = initialize_trailhead_dict(nine_height_positions, layout)
    downgrade_trailhead_dict(trailhead_dict, layout)
    valuate_trailhead_dict(trailhead_dict)

main()