from GraphParseCost import load, find_paths
import pkg_resources
import pytest

@pytest.fixture
def graph():
    return load.load_graph(pkg_resources.resource_filename(__name__, "TestData/problem.graphml"))


def test_all_paths(graph):
    find_paths.get_all_paths_from_cabinet_to_nodes(graph)