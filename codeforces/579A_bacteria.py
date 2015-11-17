#!/usr/bin/env python3
# 579A_bacteria.py - Codeforces.com/problemset/problem/579/A by Sergey 2015

import unittest
import sys

###############################################################################
# Bacteria Class (Main Program)
###############################################################################


class Bacteria:
    """ Bacteria representation """

    def __init__(self, test_inputs=None):
        """ Default constructor """

        it = iter(test_inputs.split("\n")) if test_inputs else None

        def uinput():
            return next(it) if it else sys.stdin.readline().rstrip()

        # Reading single elements
        [self.n] = map(int, uinput().split())

    def calculate(self):
        """ Main calcualtion function of the class """

        result = 1
        cur = self.n
        while cur != 1:
            if cur % 2:
                result += 1
                cur -= 1
            while not cur % 2:
                cur //= 2

        return str(result)

###############################################################################
# Unit Tests
###############################################################################


class unitTests(unittest.TestCase):

    def test_single_test(self):
        """ Bacteria class testing """

        # Constructor test
        test = "5"
        d = Bacteria(test)
        self.assertEqual(d.n, 5)

        # Sample test
        self.assertEqual(Bacteria(test).calculate(), "2")

        # Sample test
        test = "8"
        self.assertEqual(Bacteria(test).calculate(), "1")

        # Sample test
        test = "1"
        self.assertEqual(Bacteria(test).calculate(), "1")

        # My tests
        test = "343000816"
        self.assertEqual(Bacteria(test).calculate(), "14")

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
        d = Bacteria(test)
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
    sys.stdout.write(Bacteria().calculate())
