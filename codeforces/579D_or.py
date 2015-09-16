#!/usr/bin/env python
# 579D_or.py - Codeforces.com/problemset/problem/579/D by Sergey 2015

import unittest
import sys

###############################################################################
# Or Class (Main Program)
###############################################################################


class Or:
    """ Or representation """

    def __init__(self, test_inputs=None):
        """ Default constructor """

        it = iter(test_inputs.split("\n")) if test_inputs else None

        def uinput():
            return next(it) if it else sys.stdin.readline().rstrip()

        # Reading single elements
        [self.n, self.k, self.x] = map(int, uinput().split())

        # Reading a single line of multiple elements
        self.nums = list(map(int, uinput().split()))

        self.cnt = [0] * 100
        for n in self.nums:
            i = 0
            while n != 0:
                if n % 2:
                    self.cnt[i] += 1
                n >>= 1
                i += 1

        self.nmax = 0
        for n in self.nums:
            cur_cnt = list(self.cnt)
            i = 0
            nn = n
            while n != 0:
                if n % 2:
                    cur_cnt[i] -= 1
                n >>= 1
                i += 1
            n = nn * self.x ** self.k
            i = 0
            while n != 0:
                if n % 2:
                    cur_cnt[i] += 1
                n >>= 1
                i += 1

            k = 0
            for i in range(len(cur_cnt)):
                if cur_cnt[i] > 0:
                    k += 1 << i

            if k > self.nmax:
                self.nmax = k

    def calculate(self):
        """ Main calcualtion function of the class """

        result = self.nmax

        return str(result)

###############################################################################
# Unit Tests
###############################################################################


class unitTests(unittest.TestCase):

    def test_single_test(self):
        """ Or class testing """

        # Constructor test
        test = "3 1 2\n1 1 1"
        d = Or(test)
        self.assertEqual(d.n, 3)
        self.assertEqual(d.k, 1)
        self.assertEqual(d.x, 2)
        self.assertEqual(d.nums, [1, 1, 1])

        # Sample test
        self.assertEqual(Or(test).calculate(), "3")

        # Sample test
        test = "4 2 3\n1 2 4 8"
        self.assertEqual(Or(test).calculate(), "79")

        # Sample test
        test = ""
        # self.assertEqual(Or(test).calculate(), "0")

        # My tests
        test = ""
        # self.assertEqual(Or(test).calculate(), "0")

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
        d = Or(test)
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
    sys.stdout.write(Or().calculate())
