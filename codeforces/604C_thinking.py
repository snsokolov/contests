#!/usr/bin/env python3
# 604C_thinking.py - Codeforces.com/problemset/problem/604/C by Sergey 2015

import unittest
import sys

###############################################################################
# Thinking Class (Main Program)
###############################################################################


class Thinking:
    """ Thinking representation """

    def __init__(self, test_inputs=None):
        """ Default constructor """

        it = iter(test_inputs.split("\n")) if test_inputs else None

        def uinput():
            return next(it) if it else sys.stdin.readline().rstrip()

        # Reading single elements
        [self.n] = map(int, uinput().split())
        self.s = uinput()

    def calculate(self):
        """ Main calcualtion function of the class """

        result = 1
        empty = 0
        prev = self.s[0]
        for i in range(1, self.n):
            cur = self.s[i]
            if cur != prev:
                result += 1
            else:
                empty += 1
            prev = cur
        result += min(empty, 2)

        return str(result)

###############################################################################
# Unit Tests
###############################################################################


class unitTests(unittest.TestCase):

    def test_single_test(self):
        """ Thinking class testing """

        # Constructor test
        test = "8\n10000011"
        d = Thinking(test)
        self.assertEqual(d.n, 8)
        self.assertEqual(d.s, "10000011")

        # Sample test
        self.assertEqual(Thinking(test).calculate(), "5")

        # Sample test
        test = "2\n01"
        self.assertEqual(Thinking(test).calculate(), "2")

        # Sample test
        test = "1\n0"
        self.assertEqual(Thinking(test).calculate(), "1")

        # My tests
        test = "6\n010100"
        self.assertEqual(Thinking(test).calculate(), "6")

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
        d = Thinking(test)
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
    sys.stdout.write(Thinking().calculate())
