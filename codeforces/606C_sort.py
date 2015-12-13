#!/usr/bin/env python3
# 606C_sort.py - Codeforces.com/problemset/problem/606/C by Sergey 2015

import unittest
import sys

###############################################################################
# Sort Class (Main Program)
###############################################################################


class Sort:
    """ Sort representation """

    def __init__(self, test_inputs=None):
        """ Default constructor """

        it = iter(test_inputs.split("\n")) if test_inputs else None

        def uinput():
            return next(it) if it else sys.stdin.readline().rstrip()

        # Reading single elements
        [self.n] = map(int, uinput().split())

        # Reading a single line of multiple elements
        self.nums = list(map(int, uinput().split()))

        # Translate number to position
        tr = [0] * self.n
        for i in range(self.n):
            tr[self.nums[i]-1] = i

        # Longest increasing subarray
        max_len = 1
        for i in range(self.n):
            if i > 0 and tr[i] > tr[i-1]:
                cur_len += 1
                max_len = max(max_len, cur_len)
            else:
                cur_len = 1

        self.result = self.n - max_len

    def calculate(self):
        """ Main calcualtion function of the class """

        return str(self.result)

###############################################################################
# Unit Tests
###############################################################################


class unitTests(unittest.TestCase):

    def test_single_test(self):
        """ Sort class testing """

        # Constructor test
        test = "5\n4 1 2 5 3"
        d = Sort(test)
        self.assertEqual(d.n, 5)
        self.assertEqual(d.nums, [4, 1, 2, 5, 3])

        # Sample test
        self.assertEqual(Sort(test).calculate(), "2")

        # Sample test
        test = "4\n4 1 3 2"
        self.assertEqual(Sort(test).calculate(), "2")

        # Sample test
        test = "8\n6 2 1 8 5 7 3 4"
        self.assertEqual(Sort(test).calculate(), "5")

        # My tests
        test = ""
        # self.assertEqual(Sort(test).calculate(), "0")

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
        d = Sort(test)
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
    sys.stdout.write(Sort().calculate())
