def load_layout():
    with open('input_16.txt') as file:
        lines = file.read().splitlines()
        lines.reverse()
        layout = []
        for line in lines:
            layout.append([x for x in line])
    return layout

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

def process_location(layout, path, location_map):
    location, heading, cost, visited = path
    x, y = location
    if layout[y][x] == '#':
        return []

    if (location, heading) in location_map and location_map[(location, heading)][0] < cost:
        return []

    if (location, heading) not in location_map:
        location_map[(location, heading)] = (cost,visited.copy())
    elif cost == location_map[(location, heading)][0]:
        for item in visited:
            location_map[(location, heading)][1].add(item)
    else:
        location_map[(location, heading)] = (cost,visited.copy())

    if layout[y][x] == 'E':
        return []

    new_paths = []
    for direction in get_possible_directions(heading):
        dx,dy = direction
        new_location = (x+dx,y+dy)
        if new_location not in visited:
            visited_copy = visited.copy()
            visited_copy.add(location)
            new_paths.append((new_location,direction,cost+get_additional_cost(heading, direction),visited_copy))
    return new_paths

def  print_layout(layout):
    for i in range(len(layout)):
        print(''.join(layout[len(layout) -1 -i]))

def main():
    layout = load_layout()
    start_location = get_map_location(layout,'S')
    location_map = dict()
    path_pile = [(start_location,(1,0),0,set())]
    while len(path_pile) > 0:
        current_path = path_pile.pop(0)
        new_paths = process_location(layout, current_path, location_map)
        for path in new_paths:
            path_pile.append(path)

    end_location = get_map_location(layout, 'E')
    ends_dict = []
    for key,value in location_map.items():
        if key[0] == end_location:
            ends_dict.append(value)
    min_value = min([x for x,y in ends_dict])
    min_ends_dict = [x for x in ends_dict if x[0] == min_value]
    final_visited = set()
    for value, locations in min_ends_dict:
        for location in locations:
            final_visited.add(location)

    # for location in final_visited:
    #     x,y = location
    #     layout[y][x] = 'O'
    # layout[start_location[1]][start_location[0]] = 'S'
    # print_layout(layout)
    print(len(final_visited) + 1)
main()
