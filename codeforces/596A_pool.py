#!/usr/bin/env python3
# 596A_pool.py - Codeforces.com/problemset/problem/596/A by Sergey 2015

import unittest
import sys

###############################################################################
# Pool Class (Main Program)
###############################################################################


class Pool:
    """ Pool representation """

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

    def calculate(self):
        """ Main calcualtion function of the class """

        result = 0
        m = min(3, len(self.numa))

        for i in range(m):
            for j in range(i+1, m):
                result += abs(
                    (self.numa[i] - self.numa[j]) *
                    (self.numb[i] - self.numb[j]))
        if result == 0:
            result = -1

        return str(result)

###############################################################################
# Unit Tests
###############################################################################


class unitTests(unittest.TestCase):

    def test_single_test(self):
        """ Pool class testing """

        # Constructor test
        test = "2\n0 0\n1 1"
        d = Pool(test)
        self.assertEqual(d.n, 2)
        self.assertEqual(d.numa, [0, 1])
        self.assertEqual(d.numb, [0, 1])

        # Sample test
        self.assertEqual(Pool(test).calculate(), "1")

        # Sample test
        test = "1\n1 1"
        self.assertEqual(Pool(test).calculate(), "-1")

        # Sample test
        test = "4\n2 2\n3 3\n2 3\n3 2"
        self.assertEqual(Pool(test).calculate(), "1")

        # My tests
        test = "2\n100 100\n0 0"
        self.assertEqual(Pool(test).calculate(), "10000")

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
        d = Pool(test)
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
    sys.stdout.write(Pool().calculate())
