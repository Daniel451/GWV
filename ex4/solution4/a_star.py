from screen import GWV_screen
import networkx as nx
import time

class GWV_a_star:
    def __init__(self, G, GWVS):
        """
        :param G:
        :type G: nx.Graph

        :param GWVS:
        :type GWVS: GWV_screen
        """

        self.__G = G
        self.__GWVS = GWVS

        self.wait_time = 0.05

        # set of already evaluated nodes
        self.__closed_set = set()

        # set of nodes to be evaluated
        self.__open_set = set()
        self.__open_set.add(self.__G.graph["start"])

        # dict of navigated nodes
        self.__came_from = dict()

        # dict of costs (for a certain path to a node - actual edge cost)
        self.__g_score = dict()
        self.__g_score[self.__G.graph["start"]] = 0

        # dict of costs (total estimated costs)
        self.__f_score = dict()
        self.__f_score[self.__G.graph["start"]] = self.__g_score[self.__G.graph["start"]]\
                                                  + self.__h(self.__G.graph["start"])

        # set initial cost for every node very high
        for node in self.__G.nodes():
            if node != self.__G.graph["start"]:
                self.__g_score[node] = 99999999
                self.__f_score[node] = 99999999


    def run_algorithm(self):

        last_current = None

        # loop while the open set is not empty
        while len(self.__open_set) > 0:
            # plot
            self.__GWVS.plot_graph(self.__G)
            time.sleep(self.wait_time)

            # get current node -> node with the lowest f score
            current = self.__get_node_with_lowest_fscore()
            self.__G.graph["robot_position"] = current

            # for first iteration only
            if last_current is None:
                last_current = current


            # check if goal node is found
            if current == self.__G.graph["goal"] or self.__G.graph["goal"] in self.__open_set:
                time.sleep(1)
                self.__return_path_to_goal(current)
                break

            # remove current node from open set
            self.__open_set.remove(current)
            # add current node to closed set
            self.__closed_set.add(current)

            # update Graph
            self.__G.graph["open_set"] = self.__open_set
            self.__G.graph["closed_set"] = self.__closed_set
            self.__GWVS.plot_graph(self.__G)

            # get the neighbors of current node
            neighbors = self.__G.neighbors(current)

            # loop over the neighbors of current node
            for neighbor in neighbors:
                # if already processed, skip this loop
                if neighbor in self.__closed_set:
                    continue

                # calc g score for neighbor
                g_score_neighbor = self.__g_score[current] + self.__G.edge[current][neighbor]["costs"]

                # check if neighbor node is already discovered
                if neighbor not in self.__open_set:
                    self.__open_set.add(neighbor)
                    self.__relabel_node_field(neighbor, "+")
                    self.__GWVS.plot_graph(self.__G)
                    time.sleep(self.wait_time)
                # check if this path is too expansive (g costs) compared to a previously found path
                elif g_score_neighbor >= self.__g_score[neighbor]:
                    continue

                # new (cheaper (g costs)) path found
                self.__came_from[neighbor] = current
                self.__g_score[neighbor] = g_score_neighbor
                self.__f_score[neighbor] = g_score_neighbor + self.__h(neighbor)

            # reset last_current
            last_current = current
            self.__relabel_node_field(last_current, "*")
            self.__GWVS.plot_graph(self.__G)


    def __return_path_to_goal(self, current):
        goal_path = [current]
        predecessor = None

        while predecessor != self.__G.graph["start"]:
            predecessor = self.__came_from[current]
            goal_path.append(predecessor)
            current = predecessor

        for node in goal_path:
            self.__relabel_node_field(node, "#")

        self.__G.graph["goal_path"] = goal_path

        self.__GWVS.plot_graph(self.__G)



    def __relabel_node_field(self, node, new_label):
        if self.__G.node[node]["field"] not in ["g", "s", "x", "1", "2"]:
            self.__G.node[node]["field"] = new_label


    def __h(self, node):
        row1, col1 = node  # unpack row and col from tuple node
        row2, col2 = self.__G.graph["goal"]  # unpack row and col from tuple goal

        # this simply returns the total amount of edges from node to goal
        # since the amount of edges equals the delta of rows + delta of columns
        # from node to goal
        return abs(row1 - row2) + abs(col1 - col2)


    def __get_node_with_lowest_fscore(self):
        return reduce(lambda node1, node2:
                      node1
                      if self.__f_score[node1] < self.__f_score[node2]
                      else
                      node2,
                      filter(lambda node: node in self.__open_set, self.__f_score))

