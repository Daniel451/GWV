from graph_class import UnweightedUndirectedGraph
from BFS import search_BFS
from DFS import search_DFS

__author__ = 'daniel'


############################################
### read the file and get a graph object ###
############################################

with open("blatt3_environment.txt") as f:
    fdata = f.readlines()

# delete \n in every line
fdata = map(lambda line: line.replace("\n", ""), fdata)

# get a graph object of our graph class
G = UnweightedUndirectedGraph()

x_dimension = max(map(lambda line: len(line), fdata))  # get the maximum x dimension
y_dimension = len(fdata)  # get the maximum y dimension
G.set_representation_dimensions((y_dimension, x_dimension))  # save the dimension tuple


############################################
### add the nodes and edges to the graph ###
############################################

start_node = ""
goal_node = ""

# add the nodes
# iterates over every line
for i_line in xrange(0, len(fdata)):

    # iterates over every element in a line
    for i_elem in xrange(0, len(fdata[i_line])):
        node_id = "({},{})".format(i_line, i_elem)
        label = fdata[i_line][i_elem]

        # add the node to the graph
        G.add_node(node_id)

        # add a label to the node
        G.set_label(node_id, label)

        if label == "s":
            start_node = node_id
        elif label == "g":
            goal_node = node_id



# add the edges
# iterates over every line
for i_line in xrange(0, len(fdata)):

    # iterates over every element in a line
    for i_elem in xrange(0, len(fdata[i_line])):

        node_id = "({},{})".format(i_line, i_elem)
        label = fdata[i_line][i_elem]

        # only process node if it is no cross (wall)
        if label != "x":

            # the neighbors of current node in fdata
            top = "({},{})".format(i_line - 1, i_elem)
            bottom = "({},{})".format(i_line + 1, i_elem)
            left = "({},{})".format(i_line, i_elem - 1)
            right = "({},{})".format(i_line, i_elem + 1)

            if G.get_label(top) != "x" and not G.has_edge((node_id, top)):
                G.add_edge((node_id, top))

            if G.get_label(bottom) != "x" and not G.has_edge((node_id, bottom)):
                G.add_edge((node_id, bottom))

            if G.get_label(left) != "x" and not G.has_edge((node_id, left)):
                G.add_edge((node_id, left))

            if G.get_label(right) != "x" and not G.has_edge((node_id, right)):
                G.add_edge((node_id, right))


#####################
### startup stuff ###
#####################

print("#############")
print("### setup ###")
print("#############")

print("\nPlease enter a number for the algorithm you want to see:\n")
print("  [0] Breadth-First-Search")
print("  [1] Depth-First-Search")

user_input = raw_input("\nChoose 0, 1: ")

if user_input in ["0", "1"]:
    algorithm = user_input
else:
    print("\nThis was not a number fulfilling 0 <= number <= 1. Exiting...\n")
    exit()

print("\nPlease enter a number whether you want the animation to be:\n")
print("  [0] waiting for user to press enter continuously")
print("  [1] very slow (1.0 seconds between every step)")
print("  [2] slow      (0.5 seconds between every step)")
print("  [3] fast      (no delay at all)")

user_input = raw_input("\nChoose 0, 1, 2, or 3: ")

if user_input in ["0", "1", "2", "3"]:
    delay = user_input
else:
    print("\nThis was not a number fulfilling 0 <= number <= 3. Exiting...\n")
    exit()


#######################
### start algorithm ###
#######################

if algorithm == "0":
    BFS = search_BFS(start_node, goal_node, G, delay)
    BFS.run_algorithm()
elif algorithm == "1":
    DFS = search_DFS(start_node, goal_node, G, delay)
    DFS.run_algorithm()