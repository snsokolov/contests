#!/usr/bin/env python3
# 672B_good.py - Codeforces.com/problemset/problem/672/B by Sergey 2016

import unittest
import sys

###############################################################################
# Good Class (Main Program)
###############################################################################


class Good:
    """ Good representation """

    def __init__(self, test_inputs=None):
        """ Default constructor """

        it = iter(test_inputs.split("\n")) if test_inputs else None

        def uinput():
            return next(it) if it else sys.stdin.readline().rstrip()

        # Reading single elements
        [self.n] = map(int, uinput().split())

        self.s = list(uinput())

    def calculate(self):
        """ Main calcualtion function of the class """

        freq = [0]*26
        for c in self.s:
            ltr = ord(c) - ord('a')
            freq[ltr] += 1

        zeroes = 0
        extra = 0
        for n in freq:
            if n == 0:
                zeroes += 1
            if n > 1:
                extra += n - 1

        result = -1 if extra > zeroes else extra

        return str(result)

###############################################################################
# Unit Tests
###############################################################################


class unitTests(unittest.TestCase):

    def test_single_test(self):
        """ Good class testing """

        # Constructor test
        test = "2\naa"
        d = Good(test)
        self.assertEqual(d.n, 2)
        self.assertEqual(d.s, ["a", "a"])

        # Sample test
        self.assertEqual(Good(test).calculate(), "1")

        # Sample test
        test = "4\nkoko"
        self.assertEqual(Good(test).calculate(), "2")

        # Sample test
        test = "5\nmurat"
        self.assertEqual(Good(test).calculate(), "0")

        # My tests
        test = "30\ndasdsadasdasdasdsadasdsadasdasda"
        self.assertEqual(Good(test).calculate(), "-1")

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
        d = Good(test)
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
    sys.stdout.write(Good().calculate())
