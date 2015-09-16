#!/usr/bin/env python
# 579C_polyline.py - Codeforces.com/problemset/problem/579/C by Sergey 2015

import unittest
import sys

###############################################################################
# Polyline Class (Main Program)
###############################################################################


class Polyline:
    """ Polyline representation """

    def __init__(self, test_inputs=None):
        """ Default constructor """

        it = iter(test_inputs.split("\n")) if test_inputs else None

        def uinput():
            return next(it) if it else sys.stdin.readline().rstrip()

        # Reading single elements
        [self.a, self.b] = map(int, uinput().split())

    def calculate(self):
        """ Main calcualtion function of the class """

        result = float(1)

        if self.a < self.b:
            return "-1"

        if self.a == self.b:
            return str("{0:.12f}".format(self.b))

        r1 = (self.a + self.b) / (2 * int((self.a + self.b) / (2 * self.b)))
        d = (2 * int((self.a - self.b) / (2 * self.b)))
        result = r1 if d == 0 else min(r1, (self.a - self.b) / d)
        return str("{0:.12f}".format(result))

###############################################################################
# Unit Tests
###############################################################################


class unitTests(unittest.TestCase):

    def test_single_test(self):
        """ Polyline class testing """

        # Constructor test
        test = "3 1"
        d = Polyline(test)
        self.assertEqual(d.a, 3)
        self.assertEqual(d.b, 1)

        # Sample test
        self.assertEqual(Polyline(test).calculate(), "1.000000000000")

        # Sample test
        test = "1 3"
        self.assertEqual(Polyline(test).calculate(), "-1")

        # Sample test
        test = "4 1"
        self.assertEqual(Polyline(test).calculate(), "1.250000000000")

        # My tests
        test = "103 100"
        self.assertEqual(float(Polyline(test).calculate()), 101.5)
        test = "299 100"
        self.assertEqual(float(Polyline(test).calculate()), 199.5)
        test = "310 100"
        self.assertEqual(float(Polyline(test).calculate()), 102.5)

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
        d = Polyline(test)
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
    sys.stdout.write(Polyline().calculate())
