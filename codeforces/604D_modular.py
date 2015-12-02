#!/usr/bin/env python3
# 604D_modular.py - Codeforces.com/problemset/problem/604/D by Sergey 2015

import unittest
import sys

###############################################################################
# Modular Class (Main Program)
###############################################################################


class Binominals:
    """ Binominals representation """

    def mod(self, a):
        return a % self.m

    def add(self, a, b):
        return (a + b) % self.m

    def mul(self, a, b):
        return (a * b) % self.m

    def pow(self, e, n):
        r = 1
        while n > 0:
            if n & 1:
                r = self.mul(r, e)
            e = self.mul(e, e)
            n >>= 1
        return r

    def inv(self, a):
        return self.pow(a, self.m-2)

    def __init__(self, mod=(10**9)+7, maxn=10**5):
        self.m = mod


class Modular:
    """ Modular representation """

    def __init__(self, test_inputs=None):
        """ Default constructor """

        it = iter(test_inputs.split("\n")) if test_inputs else None

        def uinput():
            return next(it) if it else sys.stdin.readline().rstrip()

        # Reading single elements
        [self.p, self.k] = map(int, uinput().split())

        self.M = 10**9+7

    def calculate(self):
        """ Main calcualtion function of the class """

        result = 0
        bp = Binominals(mod=self.p)
        mm = 1
        for m in range(1, self.p):
            mm = bp.mul(mm, self.k)
            if mm == 1:
                break

        bb = Binominals(mod=self.M)
        if self.k == 0:
            result = bb.pow(self.p, self.p-1)
        elif self.k == 1:
            result = bb.pow(self.p, self.p)
        else:
            result = bb.pow(self.p, (self.p-1)//m)

        return str(result)

###############################################################################
# Unit Tests
###############################################################################


class unitTests(unittest.TestCase):

    def test_single_test(self):
        """ Modular class testing """

        # Constructor test
        test = "3 2"
        d = Modular(test)
        self.assertEqual(d.k, 2)
        self.assertEqual(d.p, 3)

        # Sample test
        self.assertEqual(Modular(test).calculate(), "3")

        # Sample test
        test = "5 4"
        self.assertEqual(Modular(test).calculate(), "25")

        # My tests
        test = ""
        # self.assertEqual(Modular(test).calculate(), "0")

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
        d = Modular(test)
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
    sys.stdout.write(Modular().calculate())
