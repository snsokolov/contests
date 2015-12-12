#!/usr/bin/env python3
# 606A_spheres.py - Codeforces.com/problemset/problem/606/A by Sergey 2015

import unittest
import sys

###############################################################################
# Spheres Class (Main Program)
###############################################################################


class Spheres:
    """ Spheres representation """

    def __init__(self, test_inputs=None):
        """ Default constructor """

        it = iter(test_inputs.split("\n")) if test_inputs else None

        def uinput():
            return next(it) if it else sys.stdin.readline().rstrip()

        # Reading a single line of multiple elements
        self.numa = list(map(int, uinput().split()))
        self.numb = list(map(int, uinput().split()))

        self.delta = [a - b for (a, b) in zip(self.numa, self.numb)]
        pos = [d // 2 for d in self.delta if d > 0]
        neg = [d for d in self.delta if d < 0]

        self.result = 1
        if sum(pos) + sum(neg) < 0:
            self.result = 0

    def calculate(self):
        """ Main calcualtion function of the class """

        return "Yes" if self.result else "No"

###############################################################################
# Unit Tests
###############################################################################


class unitTests(unittest.TestCase):

    def test_single_test(self):
        """ Spheres class testing """

        # Constructor test
        test = "4 4 0\n2 1 2"
        d = Spheres(test)
        self.assertEqual(d.numa, [4, 4, 0])
        self.assertEqual(d.numb, [2, 1, 2])
        self.assertEqual(d.delta, [2, 3, -2])

        # Sample test
        self.assertEqual(Spheres(test).calculate(), "Yes")

        # Sample test
        test = "5 6 1\n2 7 2"
        self.assertEqual(Spheres(test).calculate(), "No")

        # Sample test
        test = "3 3 3\n2 2 2"
        self.assertEqual(Spheres(test).calculate(), "Yes")

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
        d = Spheres(test)
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
    sys.stdout.write(Spheres().calculate())
