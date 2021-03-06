#!/usr/bin/env python3
# 577A_table.py - Codeforces.com/problemset/problem/577/A by Sergey 2015

import unittest
import sys

###############################################################################
# Table Class (Main Program)
###############################################################################


class Table:
    """ Table representation """

    def __init__(self, test_inputs=None):
        """ Default constructor """

        it = iter(test_inputs.split("\n")) if test_inputs else None

        def uinput():
            return next(it) if it else sys.stdin.readline().rstrip()

        # Reading single elements
        [self.n, self.m] = map(int, uinput().split())

    def calculate(self):
        """ Main calcualtion function of the class """

        result = 0
        for i in range(1, self.n+1):
            if self.m % i == 0 and self.m//i <= self.n:
                result += 1

        return str(result)

###############################################################################
# Unit Tests
###############################################################################


class unitTests(unittest.TestCase):

    def test_single_test(self):
        """ Table class testing """

        # Constructor test
        test = "10 5"
        d = Table(test)
        self.assertEqual(d.n, 10)
        self.assertEqual(d.m, 5)

        # Sample test
        self.assertEqual(Table(test).calculate(), "2")

        # Sample test
        test = "6 12"
        self.assertEqual(Table(test).calculate(), "4")

        # Sample test
        test = "5 13"
        self.assertEqual(Table(test).calculate(), "0")

        # My tests
        test = "2 2"
        self.assertEqual(Table(test).calculate(), "2")

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
        d = Table(test)
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
    sys.stdout.write(Table().calculate())
