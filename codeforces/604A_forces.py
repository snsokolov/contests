#!/usr/bin/env python3
# 604A_forces.py - Codeforces.com/problemset/problem/604/A by Sergey 2015

import unittest
import sys

###############################################################################
# Forces Class (Main Program)
###############################################################################


class Forces:
    """ Forces representation """

    def __init__(self, test_inputs=None):
        """ Default constructor """

        it = iter(test_inputs.split("\n")) if test_inputs else None

        def uinput():
            return next(it) if it else sys.stdin.readline().rstrip()

        # Reading a single line of multiple elements
        self.numm = list(map(int, uinput().split()))
        self.numw = list(map(int, uinput().split()))
        [self.hs, self.hu] = map(int, uinput().split())
        self.mx = [500, 1000, 1500, 2000, 2500]

    def calculate(self):
        """ Main calcualtion function of the class """

        result = 0
        for i in range(5):
            x = self.mx[i]
            m = self.numm[i]
            w = self.numw[i]
            result += max(0.3*x, (1 - m/250) * x - 50 * w)

        result += 100 * self.hs - 50 * self.hu

        return str(int(result))

###############################################################################
# Unit Tests
###############################################################################


class unitTests(unittest.TestCase):

    def test_single_test(self):
        """ Forces class testing """

        # Constructor test
        test = "20 40 60 80 100\n0 1 2 3 4\n1 0"
        d = Forces(test)
        self.assertEqual(d.numw, [0, 1, 2, 3, 4])

        # Sample test
        self.assertEqual(Forces(test).calculate(), "4900")

        # Sample test
        test = "119 119 119 119 119\n0 0 0 0 0\n10 0"
        self.assertEqual(Forces(test).calculate(), "4930")

        # Sample test
        test = ""
        # self.assertEqual(Forces(test).calculate(), "0")

        # My tests
        test = ""
        # self.assertEqual(Forces(test).calculate(), "0")

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
        d = Forces(test)
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
    sys.stdout.write(Forces().calculate())
