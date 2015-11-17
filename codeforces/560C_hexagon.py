#!/usr/bin/env python3
# 560C_hexagon.py - Codeforces.com/problemset/problem/560/C Hexagon program by Sergey 2015

# Standard modules
import unittest
import sys

# Additional modules


###############################################################################
# Hexagon Class
###############################################################################


class Hexagon:
    """ Hexagon representation """

    def __init__(self, args):
        """ Default constructor """

        self.nums = args

        self.bottom = self.nums[0]
        self.bi = 0
        for i in range(6):
            if self.nums[i] > self.bottom:
                self.bottom = self.nums[i]
                self.bi = i

        self.ll = self.nums[(self.bi - 1 + 6) % 6]
        self.hl = self.nums[(self.bi - 2 + 6) % 6]
        self.lr = self.nums[(self.bi + 1 + 6) % 6]

        self.ill = self.ll
        self.ilr = self.lr
        self.ihl = self.hl
        self.ib = self.bottom
        self.low = 0
        while self.ill > 0:
            if self.ilr <= 0:
                self.low += self.ib * 2
            else:
                self.low += self.ib * 2 + 1
                self.ib += 1
                self.ilr -= 1
            self.ill -= 1

        self.hi = 0
        while self.ihl > 0:
            if self.ilr <= 0:
                self.hi += self.ib * 2 - 1
                self.ib -= 1
            else:
                self.hi += self.ib * 2
                self.ilr -= 1
            self.ihl -= 1

    def calculate(self):
        """ Main calcualtion function of the class """

        result = self.low + self.hi

        return str(result)


###############################################################################
# Helping classes
###############################################################################


###############################################################################
# Hexagon Class testing wrapper code
###############################################################################


def get_inputs(test_inputs=None):

    it = iter(test_inputs.split("\n")) if test_inputs else None

    def uinput():
        """ Unit-testable input function wrapper """
        if it:
            return next(it)
        else:
            return sys.stdin.readline()

    # Getting string inputs. Place all uinput() calls here
    imax = 6
    nums = list(map(int, uinput().split()))

    # Decoding inputs into a list
    return nums


def calculate(test_inputs=None):
    """ Base class calculate method wrapper """
    return Hexagon(get_inputs(test_inputs)).calculate()


###############################################################################
# Unit Tests
###############################################################################


class unitTests(unittest.TestCase):

    def test_Hexagon_class__basic_functions(self):
        """ Hexagon class basic functions testing """

        # Constructor test
        d = Hexagon([2, 1, 3, 2, 1, 3])
        self.assertEqual(d.bottom, 3)
        self.assertEqual(d.ll, 1)
        self.assertEqual(d.hl, 2)
        self.assertEqual(d.lr, 2)
        self.assertEqual(d.low, 7)
        self.assertEqual(d.hi, 15)

    def test_sample_tests(self):
        """ Quiz sample tests. Add \n to separate lines """

        # Sample test 1
        test = "1 1 1 1 1 1"
        self.assertEqual(calculate(test), "6")
        self.assertEqual(list(get_inputs(test)), [1, 1, 1, 1, 1, 1])

        # Sample test 2
        test = "1 2 1 2 1 2"
        self.assertEqual(calculate(test), "13")

        # My test
        test = "3 2 1 3 2 1"
        self.assertEqual(calculate(test), "22")
        test = "3 1 2 3 1 2"
        self.assertEqual(calculate(test), "22")
        test = "4 1 2 3 2 1"
        self.assertEqual(calculate(test), "25")

    def test_time_limit_test(self):
        """ Quiz time limit test """

        import random

        # Time limit test
        test = "1000 900 999 990 999 1000"

        import timeit

        start = timeit.default_timer()
        args = get_inputs(test)

        init = timeit.default_timer()
        d = Hexagon(args)

        calc = timeit.default_timer()
        d.calculate()

        stop = timeit.default_timer()
        print(
            "\nTime Test: " +
            "{0:.3f}s (inp {1:.3f}s init {2:.3f}s calc {3:.3f}s)".
            format(stop-start, init-start, calc-init, stop-calc))

if __name__ == "__main__":

    # Avoiding recursion limitaions
    sys.setrecursionlimit(100000)

    if sys.argv[-1] == "-ut":
        unittest.main(argv=[" "])

    # Print the result string
    sys.stdout.write(calculate())
