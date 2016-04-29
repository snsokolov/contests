#!/usr/bin/env python3
# 669B_gh.py - Codeforces.com/problemset/problem/669/B by Sergey 2016

import unittest
import sys

###############################################################################
# Gh Class (Main Program)
###############################################################################


class Gh:
    """ Gh representation """

    def __init__(self, test_inputs=None):
        """ Default constructor """

        it = iter(test_inputs.split("\n")) if test_inputs else None

        def uinput():
            return next(it) if it else sys.stdin.readline().rstrip()

        # Reading single elements
        [self.n] = map(int, uinput().split())

        # Reading a single line of multiple elements
        self.numa = [s == ">" for s in uinput()]
        self.numb = list(map(int, uinput().split()))

    def calculate(self):
        """ Main calcualtion function of the class """

        result = "FINITE"
        pos = 0
        vis = set([])
        while 0 <= pos < self.n:
            vis.add(pos)
            if self.numa[pos]:
                pos += self.numb[pos]
            else:
                pos -= self.numb[pos]
            if pos in vis:
                result = "IN" + result
                break

        return str(result)

###############################################################################
# Unit Tests
###############################################################################


class unitTests(unittest.TestCase):

    def test_single_test(self):
        """ Gh class testing """

        # Constructor test
        test = "2\n><\n1 2"
        d = Gh(test)
        self.assertEqual(d.n, 2)
        self.assertEqual(d.numa, [1, 0])
        self.assertEqual(d.numb, [1, 2])

        # Sample test
        self.assertEqual(Gh(test).calculate(), "FINITE")

        # Sample test
        test = "3\n>><\n2 1 1"
        self.assertEqual(Gh(test).calculate(), "INFINITE")

        # Sample test
        test = "4\n>>><\n1 1 1 4"
        self.assertEqual(Gh(test).calculate(), "FINITE")

        # My tests
        test = ""
        # self.assertEqual(Gh(test).calculate(), "0")

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
        d = Gh(test)
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
    sys.stdout.write(Gh().calculate())
