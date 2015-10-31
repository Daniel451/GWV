from collections import deque
from graph_class import UnweightedUndirectedGraph
import matplotlib.pyplot as plt
import time


__author__ = 'daniel'


class search_BFS:

    def __init__(self, node_start, node_goal, graph, delay):
        """
        :param node_start: start node
        :param node_goal: goal node to search for
        :param graph: a Graph
        :type graph: UnweightedUndirectedGraph
        """
        self.G = graph
        self.visited = set()
        self.queue = deque()
        self.start = node_start
        self.goal = node_goal
        self.queue.append(self.start)
        self.delay = delay

        # plotting
        self.f, self.axarr = plt.subplots(1, 1, sharex=False, sharey=False)


    def run_algorithm(self):

        while len(self.queue) > 0:
            #print("queue: {}".format(self.queue))
            #print("visited: {}").format(self.visited)

            current_node = self.queue.popleft()
            self.visited.add(current_node)

            if self.G.get_label(current_node) not in ["g", "s"]:
                self.G.set_label(current_node, "r")

            neighbors = self.G.get_neighbors(current_node)

            if current_node == self.goal or self.goal in neighbors:
                # goal handler -> return true because goal is found
                self.plot(current_node)
                break

            while len(neighbors) > 0:
                neighbor = neighbors.pop()
                if neighbor not in self.queue and neighbor not in self.visited:
                    self.queue.append(neighbor)
                    if self.G.get_label(neighbor) not in ["g", "s", "x", "v", "r"]:
                        self.G.set_label(neighbor, "q")

            # delay settings
            if self.delay == "0":
                bla = raw_input("press any key to continue...")
            elif self.delay == "1":
                time.sleep(1.0)
            elif self.delay == "2":
                time.sleep(0.5)

            # plotting
            self.plot(current_node)

            # label current robot node to visited so that a new node can become the robot's position
            if self.G.get_label(current_node) not in ["g", "s"]:
                self.G.set_label(current_node, "v")

        # pause the animation
        plt.show(block=True)


    def plot(self, current_node):
        """
        Only for visualization.

        :param current_node:
        :return:
        """
        self.axarr.clear()
        self.axarr.set_title("Breadth-First-Search")
        self.axarr.imshow(self.G.get_representations_array(), interpolation = "none")

        plt.xticks(range(0, self.G.get_representation_dimensions()[1]))
        plt.yticks(range(0, self.G.get_representation_dimensions()[0]))

        queue = list(self.queue)

        line1 = "Robot position: {}".format(current_node)
        line2 = "Queue nodes (first 6) : {}".format(queue[0:6])
        line3 = "Queue nodes (last 6)  : {}".format(queue[-6:])

        plot_text = "{}\n{}\n{}".format(line1, line2, line3)
        plt.text(0.0, self.G.get_representation_dimensions()[0] + 1.0,
                 plot_text, size=12, horizontalalignment='left', verticalalignment='top')

        plt.draw()
        plt.pause(0.01)

