#!/usr/bin/env python3
# 621A_shark.py - Codeforces.com/problemset/problem/621/A by Sergey 2016

import unittest
import sys

###############################################################################
# Shark Class (Main Program)
###############################################################################


class Shark:
    """ Shark representation """

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

        s = sum(self.nums)
        srt = sorted(self.nums)
        minodd = 0
        for m in srt:
            if m % 2:
                minodd = m
                break

        result = s if not s % 2 else s - minodd

        return str(result)

###############################################################################
# Unit Tests
###############################################################################


class unitTests(unittest.TestCase):

    def test_single_test(self):
        """ Shark class testing """

        # Constructor test
        test = "3\n1 2 3"
        d = Shark(test)
        self.assertEqual(d.n, 3)
        self.assertEqual(d.nums, [1, 2, 3])

        # Sample test
        self.assertEqual(Shark(test).calculate(), "6")

        # Sample test
        test = "1\n1"
        self.assertEqual(Shark(test).calculate(), "0")

        test = "1\n1 1 3 2"
        self.assertEqual(Shark(test).calculate(), "6")

        # Sample test
        test = "5\n999999999 999999999 999999999 999999999 999999999"
        self.assertEqual(Shark(test).calculate(), "3999999996")

        # Sample test
        test = ""
        # self.assertEqual(Shark(test).calculate(), "0")

        # My tests
        test = ""
        # self.assertEqual(Shark(test).calculate(), "0")

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
        d = Shark(test)
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
    sys.stdout.write(Shark().calculate())
