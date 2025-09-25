import unittest
from GraphePython import Graph

class GraphePythonOptimisation(unittest.TestCase) :
    def test_get_center(self) :
        self.graph = Graph
        self.graph.generate_random_graph(50, 150, (0, 25), integer=True)
        self.graph.save_graph("testGraph.txt")