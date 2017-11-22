import argparse
from . import load, find_paths, cost_path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("graph_data", help="graphml formatted graph to work on")
    parser.add_argument("cost_cards", help="Cost card json data")

    args = parser.parse_args()
    graph = load.load_graph(args.graph_data)
    costcards = load.load_rate_cards(args.cost_cards)

    paths = find_paths.get_all_paths_from_cabinet_to_nodes(graph)
    for i in paths.keys():
        allcosts = cost_path.cost_path(graph, paths[i], costcards)
        print(paths[i], allcosts)


if __name__=="__main__":
    main()