
def cost_path(graph, path, costs):
    """Takes a path and calculates the costs per ratecard

    :param graph: The networkx graph object of the layout
    :param list path: The path from the cabinet to the end point
    :param list costs: List of dicts of the cost cards
    """
    path_length = 0
    total_costs = {}
    for costcard in costs:
        total_costs[costcard["card_name"]] = {}
    for i in range(0, len(path)):
        if not i == len(path)-1:
            edge = graph.get_edge_data(path[i], path[i+1])
            path_length += edge["length"]
        node_type = graph.nodes[path[i]]["type"]
        for card in costs:
            card_name = card["card_name"]
            if node_type in card["costs_single"]:
                if "costs_single" not in total_costs[card_name]:
                    total_costs[card_name]["costs_single"] = 0
                total_costs[card_name]["costs_single"] += card["costs_single"][node_type]

            if not i == len(path)-1:
                if edge["material"] in card["costs_per_m"]:
                    cost = edge["length"] * card["costs_per_m"][edge["material"]]
                    if "costs_per_m" not in total_costs[card_name].keys():
                        total_costs[card_name]["costs_per_m"] = 0
                    total_costs[card_name]["costs_per_m"] += cost

            if i == len(path)-1:
                if node_type in card["costs_per_total_length"]:
                    cost = path_length * card["costs_per_total_length"][node_type]
                    if "costs_per_total_length" not in total_costs[card_name]:
                        total_costs[card_name]["costs_per_total_length"] = 0
                    total_costs[card_name]["costs_per_total_length"] += cost

    for i in total_costs:
        total_costs[i]["Total"] = 0
        for area in total_costs[i]:
            total_costs[i]["Total"] += total_costs[i][area]

    return total_costs
