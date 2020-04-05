

import string
import random
import numpy as np

# create substitution cipher
# one will work as key, another will be the value
letters1 = list(string.ascii_lowercase)
letters2 = list(string.ascii_lowercase)

truemapping = {}

random.shuffle(letters2)

for k, v in zip(letters1, letters2):
    truemapping[k] = v

# the language model
# initialize Markov matrix
M = np.ones((26, 26))

# initial state distribution
pi = np.zeros(26)


# a function to update the Markov model
def update_transition(ch1, ch2):
    #ord('a') == 97, ord('b') == 98 ....
    i = ord(ch1) - 97
    j = ord(ch2) - 97
    M[i,j] += 1