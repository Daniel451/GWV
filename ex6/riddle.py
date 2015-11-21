from collections import OrderedDict

words = ["add", "ado", "age", "ago", "aid", "ail", "aim", "air",
"and", "any", "ape", "apt", "arc", "are", "ark", "arm",
"art", "ash", "ask", "auk", "awe", "awl", "aye", "bad",
"bag", "ban", "bat", "bee", "boa", "ear", "eel", "eft",
"far", "fat", "fit", "lee", "oaf", "rat", "tar", "tie"]


class Crosswords:
    def __init__(self, words):
        # variables
        self.A1D1 = set()
        self.A1D2 = set()
        self.A1D3 = set()

        self.A2D1 = set()
        self.A2D2 = set()
        self.A2D3 = set()

        self.A3D1 = set()
        self.A3D2 = set()
        self.A3D3 = set()

        # variable dict
        self.variables = OrderedDict()
        self.variables["A1D1"] = self.A1D1
        self.variables["A1D2"] = self.A1D2
        self.variables["A1D3"] = self.A1D3

        self.variables["A2D1"] = self.A2D1
        self.variables["A2D2"] = self.A2D2
        self.variables["A2D3"] = self.A2D3

        self.variables["A3D1"] = self.A3D1
        self.variables["A3D2"] = self.A3D2
        self.variables["A3D3"] = self.A3D3

        # rows
        self.rows = OrderedDict()
        self.rows["A1"] = [self.A1D1, self.A1D2, self.A1D3]
        self.rows["A2"] = [self.A2D1, self.A2D2, self.A2D3]
        self.rows["A3"] = [self.A3D1, self.A3D2, self.A3D3]

        # cols
        self.cols = OrderedDict()
        self.cols["D1"] = [self.A1D1, self.A2D1, self.A3D1]
        self.cols["D2"] = [self.A1D2, self.A2D2, self.A3D2]
        self.cols["D3"] = [self.A1D3, self.A2D3, self.A3D3]

        # character set
        self.characters = set()

        # valid words
        self.words = words

        # set for start, mid and end characters
        self.start_chars = set()
        self.mid_chars = set()
        self.end_chars = set()

        # get all valid characters
        for word in words:
            self.characters.update([character for character in word])
            self.start_chars.update(word[0])
            self.mid_chars.update(word[1])
            self.end_chars.update(word[-1])

        # initialize the sets
        for key in self.variables:
            self.variables[key].update(self.characters)


    def domain_consistency(self):

        # start chars
        self.variables["A1D1"].intersection_update(self.start_chars)
        self.variables["A1D2"].intersection_update(self.start_chars)
        self.variables["A1D3"].intersection_update(self.start_chars)

        self.variables["A2D1"].intersection_update(self.start_chars)
        self.variables["A3D1"].intersection_update(self.start_chars)

        # mid chars
        self.variables["A2D1"].intersection_update(self.mid_chars)
        self.variables["A2D2"].intersection_update(self.mid_chars)
        self.variables["A2D3"].intersection_update(self.mid_chars)

        self.variables["A1D2"].intersection_update(self.mid_chars)
        self.variables["A3D2"].intersection_update(self.mid_chars)

        # end chars
        self.variables["A1D3"].intersection_update(self.end_chars)
        self.variables["A2D3"].intersection_update(self.end_chars)
        self.variables["A3D3"].intersection_update(self.end_chars)

        self.variables["A3D1"].intersection_update(self.end_chars)
        self.variables["A3D2"].intersection_update(self.end_chars)


    def get_variable(self, str_id):
        return self.variables[str_id]


    def get_row(self, str_id):
        return self.rows[str_id]


    def get_col(self, str_id):
        return self.cols[str_id]


    def get_representation(self):

        ssize = 0

        # get maximum size of one set
        for cset in self.variables.itervalues():
            if ssize < len(cset):
                ssize = len(cset)

        linebuffer = ""

        for i, key, cset in zip(range(1, len(self.variables)+1),
                                self.variables.iterkeys(),
                                self.variables.itervalues()):

            linebuffer += str(key) + ": "

            setbuffer = ""
            for elem in cset:
                setbuffer += str(elem) + " "
            linebuffer += setbuffer.ljust(ssize*2+2, " ")


            if i % 3 == 0:
                linebuffer += "\n"
                print(linebuffer)
                linebuffer = ""



C = Crosswords(words)

print ("\nBeginning:\n")
C.get_representation()
print("\n")

C.domain_consistency()

print("After domain consistency (start, mid and end chars evaluated):\n")
C.get_representation()
print("\n")

