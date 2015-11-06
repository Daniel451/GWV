#!/usr/bin/env python

import networkx as nx
import numpy as np
from matplotlib import pyplot as plt
from readfile import GWV_reader

# create an empty graph
G = nx.Graph()

####################################
# read and traverse the input file #
####################################
filepath = "test_env_2.txt"


GWVR = GWV_reader(G, filepath)