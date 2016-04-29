#!/usr/bin/env python3
# 667A_rain.py - Codeforces.com/problemset/problem/667/A by Sergey 2016

import unittest
import sys

###############################################################################
# Rain Class (Main Program)
###############################################################################


class Rain:
    """ Rain representation """

    def __init__(self, test_inputs=None):
        """ Default constructor """

        it = iter(test_inputs.split("\n")) if test_inputs else None

        def uinput():
            return next(it) if it else sys.stdin.readline().rstrip()

        # Reading single elements
        [self.d, self.h, self.v, self.e] = map(int, uinput().split())

    def calculate(self):
        """ Main calcualtion function of the class """

        result = "NO"
        pi = 3.141592653589793238462
        vv = float(self.v) * 4 / (pi * self.d * self.d)
        if vv > self.e:
            result = "YES\n"
            result += str(float(self.h) / (vv - self.e))

        return str(result)

###############################################################################
# Unit Tests
###############################################################################


class unitTests(unittest.TestCase):

    def test_single_test(self):
        """ Rain class testing """

        # Constructor test
        test = "1 2 3 10"
        d = Rain(test)
        self.assertEqual(d.d, 1)

        # Sample test
        self.assertEqual(Rain(test).calculate(), "NO")

        # Sample test
        test = "1 1 1 1"
        self.assertEqual(Rain(test).calculate(), "YES\n3.6597923663254868")

        # Sample test
        test = ""
        # self.assertEqual(Rain(test).calculate(), "0")

        # My tests
        test = ""
        # self.assertEqual(Rain(test).calculate(), "0")

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
        d = Rain(test)
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
    sys.stdout.write(Rain().calculate())
