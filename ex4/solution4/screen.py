import networkx as nx
import curses


class GWV_screen:
    def __init__(self):
        # create a default screen
        self.stdscr = curses.initscr()

        # start coloring
        curses.start_color()
        curses.use_default_colors()

        # define colors
        curses.init_pair(1, curses.COLOR_RED, -1)
        curses.init_pair(2, curses.COLOR_YELLOW, -1)
        curses.init_pair(3, curses.COLOR_MAGENTA, -1)
        curses.init_pair(4, curses.COLOR_GREEN, -1)
        curses.init_pair(5, curses.COLOR_BLUE, -1)
        curses.init_pair(6, curses.COLOR_BLACK, curses.COLOR_WHITE)
        curses.init_pair(7, curses.COLOR_WHITE, -1)
        curses.init_pair(8, curses.COLOR_CYAN, -1)


    def reset_shell(self):
        curses.reset_shell_mode()


    def add_str_to_scr(self, a_str, colorpair = 7):
        self.stdscr.addstr(str(a_str), curses.color_pair(colorpair))


    def clear_screen(self):
        self.stdscr.clear()


    def refresh_screen(self):
        self.stdscr.refresh()


    def get_user_input(self):
        return chr(self.stdscr.getch())


    def plot_graph(self, G):
        """
        :param G: A non-empty nx.Graph object
        :type G: nx.Graph
        """
        self.clear_screen()

        self.add_str_to_scr("################################################"
                            +"############################################\n")
        self.add_str_to_scr("### legend   --->   ")

        # legend: start
        self.add_str_to_scr("s", 2)
        self.add_str_to_scr(": start node | ")

        # legend: goal
        self.add_str_to_scr("g", 4)
        self.add_str_to_scr(": goal node | ")

        # legend: closed set
        self.add_str_to_scr("*", 1)
        self.add_str_to_scr(": closed set | ")

        # legend: open set
        self.add_str_to_scr("+", 8)
        self.add_str_to_scr(": open set | ")

        # legend: wall
        self.add_str_to_scr("x")
        self.add_str_to_scr(": wall ###\n")

        self.add_str_to_scr("#################################################"
                            +"###########################################\n\n")

        self.add_str_to_scr("robot position: {}\n".format(G.graph["robot_position"]))
        self.add_str_to_scr("open set: {}\n".format(sorted(G.graph["open_set"])))
        #self.add_str_to_scr("closed set: {}\n\n".format(sorted(G.graph["closed_set"])))

        self.add_str_to_scr("\n")

        self.add_str_to_scr("row\n")

        for i_row in xrange(0, G.graph["rows"]):

            self.add_str_to_scr("[{:2}] ".format(i_row))

            for i_column in xrange(0, G.graph["columns"]):
                cell = G.node[(i_row, i_column)]["field"]
                if cell == "s":
                    self.add_str_to_scr(cell, 2)
                elif cell == "g":
                    self.add_str_to_scr(cell, 4)
                elif cell == "*":
                    self.add_str_to_scr(cell, 1)
                elif cell == "+":
                    self.add_str_to_scr(cell, 8)
                elif cell == "#":
                    self.add_str_to_scr(cell, 3)
                else:
                    self.add_str_to_scr(cell)
            self.add_str_to_scr("\n")

        if len(G.graph["goal_path"]) > 0:
            self.add_str_to_scr("Path to goal was found!\n\n")
            self.add_str_to_scr("Goal path: ")
            for i, node in zip(range(0, len(G.graph["goal_path"])), reversed(G.graph["goal_path"])):
                if i != len(G.graph["goal_path"]) - 1:
                    self.add_str_to_scr("{} -> ".format(node))
                else:
                    self.add_str_to_scr(node)
            self.add_str_to_scr("\n")

        self.refresh_screen()
