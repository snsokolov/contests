#!/usr/bin/env python3
# 609C_load.py - Codeforces.com/problemset/problem/609/C by Sergey 2015

import unittest
import sys

###############################################################################
# Load Class (Main Program)
###############################################################################


class Load:
    """ Load representation """

    def __init__(self, test_inputs=None):
        """ Default constructor """

        it = iter(test_inputs.split("\n")) if test_inputs else None

        def uinput():
            return next(it) if it else sys.stdin.readline().rstrip()

        # Reading single elements
        [self.n] = map(int, uinput().split())

        # Reading a single line of multiple elements
        self.nums = list(map(int, uinput().split()))

        self.snums = list(reversed(sorted(self.nums)))

        self.summ = sum(self.nums)
        self.avg = self.summ // self.n
        self.numavgp1 = self.summ - self.avg * self.n
        self.targ = [self.avg+1] * self.numavgp1
        self.targ += [self.avg] * (self.n - self.numavgp1)

    def calculate(self):
        """ Main calcualtion function of the class """

        result = 0
        for i in range(self.n):
            delta = self.snums[i] - self.targ[i]
            result += delta if delta > 0 else 0

        return str(result)

###############################################################################
# Unit Tests
###############################################################################


class unitTests(unittest.TestCase):

    def test_single_test(self):
        """ Load class testing """

        # Constructor test
        test = "2\n1 6"
        d = Load(test)
        self.assertEqual(d.n, 2)
        self.assertEqual(d.nums, [1, 6])
        self.assertEqual(d.snums, [6, 1])
        self.assertEqual(d.targ, [4, 3])

        # Sample test
        self.assertEqual(Load(test).calculate(), "2")

        # Sample test
        test = "7\n10 11 10 11 10 11 11"
        self.assertEqual(Load(test).calculate(), "0")

        # Sample test
        test = "5\n1 2 3 4 5"
        self.assertEqual(Load(test).calculate(), "3")

        # My tests
        test = ""
        # self.assertEqual(Load(test).calculate(), "0")

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
        d = Load(test)
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
    sys.stdout.write(Load().calculate())
