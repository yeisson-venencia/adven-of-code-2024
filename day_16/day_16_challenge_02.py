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

def process_location(layout, path, location_map, e_visited):
    location, heading, cost, visited = path
    x, y = location
    if layout[y][x] == '#':
        return []

    if (location, heading) in location_map and cost > location_map[(location, heading)]:
        return []

    location_map[(location, heading)] = cost

    if layout[y][x] == 'E':
        e_cost = e_visited[0]
        if cost == e_cost:
            for v_location in visited:
                e_visited[1].add(v_location)
            e_visited[1].add(location)
        elif cost < e_cost:
            new_e_set = set()
            for v_location in visited:
                new_e_set.add(v_location)
            new_e_set.add(location)
            e_visited[1] = new_e_set
            e_visited[0] = cost
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
    e_visited = [1000000000, set()]
    path_pile = [(start_location,(1,0),0,set())]
    while len(path_pile) > 0:
        current_path = path_pile.pop(0)
        new_paths = process_location(layout, current_path, location_map, e_visited)
        for path in new_paths:
            path_pile.append(path)

    # end_location = get_map_location(layout, 'E')
    # for location in e_visited[1]:
    #     x,y = location
    #     layout[y][x] = 'O'
    # layout[start_location[1]][start_location[0]] = 'S'
    # layout[end_location[1]][end_location[0]] = 'E'
    # print_layout(layout)

    print(len(e_visited[1]))
main()
