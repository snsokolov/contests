#!/usr/bin/env python3
# envelopes.py - Envelopes program by Sergey 2017

import unittest
import random
import collections
import operator

###############################################################################
# Envelopes Class (Main Program)
###############################################################################


class Envelopes:
    """ Envelopes representation """

    def __init__(self, max, max_series):
        """ Default constructor """
        self.max = max
        self.max_series = max_series
        self.series = [self.gen() for _ in range(max_series)]
        self.matches = collections.defaultdict(list)

        for envelopes in self.series:
            self.matches[envelopes[0]].append(envelopes[1])
            self.matches[envelopes[1]].append(envelopes[0])

    def gen(self):
        rnd = random.randrange(self.max)
        envelopes = [rnd, rnd*2]
        random.shuffle(envelopes)
        return tuple(envelopes)

###############################################################################
# Unit Tests
###############################################################################


class unitTests(unittest.TestCase):

    def test_Envelopes_basic(self):
        """ Envelopes class testing """
        d = Envelopes(max=10, max_series=5)

        # Check that series are generated
        self.assertEqual(len(d.series), 5)

        # Make sure envelopes are generated correctly
        envelopes = d.gen()
        self.assertTrue(
            envelopes[0] == 2 * envelopes[1] or
            envelopes[1] == 2 * envelopes[0])

        # Check that array of matches is generated correctly
        self.assertTrue(d.series[0][1] in d.matches[d.series[0][0]])

    def test_Envelopes_series(self):

        for _ in range(5):
            d = Envelopes(max=100, max_series=10000)

            # Equity when not opening envelopes
            eno = (0, 0)
            # Equity when opening first envelope
            eo = (0, 0)

            num = 20

            for envelopes in d.series:
                eno = tuple(map(operator.add, eno, envelopes))
                if envelopes[0] == num:
                    eo = tuple(map(operator.add, eo, envelopes))

            print("Not opening: ", eno)
            print("Opening: ", eo)

if __name__ == "__main__":
    unittest.main(argv=[" "])
