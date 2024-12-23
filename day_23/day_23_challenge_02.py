def load_data():
    with open('input_23.txt') as file:
        lines = file.read().splitlines()
    return lines

def get_connections_dict(data):
    connections_dict = dict()

    for line in data:
        node_a,node_b = line.split('-')
        if node_a not in connections_dict:
            connections_dict[node_a] = set()
        if node_b not in connections_dict:
            connections_dict[node_b] = set()
        connections_dict[node_a].add(node_b)
        connections_dict[node_b].add(node_a)

    return connections_dict

def get_t_staring_nodes(connections_dict):
    t_starting_nodes = []
    for node,connections in connections_dict.items():
        if node[0] == 't':
            t_starting_nodes.append((node,list(connections)))
    return t_starting_nodes

def belong_to_mesh(connection,mesh, connections_dict):
    for node in mesh:
        if connection not in connections_dict[node]:
            return False
    return True

def get_largest_mesh(t_starting_nodes,connections_dict):
    largest_meshes = set()
    for node,connections in t_starting_nodes:
        t_meshes  = []
        for connection in connections:
            in_mesh = False
            for mesh in t_meshes:
                if belong_to_mesh(connection,mesh, connections_dict):
                    mesh.append(connection)
                    in_mesh = True
                    break
            if not in_mesh:
                t_meshes.append([node,connection])
        selected_mesh = []
        max_len = 0
        for mesh in t_meshes:
            if len(mesh) > max_len:
                selected_mesh = mesh
                max_len = len(mesh)
        selected_mesh.sort()
        largest_meshes.add(','.join(selected_mesh))

    max_len = 0
    largest_mesh = ''
    for mesh in largest_meshes:
        if len(mesh) > max_len:
            largest_mesh = mesh
            max_len = len(mesh)

    return largest_mesh


def main():
    data = load_data()
    connections_dict = get_connections_dict(data)
    t_starting_nodes = get_t_staring_nodes(connections_dict)
    largest_mesh = get_largest_mesh(t_starting_nodes,connections_dict)
    print(largest_mesh)

main()