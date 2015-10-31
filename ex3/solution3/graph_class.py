from collections import deque
import numpy as np


class UnweightedUndirectedGraph:
    def __init__(self):
        self.nodes = set()  # a set of nodes, e.g.: set("a", "b", "c", ...)
        self.edges = set()  # a set of edges, e.g.: set( (a, a), (a, b), (c, d), ... )
        self.labels = dict()  # labels for nodes

        # representation stuff
        self.representation = dict()  # dictionary of every node with it's coordinates
        self.representation_dimensions = (0, 0)  # tuple of x and y dimensions
        self.visited = (1.0, 0, 0)  # color: red (for visited nodes)
        self.start = (0.65, 0, 0.7)  # color: purple (for the start nodes)
        self.goal = (0, 0.8, 0)  # color: green (for goal nodes)
        self.queue = (0.9, 0.55, 0)  # color: orange (for nodes currently in the queue)
        self.wall = (0.0, 0.0, 0.0)  # color: black (for wall nodes)
        self.robot = (0.0, 1.0, 1.0)  # color: teal (current robot position)
        self.normal_field = (1.0, 1.0, 1.0)  # color: white (for normal fields)



    def set_representation_dimensions(self, dtuple):
        # assertions
        assert type(dtuple) is tuple, "the type of node_tuple has to be tuple."
        assert len(dtuple) == 2, "the length of node_tuple has to be 2 but was {0}".format(len(dtuple))

        self.representation_dimensions = dtuple

    def get_representation_dimensions(self):
        return self.representation_dimensions

    def add_node(self, node):
        # assertions
        assert type(node) is str or type(node) is int, "the type of node has to be str or int."
        assert node not in self.nodes, "the node {0} already exists.".format(node)

        # add node to set
        self.nodes.add(node)

    def add_edge(self, node_tuple):
        # assertions
        assert type(node_tuple) is tuple, "the type of node_tuple has to be tuple."
        assert len(node_tuple) == 2, "the length of node_tuple has to be 2 but was {0}".format(len(node_tuple))

        # prevent having (a, b) and (b, a) in the edges by sorting the tuple first
        node_tuple = tuple(sorted(node_tuple))

        # check if edge already exists
        assert node_tuple not in self.edges, "the edge {0} already exists.".format(node_tuple)

        # add edge to set
        self.edges.add(node_tuple)

    def del_node(self, node):
        # assertions
        assert type(node) is str or type(node) is int, "the type of node has to be str or int."
        assert node in self.nodes, "the node {0} does not exist.".format(node)

        # delete node
        self.nodes.remove(node)

    def del_edge(self, node_tuple):
        # assertions
        assert type(node_tuple) is tuple, "the type of node_tuple has to be tuple."
        assert len(node_tuple) == 2, "the length of node_tuple has to be 2 but was {0}".format(len(node_tuple))

        # sort the tuple
        node_tuple = tuple(sorted(node_tuple))

        # check if edge exists
        assert node_tuple in self.edges, "the edge {0} does not exist.".format(node_tuple)

        # delete edge
        self.edges.remove(node_tuple)

    def set_label(self, node, label):
        # assertions
        assert type(node) is str or type(node) is int, "the type of node has to be str or int."
        assert type(label) is str or type(label) is int, "the type of label has to be str or int."
        assert node in self.nodes, "the node {0} does not exist.".format(node)

        # set the label
        self.labels[node] = str(label)

    def get_label(self, node):
        # assertions
        assert type(node) is str or type(node) is int, "the type of node has to be str or int."
        assert node in self.nodes, "the node {0} does not exist.".format(node)

        # return the label or return an empty string
        if node in self.labels:
            return self.labels[node]
        else:
            return ""

    def has_node(self, node):
        # assertions
        assert type(node) is str or type(node) is int, "the type of node has to be str or int."

        # return if node exists
        return node in self.nodes

    def has_edge(self, node_tuple):
        # assertions
        assert type(node_tuple) is tuple, "the type of node_tuple has to be tuple."
        assert len(node_tuple) == 2, "the length of node_tuple has to be 2 but was {0}".format(len(node_tuple))

        # sort it first
        node_tuple = tuple(sorted(node_tuple))

        # return if edge exists
        return node_tuple in self.edges

    def get_all_nodes(self):
        return self.nodes

    def get_all_edges(self):
        return self.edges

    def get_all_labels(self):
        return self.labels

    def get_neighbors(self, node):
        # assertions
        assert type(node) is str or type(node) is int, "the type of node has to be str or int."
        assert node in self.nodes, "the node {0} does not exist.".format(node)

        neighbors = deque()

        # iterate over all edges
        for edge in self.edges:
            if edge[0] == node and edge[1] != node:
                neighbors.append(edge[1])  # append the neighbor if the tuple looks like (node, neighbor)
            elif edge[0] != node and edge[1] == node:
                neighbors.append(edge[0])  # append the neighbor if the tuple looks like (neighbor, node)

        return neighbors

    def get_representations(self):
        return self.representation

    def get_representations_array(self):
        # dimension -> (x-dimension, y-dimension, RGB value)
        dimension = (self.get_representation_dimensions()[0], self.get_representation_dimensions()[1], 3)
        container = np.zeros(len(self.nodes)*3).reshape(dimension)

        for x in range(0, self.get_representation_dimensions()[0]):
            for y in range(0, self.get_representation_dimensions()[1]):
                # set color
                if self.get_label("({},{})".format(x, y)) == "x":
                    container[x, y, 0] = self.wall[0]
                    container[x, y, 1] = self.wall[1]
                    container[x, y, 2] = self.wall[2]
                elif self.get_label("({},{})".format(x, y)) == "s":
                    container[x, y, 0] = self.start[0]
                    container[x, y, 1] = self.start[1]
                    container[x, y, 2] = self.start[2]
                elif self.get_label("({},{})".format(x, y)) == "g":
                    container[x, y, 0] = self.goal[0]
                    container[x, y, 1] = self.goal[1]
                    container[x, y, 2] = self.goal[2]
                elif self.get_label("({},{})".format(x, y)) == "v":
                    container[x, y, 0] = self.visited[0]
                    container[x, y, 1] = self.visited[1]
                    container[x, y, 2] = self.visited[2]
                elif self.get_label("({},{})".format(x, y)) == "q":
                    container[x, y, 0] = self.queue[0]
                    container[x, y, 1] = self.queue[1]
                    container[x, y, 2] = self.queue[2]
                elif self.get_label("({},{})".format(x, y)) == "r":
                    container[x, y, 0] = self.robot[0]
                    container[x, y, 1] = self.robot[1]
                    container[x, y, 2] = self.robot[2]
                elif self.get_label("({},{})".format(x, y)) == " ":
                    container[x, y, 0] = self.normal_field[0]
                    container[x, y, 1] = self.normal_field[1]
                    container[x, y, 2] = self.normal_field[2]

        return container

    def get_node_representation(self, node):
        # assertions
        assert type(node) is str or type(node) is int, "the type of node has to be str or int."
        assert node in self.nodes, "the node {0} does not exist.".format(node)
        assert node in self.representation, "the node {0} has no representation.".format(node)

        return self.representation[node]

    def set_one_representation(self, node, coords):
        # assertions
        assert type(node) is str or type(node) is int, "the type of node has to be str or int."
        assert node in self.nodes, "the node {0} does not exist.".format(node)
        assert type(coords) is tuple, "the type of coords has to be tuple."
        assert len(coords) == 2, "the length of coords has to be 2 but was {0}".format(len(coords))

        self.representation[node] = coords
