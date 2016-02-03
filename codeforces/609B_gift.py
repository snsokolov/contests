#!/usr/bin/env python3
# 609B_gift.py - Codeforces.com/problemset/problem/609/B by Sergey 2015

import unittest
import sys

###############################################################################
# Gift Class (Main Program)
###############################################################################


class Gift:
    """ Gift representation """

    def __init__(self, test_inputs=None):
        """ Default constructor """

        it = iter(test_inputs.split("\n")) if test_inputs else None

        def uinput():
            return next(it) if it else sys.stdin.readline().rstrip()

        # Reading single elements
        [self.n, self.m] = map(int, uinput().split())

        # Reading a single line of multiple elements
        self.nums = list(map(int, uinput().split()))

        self.genr = [0] * self.m
        for n in self.nums:
            self.genr[n-1] += 1

        self.summ = sum(self.genr)

    def calculate(self):
        """ Main calcualtion function of the class """

        result = 0
        for (i, n) in enumerate(self.nums):
            result += self.summ - self.genr[n-1]

        return str(result//2)

###############################################################################
# Unit Tests
###############################################################################


class unitTests(unittest.TestCase):

    def test_single_test(self):
        """ Gift class testing """

        # Constructor test
        test = "4 3\n2 1 3 1"
        d = Gift(test)
        self.assertEqual(d.n, 4)
        self.assertEqual(d.m, 3)
        self.assertEqual(d.nums, [2, 1, 3, 1])
        self.assertEqual(d.genr, [2, 1, 1])

        # Sample test
        self.assertEqual(Gift(test).calculate(), "5")

        # Sample test
        test = "7 4\n4 2 3 1 2 4 3"
        self.assertEqual(Gift(test).calculate(), "18")

        # Sample test
        test = ""
        # self.assertEqual(Gift(test).calculate(), "0")

        # My tests
        test = ""
        # self.assertEqual(Gift(test).calculate(), "0")

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
        d = Gift(test)
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
    sys.stdout.write(Gift().calculate())
