import networkx as nx


def find_cabinet(graph):
    """ Spin through the nodes in the graph and find the cabinet

    :param graph: The networkx graph object
    :return str: The node name of the cabinet
    """
    cabinets = []
    for node in graph.nodes:
        if "type" in graph.nodes[node].keys():
            if graph.nodes[node]["type"] == "Cabinet":
                cabinets.append(node)

    if not len(cabinets) == 1:
        print("Found more than one cabinet")
        raise IOError
    return cabinets[-1]


def get_all_paths_from_cabinet_to_nodes(graph):
    """ This function returns a dictionary of lists
    composed of cabinet to pot pairs

    :param graph:
    :return: a dictionary of lists composed of cabinet to
             pot pairs.
    """
    # find the cabinet
    cabinet = find_cabinet(graph)

    paths = nx.shortest_path(graph, weight="length", source=cabinet)

    return paths
