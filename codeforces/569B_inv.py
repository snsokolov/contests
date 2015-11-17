#!/usr/bin/env python3
# 569B_inv.py - Codeforces.com/problemset/problem/569/B Inv program by Sergey 2015

import unittest
import sys
import collections

###############################################################################
# Inv Class
###############################################################################


class Inv:
    """ Inv representation """

    N = 100002

    def __init__(self, test_inputs=None):
        """ Default constructor """

        it = iter(test_inputs.split("\n")) if test_inputs else None

        def uinput():
            return next(it) if it else sys.stdin.readline().rstrip()

        # Reading single elements
        self.imax = int(uinput())

        # Reading a single line of multiple elements
        self.nums = list(map(int, uinput().split()))

        # Counts
        self.cnt = [0] * self.N
        for i in range(self.imax):
            self.cnt[self.nums[i]] += 1

        self.empty = collections.deque()

        for i in range(1, self.N):
            if self.cnt[i] == 0:
                self.empty.append(i)

    def calculate(self):
        """ Main calcualtion function of the class """

        result = []
        for i in range(self.imax):
            num = self.nums[i]
            if self.cnt[num] > 1 or num > self.imax:
                e = self.empty.popleft()
                self.cnt[num] -= 1
                result.append(e)
            else:
                result.append(num)

        return str(" ".join(map(str, result)))

###############################################################################
# Unit Tests
###############################################################################


class unitTests(unittest.TestCase):

    def test_single_test(self):
        """ Inv class testing """

        # Constructor test
        test = "3\n1 3 2"
        d = Inv(test)
        self.assertEqual(d.imax, 3)
        self.assertEqual(d.nums, [1, 3, 2])

        # Sample test
        self.assertEqual(Inv(test).calculate(), "1 3 2")

        # Sample test
        test = "4\n2 2 3 3"
        self.assertEqual(Inv(test).calculate(), "1 2 4 3")

        # Sample test
        test = "1\n2"
        self.assertEqual(Inv(test).calculate(), "1")

        # Time limit test
        self.time_limit_test(10000)

    def time_limit_test(self, imax):
        """ Timelimit testing """
        import random
        import timeit

        # Random inputs
        test = str(imax) + "\n"
        nums = [random.randint(1, imax) for i in range(imax)]
        test += " ".join(map(str, nums)) + "\n"

        # Run the test
        start = timeit.default_timer()
        d = Inv(test)
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
    sys.stdout.write(Inv().calculate())
