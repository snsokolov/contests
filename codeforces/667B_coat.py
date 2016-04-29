#!/usr/bin/env python3
# 667B_coat.py - Codeforces.com/problemset/problem/667/B by Sergey 2016

import unittest
import sys

###############################################################################
# Coat Class (Main Program)
###############################################################################


class Coat:
    """ Coat representation """

    def __init__(self, test_inputs=None):
        """ Default constructor """

        it = iter(test_inputs.split("\n")) if test_inputs else None

        def uinput():
            return next(it) if it else sys.stdin.readline().rstrip()

        # Reading single elements
        [self.n] = map(int, uinput().split())

        # Reading a single line of multiple elements
        self.numl = list(map(int, uinput().split()))

    def calculate(self):
        """ Main calcualtion function of the class """

        result = 0
        lsum = sum(self.numl)
        lmax = max(self.numl)
        result = 2*lmax - lsum + 1

        return str(result)

###############################################################################
# Unit Tests
###############################################################################


class unitTests(unittest.TestCase):

    def test_single_test(self):
        """ Coat class testing """

        # Constructor test
        test = "3\n1 2 1"
        d = Coat(test)
        self.assertEqual(d.n, 3)
        self.assertEqual(d.numl, [1, 2, 1])

        # Sample test
        self.assertEqual(Coat(test).calculate(), "1")

        # Sample test
        test = "5\n20 4 3 2 1"
        self.assertEqual(Coat(test).calculate(), "11")

        # Sample test
        test = ""
        # self.assertEqual(Coat(test).calculate(), "0")

        # My tests
        test = ""
        # self.assertEqual(Coat(test).calculate(), "0")

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
        d = Coat(test)
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
    sys.stdout.write(Coat().calculate())
