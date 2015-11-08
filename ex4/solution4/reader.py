import networkx as nx

class GWV_reader:
    """
    GWV_reader reads a textfile, parses it's contents and manipulates the given
    graph mostly in-place. Therefore nothing is returned but edited direclty.
    The result is full graph containing all nodes and edges depending on the file's
    contents.
    """

    def __init__(self, G, filepath):
        """
        Constructor.

        :param G: an empty networkx Graph
        :type G: nx.Graph

        :param filepath: path to the file
        :type filepath: str
        """
        # file variables
        self.__filepath = filepath  # file's path
        self.__fdata = None  # file's contents
        self.__columns = 0  # max amount of columns in any line of file's contents
        self.__rows = 0  # amount of row in file's contents

        # graph
        self.__G = G  # graph class

        # read the file's contents
        self.__read_file_data()

        # parse the file's contents
        self.__parse_file_data()


    def __read_file_data(self):
        # open file and read lines
        with open(self.__filepath) as f:
            self.__fdata = f.readlines()


    def __parse_file_data(self):
        # delete \n in every line
        self.__fdata = map(lambda line: line.replace("\n", ""), self.__fdata)

        # get dimensions
        self.__columns = max(map(lambda line: len(line), self.__fdata))  # get the maximum x dimension
        self.__rows = len(self.__fdata)  # get the maximum y dimension

        # set the dimensions as an attribute of graph G
        self.__G.graph["columns"] = self.__columns
        self.__G.graph["rows"] = self.__rows

        # set sets
        self.__G.graph["open_set"] = set()
        self.__G.graph["closed_set"] = set()

        ####################
        # create the nodes #
        ####################
        for row in xrange(0, self.__rows):  # iterate over the rows
            for column in xrange(0, self.__columns):  # iterate over the columns
                self.__G.add_node((row, column))  # adds the node to the graph
                                                  # node identifieres are tuples
                                                  # like (1, 2) for the node at row 1, column 2
                self.__G.node[(row, column)]["field"] = self.__fdata[row][column]

                # save start and end node
                if self.__G.node[(row, column)]["field"] == "s":
                    self.__G.graph["start"] = (row, column)
                    self.__G.graph["robot_position"] = (row, column)
                elif self.__G.node[(row, column)]["field"] == "g":
                    self.__G.graph["goal"] = (row, column)


        ####################
        # create the edges #
        ####################
        for row in xrange(1, self.__rows-1):  # iterate over the field's rows (without the outer walls)
            for column in xrange(1, self.__columns-1): # iterate over the field's columns (without outer walls)

                # if current node is a wall, skip this node
                if self.__G.node[(row, column)]["field"] == "x":
                    continue

                # check field above for connectivity
                if self.__G.node[(row-1, column)]["field"] != "x":  # is the node above not a wall?
                    self.__G.add_edge((row, column), (row-1, column))  # ..then add an edge..
                    self.__G.edge[(row, column)][(row-1, column)]["costs"] = 1  # ..and costs

                # check field under for connectivity
                if self.__G.node[(row+1, column)]["field"] != "x":  # is the node under not a wall?
                    self.__G.add_edge((row, column), (row+1, column))  # ..then add an edge..
                    self.__G.edge[(row, column)][(row+1, column)]["costs"] = 1  # ..and costs

                # check field left for connectivity
                if self.__G.node[(row, column-1)]["field"] != "x":  # is the node left not a wall?
                    self.__G.add_edge((row, column), (row, column-1))  # ..then add an edge..
                    self.__G.edge[(row, column)][(row, column-1)]["costs"] = 1  # ..and costs

                # check field right for connectivity
                if self.__G.node[(row, column+1)]["field"] != "x":  # is the node right not a wall?
                    self.__G.add_edge((row, column), (row, column+1))  # ..then add an edge..
                    self.__G.edge[(row, column)][(row, column+1)]["costs"] = 1  # ..and costs