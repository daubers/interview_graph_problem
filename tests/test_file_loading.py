import pkg_resources
import pytest
from GraphParseCost import load
from xml.etree.ElementTree import ParseError

def test_graphml_loads():
    print(load.load_graph(pkg_resources.resource_filename(__name__, "TestData/problem.graphml")).__dict__)


def test_graphml_missing_files():
    with pytest.raises(IOError):
        load.load_graph("This_file_doesnt_exist")


def test_bad_graphml():
    with pytest.raises(ParseError):
        load.load_graph(pkg_resources.resource_filename(__name__, "TestData/bad_problem.graphml"))
