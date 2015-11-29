#!/usr/bin/env python3
# 673A_BearSong.py - Topcoder.com by Sergey 2015

import unittest
import sys

###############################################################################
# BearSong Class (Main Program)
###############################################################################


class BearSong:
    """ BearSong representation """

    def __init__(self, test_inputs=None):
        """ Default constructor """
        self.test_inputs = test_inputs

    def countRareNotes(self, notes):

        d = {}
        for n in notes:
            d[n] = d.setdefault(n, 0) + 1
        return len([1 for k in d if d[k] == 1])

    def calculate(self):
        """ Main calcualtion function of the class """

        result = self.countRareNotes(self.test_inputs)

        return str(result)

###############################################################################
# Unit Tests
###############################################################################


class unitTests(unittest.TestCase):

    def test_single_test(self):
        """ BearSong class testing """

        # Constructor test
        test = (9, 10, 7, 8, 9, 9)
        d = BearSong(test)

        # Sample test
        self.assertEqual(BearSong(test).calculate(), "3")

        # Sample test
        test = ""
        # self.assertEqual(BearSong(test).calculate(), "0")

        # Sample test
        test = ""
        # self.assertEqual(BearSong(test).calculate(), "0")

        # My tests
        test = ""
        # self.assertEqual(BearSong(test).calculate(), "0")

        # Time limit test
        # self.time_limit_test(5000)

    def time_limit_test(self, nmax):
        """ Timelimit testing """
        import random
        import timeit

        # Random inputs
        test = str(nmax) + " " + str(nmax) + "\n"
        numnums = [str(i) + " " + str(i+1) for i in range(nmax)]
        test += "\n".join(numnums) + "\n"
        nums = [random.randint(1, 10000) for i in range(nmax)]
        test += " ".join(map(str, nums)) + "\n"

        # Run the test
        start = timeit.default_timer()
        d = BearSong(test)
        calc = timeit.default_timer()
        d.calculate()
        stop = timeit.default_timer()
        print("\nTimelimit Test: " +
              "{0:.3f}s (init {1:.3f}s calc {2:.3f}s)".
              format(stop-start, calc-start, stop-calc))

if __name__ == "__main__":

    # Avoiding recursion limitaions
    sys.setrecursionlimit(100000)

    if sys.argv[-1] == "-ut":
        unittest.main(argv=[" "])

    # Print the result string
    sys.stdout.write(BearSong().calculate())
