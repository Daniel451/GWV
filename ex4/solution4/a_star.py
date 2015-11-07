import networkx as nx

class GWV_a_star:
    def __init__(self, G):
        """
        :param G:
        :type G: nx.Graph
        """

        self.__G = G

        # set of already evaluated nodes
        self.__closed_set = set()

        # set of nodes to be evaluated
        self.__open_set = set()
        self.__open_set.add(self.__G.graph["start"])

        # dict of navigated nodes
        self.__came_from = dict()

        # dict of costs (for a certain path to a node - actual edge cost)
        self.__g_score = dict()

        # dict of costs (total estimated costs)
        self.__f_score = dict()


    def run_algorithm(self):
        # loop while the open set is not empty
        while len(self.__open_set) > 0:
            pass


    def h(self, node):
        row1, col1 = node  # unpack row and col from tuple node
        row2, col2 = self.__G.graph["goal"]  # unpack row and col from tuple goal

        # this simply returns the total amount of edges from node to goal
        return abs(row1 - row2) + abs(col1 - col2)


    def __get_node_with_lowest_fscore(self):
        pass

