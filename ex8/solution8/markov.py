#!/usr/bin/env python

from itertools import ifilter
import random
import numpy as np


class Markov(object):
    def __init__(self, filepath):
        """
        Constructor
        """
        # set of valid characters
        self.validchars = set()
        self.gen_valid_chars()

        # path to the file containing the text
        self.filepath = filepath

        # extracted and filtered words (out of the given file)
        self.words = self.read_words_from_file()

        # total amount of words
        self.len_of_words = len(self.words)

        self.keys_bigrams = {}
        self.database_bigrams()

        self.keys_trigrams = {}
        self.database_trigrams()

        self.keys_quadrograms = {}
        self.database_quadrograms()


    def gen_valid_chars(self):
        """
        Creates a set of valid characters
        (all words starting or ending with non-valid characters are filtered)
        """
        # characters a - z
        for i in xrange(0, 26):
            self.validchars.add(chr(ord("a") + i))

        # characters A - Z
        for i in xrange(0, 26):
            self.validchars.add(chr(ord("A") + i))

        # numbers 0 - 9
        for i in xrange(0, 10):
            self.validchars.add(str(i))


    def read_words_from_file(self):
        """
        Extract all words out of a given file
        """
        with open(self.filepath, "r") as f:
            str_filter = ifilter(lambda x:
                                 True if (x.strip()[0] in self.validchars
                                          or x.strip()[-1] in self.validchars)
                                 else False, f)
            gentxt = np.genfromtxt(str_filter, dtype=np.str, delimiter="\n", autostrip=True)

        return gentxt


    def bigrams(self):
        """
        bigram generator
        """
        for i in xrange(len(self.words) - 1):
            yield (self.words[i], self.words[i + 1])


    def trigrams(self):
        """
        trigram generator
        """
        for i in xrange(len(self.words) - 2):
            yield (self.words[i], self.words[i + 1], self.words[i + 2])


    def quadrograms(self):
        """
        quadrogram generator
        """
        for i in xrange(len(self.words) - 3):
            yield (self.words[i], self.words[i + 1], self.words[i + 2], self.words[i + 3])


    def database_bigrams(self):
        """
        build up bigram database
        """
        for w1, w2 in self.bigrams():
            key = w1
            if key in self.keys_bigrams:
                self.keys_bigrams[key].append(w2)
            else:
                self.keys_bigrams[key] = [w2]


    def database_trigrams(self):
        """
        build up trigram database
        """
        for w1, w2, w3 in self.trigrams():
            key = (w1, w2)
            if key in self.keys_trigrams:
                self.keys_trigrams[key].append(w3)
            else:
                self.keys_trigrams[key] = [w3]


    def database_quadrograms(self):
        """
        build up quadrogram database
        """
        for w1, w2, w3, w4 in self.quadrograms():
            key = (w1, w2, w3)
            if key in self.keys_quadrograms:
                self.keys_quadrograms[key].append(w4)
            else:
                self.keys_quadrograms[key] = [w4]


    def generate_markov_text_bigrams(self, size=25):
        """
        Generates a sequence of words via a markov chain (bigrams) with variable size
        """
        seed = random.randint(0, self.len_of_words - 2)
        start_word = self.words[seed]
        w1 = start_word
        wordlist = []
        for i in xrange(size):
            wordlist.append(w1)
            w1 = random.choice(self.keys_bigrams[w1])
        return " ".join(wordlist)


    def generate_markov_text_trigrams(self, size=25):
        """
        Generates a sequence of words via a markov chain (trigrams) with variable size
        """
        seed = random.randint(0, self.len_of_words - 3)
        start_word, next_word = self.words[seed], self.words[seed + 1]
        w1, w2 = start_word, next_word
        wordlist = []
        for i in xrange(size):
            wordlist.append(w1)
            w1, w2 = w2, random.choice(self.keys_trigrams[(w1, w2)])
        wordlist.append(w2)
        return " ".join(wordlist)


    def generate_markov_text_quadrograms(self, size=25):
        """
        Generates a sequence of words via a markov chain (quadrograms) with variable size
        """
        seed = random.randint(0, self.len_of_words - 4)
        start_word, next_word, next_next_word = self.words[seed], self.words[seed + 1], self.words[seed + 2]
        w1, w2, w3 = start_word, next_word, next_next_word
        wordlist = []
        for i in xrange(size):
            wordlist.append(w1)
            w1, w2, w3 = w2, w3, random.choice(self.keys_quadrograms[(w1, w2, w3)])
        wordlist.append(w2)
        return " ".join(wordlist)
