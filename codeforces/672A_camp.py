#!/usr/bin/env python3
# 672A_camp.py - Codeforces.com/problemset/problem/672/A by Sergey 2016

import unittest
import sys

###############################################################################
# Camp Class (Main Program)
###############################################################################


class Camp:
    """ Camp representation """

    def __init__(self, test_inputs=None):
        """ Default constructor """

        it = iter(test_inputs.split("\n")) if test_inputs else None

        def uinput():
            return next(it) if it else sys.stdin.readline().rstrip()

        # Reading single elements
        [self.n] = map(int, uinput().split())

    def calculate(self):
        """ Main calcualtion function of the class """

        line = ""
        for i in range(400):
            line += str(i)

        result = line[self.n]

        return str(result)

###############################################################################
# Unit Tests
###############################################################################


class unitTests(unittest.TestCase):

    def test_single_test(self):
        """ Camp class testing """

        # Constructor test
        test = "3"
        d = Camp(test)
        self.assertEqual(d.n, 3)

        # Sample test
        self.assertEqual(Camp(test).calculate(), "3")

        # Sample test
        test = "11"
        self.assertEqual(Camp(test).calculate(), "0")

        # Sample test
        test = ""
        # self.assertEqual(Camp(test).calculate(), "0")

        # My tests
        test = ""
        # self.assertEqual(Camp(test).calculate(), "0")

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
        d = Camp(test)
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
    sys.stdout.write(Camp().calculate())
