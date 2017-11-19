import os, sys
import traceback
from networkx.readwrite import read_graphml
from xml.etree.ElementTree import ParseError
import json


def load_graph(datafile, dataformat="graphml"):
    """This attempts to load the data in the given file and
    returns either the loaded graph or raises an exception

    :param datafile: The path of the file to load
    :param dataformat: The format expected from the file, currently
                       only "graphml" supported
    """
    if not os.path.exists(datafile):
        print("File doesn't exist. Please check the given path")
        raise IOError
    try:
        if dataformat == "graphml":
            return read_graphml(datafile)
        else:
            print("File format {} not currently supported".format(dataformat))
            raise NotImplementedError
    except ParseError as e:
        print("Not a graphml file or file unreadable\n")
        raise


def load_rate_cards(rate_card_datafile):
    """This attempts to load in the rates
    :param rate_card_datafile: The path to the JSON file with the rate cards in
    :return: A list of rate cards
    """
    with open(rate_card_datafile, "r") as datafile:
        rate_cards = json.load(datafile)
    return rate_cards
