#!/usr/bin/env python

import time
import networkx as nx
from reader import GWV_reader
from screen import GWV_screen
from filelist import GWV_filelist

# create an empty graph
G = nx.Graph()

# scan the directory
GWVF = GWV_filelist()

# create the screen
GWVS = GWV_screen()


#####################
### select a file ###
#####################

GWVS.add_str_to_scr("Possible .txt files in the working directory are:\n\n")
filepath = None
valid_keys = []

for i, filestr in zip(range(0, len(GWVF.get_txt_files())), GWVF.get_txt_files()):
    valid_keys.append(str(i))
    GWVS.add_str_to_scr("[{}]: {}\n".format(i, filestr))

GWVS.add_str_to_scr("\nPlease select a file (0 to {}): ".format(len(GWVF.get_txt_files()) - 1))

GWVS.refresh_screen()

uinput = GWVS.get_user_input()

if uinput not in valid_keys:
    GWVS.clear_screen()
    GWVS.refresh_screen()
    print("\nThe input \"{}\" is not valid. Exiting...\n\n".format(uinput))
    exit()
else:
    filepath = GWVF.get_txt_files()[int(uinput)]


# inform the user
GWVS.clear_screen()
GWVS.add_str_to_scr("The file \"{}\" will be opened and parsed now.\n".format(filepath))
GWVS.refresh_screen()
time.sleep(1)
GWVS.clear_screen()

# create a GWV_reader object which reads and parses the given file
# and manipulates an empty graph (adds nodes and edges)
GWVR = GWV_reader(G, filepath)


# show the file
GWVS.plot_graph(G)


# finally
GWVS.add_str_to_scr("\nPress any key to exit...")
GWVS.refresh_screen()
GWVS.get_user_input()
GWVS.clear_screen()
GWVS.refresh_screen()
GWVS.reset_shell()