#!/usr/bin/env python3
# 629C_brackets.py - Codeforces.com/problemset/problem/629/C by Sergey 2016

import unittest
import sys

###############################################################################
# Brackets Class (Main Program)
###############################################################################


class Brackets:
    """ Brackets representation """

    def __init__(self, test_inputs=None):
        """ Default constructor """

        it = iter(test_inputs.split("\n")) if test_inputs else None

        def uinput():
            return next(it) if it else sys.stdin.readline().rstrip()

        # Reading single elements
        [self.n, self.m] = map(int, uinput().split())

        # Reading a single line of multiple elements
        self.nums = [s == '(' for s in uinput().split()]

    def calculate(self):
        """ Main calcualtion function of the class """

        result = 0

        return str(result)

###############################################################################
# Unit Tests
###############################################################################


class unitTests(unittest.TestCase):

    def test_single_test(self):
        """ Brackets class testing """

        # Constructor test
        test = "4 1\n("
        d = Brackets(test)
        self.assertEqual(d.n, 4)
        self.assertEqual(d.m, 1)
        self.assertEqual(d.nums, [1])

        # Sample test
        # self.assertEqual(Brackets(test).calculate(), "4")

        # Sample test
        test = "4 4\n(())"
        # self.assertEqual(Brackets(test).calculate(), "1")

        # Sample test
        test = "4 3\n((("
        # self.assertEqual(Brackets(test).calculate(), "0")

        # My tests
        test = ""
        # self.assertEqual(Brackets(test).calculate(), "0")

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
        d = Brackets(test)
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
    sys.stdout.write(Brackets().calculate())
