#!/usr/bin/env python3
# 574A_bear.py - Codeforces.com/problemset/problem/574/A Bear program by Sergey 2015

import unittest
import sys

###############################################################################
# Bear Class
###############################################################################


class Bear:
    """ Bear representation """

    def __init__(self, test_inputs=None):
        """ Default constructor """

        it = iter(test_inputs.split("\n")) if test_inputs else None

        def uinput():
            return next(it) if it else sys.stdin.readline().rstrip()

        # Reading single elements
        self.n = int(uinput())

        # Reading a single line of multiple elements
        self.nums = list(map(int, uinput().split()))

    def calculate(self):
        """ Main calcualtion function of the class """

        lamak = self.nums[0]
        srt = sorted(self.nums[1:])
        result = 0

        while lamak <= srt[-1]:
            srt[-1] -= 1
            lamak += 1
            result += 1
            srt = sorted(srt)

        return str(result)

###############################################################################
# Unit Tests
###############################################################################


class unitTests(unittest.TestCase):

    def test_single_test(self):
        """ Bear class testing """

        # Constructor test
        test = "5\n5 1 11 2 8"
        d = Bear(test)
        self.assertEqual(d.n, 5)
        self.assertEqual(d.nums, [5, 1, 11, 2, 8])

        # Sample test
        self.assertEqual(Bear(test).calculate(), "4")

        # Sample test
        test = "4\n1 8 8 8"
        self.assertEqual(Bear(test).calculate(), "6")

        # Sample test
        test = "2\n7 6"
        self.assertEqual(Bear(test).calculate(), "0")

        # My tests
        test = "4\n0 1 1 1"
        self.assertEqual(Bear(test).calculate(), "2")

        # Time limit test
        self.time_limit_test(100)

    def time_limit_test(self, nmax):
        """ Timelimit testing """
        import random
        import timeit

        # Random inputs
        test = str(nmax) + "\n"
        test += "0 "
        nums = [1000 for i in range(nmax-1)]
        test += " ".join(map(str, nums)) + "\n"

        # Run the test
        start = timeit.default_timer()
        d = Bear(test)
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
    sys.stdout.write(Bear().calculate())
