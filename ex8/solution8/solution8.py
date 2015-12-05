#!/usr/bin/env python

from markov import Markov

mm = Markov("heiseticker-text.txt")


print("###############")
print("### bigrams ###")
print("###############")

print("Markov chain text of size {}:\n{}\n".format(10, mm.generate_markov_text_bigrams(10)))
print("Markov chain text of size {}:\n{}\n".format(20, mm.generate_markov_text_bigrams(20)))
print("Markov chain text of size {}:\n{}\n".format(30, mm.generate_markov_text_bigrams(30)))
print("Markov chain text of size {}:\n{}\n".format(40, mm.generate_markov_text_bigrams(40)))

print("################")
print("### trigrams ###")
print("################")

print("Markov chain text of size {}:\n{}\n".format(10, mm.generate_markov_text_trigrams(10)))
print("Markov chain text of size {}:\n{}\n".format(20, mm.generate_markov_text_trigrams(20)))
print("Markov chain text of size {}:\n{}\n".format(30, mm.generate_markov_text_trigrams(30)))
print("Markov chain text of size {}:\n{}\n".format(40, mm.generate_markov_text_trigrams(40)))

print("###################")
print("### quadrograms ###")
print("###################")

print("Markov chain text of size {}:\n{}\n".format(10, mm.generate_markov_text_quadrograms(10)))
print("Markov chain text of size {}:\n{}\n".format(20, mm.generate_markov_text_quadrograms(20)))
print("Markov chain text of size {}:\n{}\n".format(30, mm.generate_markov_text_quadrograms(30)))
print("Markov chain text of size {}:\n{}\n".format(40, mm.generate_markov_text_quadrograms(40)))