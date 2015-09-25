#!/usr/bin/env python
# 580A_steps.py - Codeforces.com/problemset/problem/580/A by Sergey 2015

import unittest
import sys

###############################################################################
# Steps Class (Main Program)
###############################################################################


class Steps:
    """ Steps representation """

    def __init__(self, test_inputs=None):
        """ Default constructor """

        it = iter(test_inputs.split("\n")) if test_inputs else None

        def uinput():
            return next(it) if it else sys.stdin.readline().rstrip()

        # Reading single elements
        [self.n] = map(int, uinput().split())

        # Reading a single line of multiple elements
        self.nums = list(map(int, uinput().split()))

    def calculate(self):
        """ Main calcualtion function of the class """

        result = m = 1
        for i in range(len(self.nums)):
            if i != 0:
                m = m + 1 if self.nums[i] >= self.nums[i-1] else 1
                result = max(result, m)

        return str(result)

###############################################################################
# Unit Tests
###############################################################################


class unitTests(unittest.TestCase):

    def test_single_test(self):
        """ Steps class testing """

        # Constructor test
        test = "6\n2 2 1 3 4 1"
        d = Steps(test)
        self.assertEqual(d.n, 6)
        self.assertEqual(d.nums[0:3], [2, 2, 1])

        # Sample test
        self.assertEqual(Steps(test).calculate(), "3")

        # Sample test
        test = "3\n2 2 9"
        self.assertEqual(Steps(test).calculate(), "3")

        # Sample test
        test = "2\n0"
        self.assertEqual(Steps(test).calculate(), "1")

        # My tests
        test = ""
        # self.assertEqual(Steps(test).calculate(), "0")

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
        d = Steps(test)
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
    sys.stdout.write(Steps().calculate())
