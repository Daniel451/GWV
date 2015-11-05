import networkx as nx
import numpy as np


# create an empty graph
G = nx.Graph()

####################################
# read and traverse the input file #
####################################
filepath = "test_env_2.txt"

# open file and read lines
with open(filepath) as f:
    fdata = f.readlines()

# delete \n in every line
fdata = map(lambda line: line.replace("\n", ""), fdata)

# get dimensions
columns_count = max(map(lambda line: len(line), fdata))  # get the maximum x dimension
rows_count = len(fdata)  # get the maximum y dimension

# container array
rep_arr = np.zeros((rows_count, columns_count), dtype="str")

# create the nodes
for row in xrange(0, rows_count):
    for column in xrange(0, columns_count):
        G.add_node((row, column))
        rep_arr[row][column] = fdata[row][column]

# create the edges
for row in xrange(1, rows_count-1):
    for column in xrange(1, columns_count-1):
        # check field above
        if rep_arr[row-1][column] != "x":
            pass
