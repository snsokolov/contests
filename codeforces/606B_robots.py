#!/usr/bin/env python3
# 606B_robots.py - Codeforces.com/problemset/problem/606/B by Sergey 2015

import unittest
import sys

###############################################################################
# Robots Class (Main Program)
###############################################################################


class Robots:
    """ Robots representation """

    def __init__(self, test_inputs=None):
        """ Default constructor """

        it = iter(test_inputs.split("\n")) if test_inputs else None

        def uinput():
            return next(it) if it else sys.stdin.readline().rstrip()

        # Reading single elements
        [self.x, self.y, self.x0, self.y0] = map(int, uinput().split())

        # Reading a single line of multiple elements
        self.nums = list(uinput())

    def calculate(self):
        """ Main calcualtion function of the class """

        xy = self.x * self.y
        loc = (self.x0, self.y0)
        locs = set([loc])
        result = [1]
        for (i, d) in enumerate(self.nums):
            nx, ny = loc
            if d == "U":
                nx = max(1, loc[0] - 1)
            if d == "D":
                nx = min(self.x, loc[0] + 1)
            if d == "L":
                ny = max(1, loc[1] - 1)
            if d == "R":
                ny = min(self.y, loc[1] + 1)
            loc = (nx, ny)
            if len(locs) == xy:
                result.append(0)
            elif i == len(self.nums) - 1:
                result.append(xy - len(locs))
            elif loc in locs:
                result.append(0)
            else:
                result.append(1)
            locs.add(loc)

        return " ".join(map(str, result))

###############################################################################
# Unit Tests
###############################################################################


class unitTests(unittest.TestCase):

    def test_single_test(self):
        """ Robots class testing """

        # Constructor test
        test = "3 4 2 2\nUURDRDRL"
        d = Robots(test)
        self.assertEqual(d.x, 3)
        self.assertEqual(d.y, 4)
        self.assertEqual(d.x0, 2)
        self.assertEqual(d.y0, 2)
        self.assertEqual(d.nums[:2], ["U", "U"])

        # Sample test
        self.assertEqual(Robots(test).calculate(), "1 1 0 1 1 1 1 0 6")

        # Sample test
        test = "2 2 2 2\nULD"
        self.assertEqual(Robots(test).calculate(), "1 1 1 1")

        # Sample test
        test = ""
        # self.assertEqual(Robots(test).calculate(), "0")

        # My tests
        test = ""
        # self.assertEqual(Robots(test).calculate(), "0")

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
        d = Robots(test)
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
    sys.stdout.write(Robots().calculate())
