def main():
    data = []
    with open('day12/input', 'r') as f:
        data = f.readlines()

    nodes = {}

    for line in data:
        node, connections = line.strip().split(" <-> ")
        nodes[node] = {
            "name": node,
            "connections": []
        }

        for con in connections.split(", "):
            if con not in nodes:
                nodes[con] = {
                    "name": con,
                    "connections": []
                }
            print("Connecting {} to {}".format(node, con))

            nodes[node]["connections"].append(con)

    print("Connections for 2:", nodes['2']["connections"])
    # for k, v in nodes.items():
    #     print(k, v)es.items():
    #     print(k, v)

    visited = []
    keys = nodes.keys()
    group = 0

    while len(keys) != len(visited):
        total_nodes = -1  # this will remove the first move from the start node
        unreached = list(filter(lambda x: x not in visited, nodes.keys()))
        stack = [unreached[0]]
        while stack:
            cur_name = stack.pop()
            current = nodes[cur_name]
            connections = current["connections"]
            for c in connections:
                if c in visited:
                    # skip to next node
                    continue
                stack.append(c)
            visited.append(cur_name)
            total_nodes += 1
        group += 1
        print("Group", group, "Total nodes: ", total_nodes)


main()
