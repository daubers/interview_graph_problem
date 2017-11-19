Quick Costing Graph Pathing Program
===================================

This is a very quick bodge together of the awesome power of NetworkX and some glue to
do other data parsing stuff!

To run it! Either run the setup.py to install and then run "parse-graph" or python -m GraphParseCost.entry

The data for the costcards is layed out in tests/TestData/cost_cards.json

Tests can be run using tox, though I'll admit they're a bit sparse.

Docs are build with Sphinx, these are all autogenned from the docstrings. Again, a bit sparse, sorry.

Things I would have liked to have done but haven't:

* Being able to give it a start and end on a graph and to find its way
* Dealing with loops (this might break /hard/ but I haven't tested it)
* Break out the thing that does cost calculations into a full class rather than a function, or make it act like a set of filters things just drop through to turn into numbers
* Tidying up variable names. The costing thing really needs this bad.
* HTML output with whizzy path graphs

