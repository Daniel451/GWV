import networkx as nx
import curses


class GWV_screen:
    def __init__(self):
        # create a default screen
        self.stdscr = curses.initscr()


    def reset_shell(self):
        curses.reset_shell_mode()


    def add_str_to_scr(self, a_str):
        self.stdscr.addstr(a_str)


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

        for i_row in xrange(0, G.graph["rows"]):
            for i_column in xrange(0, G.graph["columns"]):
                self.add_str_to_scr(G.node[(i_row, i_column)]["field"])
            self.add_str_to_scr("\n")

        self.refresh_screen()
