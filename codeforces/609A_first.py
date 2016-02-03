#!/usr/bin/env python3
# 609A_first.py - Codeforces.com/problemset/problem/609/A by Sergey 2015

import unittest
import sys

###############################################################################
# First Class (Main Program)
###############################################################################


class First:
    """ First representation """

    def __init__(self, test_inputs=None):
        """ Default constructor """

        it = iter(test_inputs.split("\n")) if test_inputs else None

        def uinput():
            return next(it) if it else sys.stdin.readline().rstrip()

        # Reading single elements
        [self.n] = map(int, uinput().split())
        [self.m] = map(int, uinput().split())

        # Reading a single line of multiple elements
        self.nums = [int(uinput()) for i in range(self.n)]
        self.numss = list(reversed(sorted(self.nums)))

    def calculate(self):
        """ Main calcualtion function of the class """

        result = 0
        sum = 0
        for i in range(self.n):
            sum += self.numss[i]
            result += 1
            if (sum >= self.m):
                break

        return str(result)

###############################################################################
# Unit Tests
###############################################################################


class unitTests(unittest.TestCase):

    def test_single_test(self):
        """ First class testing """

        # Constructor test
        test = "3\n5\n2\n1\n3"
        d = First(test)
        self.assertEqual(d.n, 3)
        self.assertEqual(d.m, 5)
        self.assertEqual(d.nums, [2, 1, 3])
        self.assertEqual(d.numss, [3, 2, 1])

        # Sample test
        self.assertEqual(First(test).calculate(), "2")

        # Sample test
        test = "3\n6\n2\n3\n2"
        self.assertEqual(First(test).calculate(), "3")

        # Sample test
        test = "2\n5\n5\n10"
        self.assertEqual(First(test).calculate(), "1")

        # My tests
        test = ""
        # self.assertEqual(First(test).calculate(), "0")

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
        d = First(test)
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
    sys.stdout.write(First().calculate())
