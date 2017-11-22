from GraphParseCost import load, find_paths, cost_path
import pkg_resources
import pytest

@pytest.fixture
def graph():
    return load.load_graph(pkg_resources.resource_filename(__name__, "TestData/problem.graphml"))

@pytest.fixture
def costs():
    return load.load_rate_cards(pkg_resources.resource_filename(__name__, "TestData/cost_cards.json"))


def test_all_paths(graph, costs):
    paths = find_paths.get_all_paths_from_cabinet_to_nodes(graph)
    for i in paths.keys():
        allcosts = cost_path.cost_path(graph, paths[i], costs)
        print(paths[i], allcosts)