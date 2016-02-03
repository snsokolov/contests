#!/usr/bin/env python3
# 621B_bishops.py - Codeforces.com/problemset/problem/621/B by Sergey 2016

import unittest
import sys

###############################################################################
# Bishops Class (Main Program)
###############################################################################


class Bishops:
    """ Bishops representation """

    def __init__(self, test_inputs=None):
        """ Default constructor """

        it = iter(test_inputs.split("\n")) if test_inputs else None

        def uinput():
            return next(it) if it else sys.stdin.readline().rstrip()

        # Reading single elements
        [self.n] = map(int, uinput().split())

        # Reading multiple number of lines of the same number of elements each
        l, s = self.n, 2
        inp = (" ".join(uinput() for i in range(l))).split()
        self.numm = [[int(inp[i]) for i in range(j, l*s, s)] for j in range(s)]
        self.numa, self.numb = self.numm

        self.pairs = 0

        # Plus
        self.cnt = {}
        for i in range(len(self.numa)):
            t = self.numa[i] + self.numb[i]
            self.cnt[t] = self.cnt.setdefault(t, 0) + 1
        for c in self.cnt.values():
            self.pairs += c*(c-1)//2

        # minus
        self.cnt = {}
        for i in range(len(self.numa)):
            t = self.numa[i] - self.numb[i]
            self.cnt[t] = self.cnt.setdefault(t, 0) + 1
        for c in self.cnt.values():
            self.pairs += c*(c-1)//2

    def calculate(self):
        """ Main calcualtion function of the class """

        result = self.pairs

        return str(result)

###############################################################################
# Unit Tests
###############################################################################


class unitTests(unittest.TestCase):

    def test_single_test(self):
        """ Bishops class testing """

        # Constructor test
        test = "5\n1 1\n1 5\n3 3\n5 1\n5 5"
        d = Bishops(test)
        self.assertEqual(d.n, 5)
        self.assertEqual(d.numa, [1, 1, 3, 5, 5])

        # Sample test
        self.assertEqual(Bishops(test).calculate(), "6")

        # Sample test
        test = "3\n1 1\n2 3\n3 5"
        self.assertEqual(Bishops(test).calculate(), "0")

        # Sample test
        test = ""
        # self.assertEqual(Bishops(test).calculate(), "0")

        # My tests
        test = ""
        # self.assertEqual(Bishops(test).calculate(), "0")

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
        d = Bishops(test)
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
    sys.stdout.write(Bishops().calculate())
