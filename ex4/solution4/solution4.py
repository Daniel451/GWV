#!/usr/bin/env python

import curses
import time
import networkx as nx
import numpy as np
from matplotlib import pyplot as plt
from readfile import GWV_reader
from plotter import GWV_plotter

# create an empty graph
G = nx.Graph()

# specify the path to the file
filepath = "test_env_2.txt"

# create a GWV_reader object which reads and parses the given file
# and manipulates an empty graph (adds nodes and edges)
GWVR = GWV_reader(G, filepath)


stdscr = curses.initscr()

stdscr.addstr("test text no 1\n")
stdscr.addstr("test text no 2\n")
stdscr.addstr("test text no 3\n")
stdscr.refresh()

stdscr.clear()

time.sleep(1)

stdscr.addstr("test text no 3\n")
stdscr.addstr("test text no 2\n")
stdscr.addstr("test text no 1\n")

stdscr.refresh()