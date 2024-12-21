def load_data():
    with open("input_20.txt") as file:
        lines = file.read().splitlines()
        lines.reverse()
    return lines


def find_location(location_char, layout):
    for j, line in enumerate(layout):
        for i, character in enumerate(line):
            if character == location_char:
                return i, j
    return -1, -1


def process_layout(layout, start_location, location_dict):
    processing_pile = [(start_location, 0)]
    while len(processing_pile) > 0:
        location, cost = processing_pile.pop(0)
        x, y = location
        location_dict[location] = cost
        if layout[y][x] == "E":
            continue
        for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            dx, dy = direction
            new_location = (x + dx, y + dy)
            if new_location not in location_dict and layout[y + dy][x + dx] != "#":
                processing_pile.append((new_location, cost + 1))


def get_possible_cheat_movements(time_limit):
    possibilities = set()
    for i in range(time_limit + 1):
        for j in range(time_limit + 1 - i):
            possibilities.add((i, j))
            possibilities.add((i, -1 * j))
            possibilities.add((-1 * i, j))
            possibilities.add((-1 * i, -1 * j))
    return possibilities


def get_valid_cheats(min_time_to_save, location_dict, cheat_time_limit):
    valid_cheats = 0
    possibilities = get_possible_cheat_movements(cheat_time_limit)
    for location, cost in location_dict.items():
        x, y = location
        for cheat in possibilities:
            dx, dy = cheat
            new_location = (x + dx, y + dy)
            if new_location in location_dict and location_dict[
                new_location
            ] - cost >= min_time_to_save + abs(dx) + abs(dy):
                valid_cheats += 1
    return valid_cheats


def main():
    layout = load_data()
    start_location = find_location("S", layout)
    location_dict = dict()
    process_layout(layout, start_location, location_dict)
    print(get_valid_cheats(100, location_dict, 20))


main()
