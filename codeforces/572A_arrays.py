#!/usr/bin/env python
# 572A_arrays.py - Codeforces.com 572A Arrays program by Sergey 2015

import unittest
import sys

###############################################################################
# Arrays Class
###############################################################################


class Arrays:
    """ Arrays representation """

    def __init__(self, test_inputs=None):
        """ Default constructor """

        it = iter(test_inputs.split("\n")) if test_inputs else None

        def uinput():
            return next(it) if it else sys.stdin.readline().rstrip()

        # Reading single elements
        self.a, self.b = map(int, uinput().split())
        self.k, self.m = map(int, uinput().split())

        # Reading a single line of multiple elements
        self.na = list(map(int, uinput().split()))
        self.nb = list(map(int, uinput().split()))

        self.na = sorted(self.na)
        self.nb = sorted(self.nb)

    def calculate(self):
        """ Main calcualtion function of the class """

        result = "YES" if self.na[self.k-1] < self.nb[-self.m] else "NO"

        return result

###############################################################################
# Unit Tests
###############################################################################


class unitTests(unittest.TestCase):

    def test_single_test(self):
        """ Arrays class testing """

        # Constructor test
        test = "3 3\n2 1\n1 2 3\n3 4 5"
        d = Arrays(test)
        self.assertEqual(d.a, 3)
        self.assertEqual(d.b, 3)
        self.assertEqual(d.na, [1, 2, 3])
        self.assertEqual(d.nb, [3, 4, 5])

        # Sample test
        self.assertEqual(Arrays(test).calculate(), "YES")

        # Sample test
        test = "3 3\n3 3\n1 2 3\n3 4 5"
        self.assertEqual(Arrays(test).calculate(), "NO")

        # Sample test
        test = "5 2\n3 1\n1 1 1 1 1\n2 2"
        self.assertEqual(Arrays(test).calculate(), "YES")

        # My tests
        test = "1\n1 2\n1"
        # self.assertEqual(Arrays(test).calculate(), "0")

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
        d = Arrays(test)
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
    sys.stdout.write(Arrays().calculate())
