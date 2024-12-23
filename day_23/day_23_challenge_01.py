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

def get_interconnections(t_starting_nodes, connections_dict):
    inter_connections = set()
    for node,connections in t_starting_nodes:
        for i in range(len(connections)-1):
            for j in range(i+1,len(connections)):
                if connections[j] in connections_dict[connections[i]]:
                    triangle = [node,connections[i], connections[j]]
                    triangle.sort()
                    inter_connections.add(','.join(triangle))
    return inter_connections

def main():
    data = load_data()
    connections_dict = get_connections_dict(data)
    t_starting_nodes = get_t_staring_nodes(connections_dict)
    inter_connections = get_interconnections(t_starting_nodes, connections_dict)
    print(len(inter_connections))

main()