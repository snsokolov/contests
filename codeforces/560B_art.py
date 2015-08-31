#!/usr/bin/env python
# 560B_art.py - Codeforces.com/problemset/problem/560/B Art program by Sergey 2015

# Standard modules
import unittest
import sys

# Additional modules


###############################################################################
# Art Class
###############################################################################


class Art:
    """ Art representation """

    def __init__(self, args):
        """ Default constructor """

        self.numa, self.numb = args

        self.r = self.rect(self.numa[0], self.numb[0])
        self.rmax = self.rect(self.numa[1], self.numb[1])
        self.rmin = self.rect(self.numa[2], self.numb[2])
        if self.rmax[0] < self.rmax[1]:
            self.rmax, self.rmin = self.rmin, self.rmax

        self.remain = []
        if self.rmax[0] < self.r[0] and self.rmax[1] <= self.r[1]:
            self.remain.append((self.r[0] - self.rmax[0], self.r[1]))
        if self.rmax[1] < self.r[1] and self.rmax[0] <= self.r[0]:
            self.remain.append((self.r[0], self.r[1] - self.rmax[1]))

        if self.rmax[1] < self.r[0] and self.rmax[0] <= self.r[1]:
            self.remain.append((self.r[0] - self.rmax[1], self.r[1]))
        if self.rmax[0] < self.r[1] and self.rmax[1] <= self.r[0]:
            self.remain.append((self.r[0], self.r[1] - self.rmax[0]))

    def rect(self, a, b):
        if a > b:
            return (a, b)
        else:
            return (b, a)

    def calculate(self):
        """ Main calcualtion function of the class """

        for rec in self.remain:
            if self.rmin[0] <= rec[0] and self.rmin[1] <= rec[1]:
                return "YES"
            if self.rmin[1] <= rec[0] and self.rmin[0] <= rec[1]:
                return "YES"
        return "NO"


###############################################################################
# Helping classes
###############################################################################


###############################################################################
# Art Class testing wrapper code
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
    imax = 3
    numnums = list(map(int, " ".join(uinput() for i in range(imax)).split()))

    # Splitting numnums into n arrays
    numa = []
    numb = []
    for i in range(0, 2*imax, 2):
        numa.append(numnums[i])
        numb.append(numnums[i+1])

    # Decoding inputs into a list
    return [numa, numb]


def calculate(test_inputs=None):
    """ Base class calculate method wrapper """
    return Art(get_inputs(test_inputs)).calculate()


###############################################################################
# Unit Tests
###############################################################################


class unitTests(unittest.TestCase):

    def test_Art_class__basic_functions(self):
        """ Art class basic functions testing """

        # Constructor test
        d = Art([[3, 1, 2], [2, 3, 1]])
        self.assertEqual(d.numa[0], 3)

        self.assertEqual(d.r, (3, 2))
        self.assertEqual(d.rmax, (3, 1))
        self.assertEqual(d.rmin, (2, 1))

        self.assertEqual(d.remain, [(3, 1)])

    def test_sample_tests(self):
        """ Quiz sample tests. Add \n to separate lines """

        # Sample test 1
        test = "3 2\n1 3\n2 1"
        self.assertEqual(calculate(test), "YES")
        self.assertEqual(list(get_inputs(test)[0]), [3, 1, 2])
        self.assertEqual(list(get_inputs(test)[1]), [2, 3, 1])

        # Sample test 2
        test = "5 5\n3 3\n3 3"
        self.assertEqual(calculate(test), "NO")

        # Sample test 3
        test = "4 2\n2 3\n1 2"
        self.assertEqual(calculate(test), "YES")

        # My test 4
        test = "5 5\n1 5\n1 5"
        self.assertEqual(calculate(test), "YES")

    def test_time_limit_test(self):
        """ Quiz time limit test """

        import random

        # Time limit test
        test = "1000 1000"
        test += "\n900 900"
        test += "\n50 50"

        import timeit

        start = timeit.default_timer()
        args = get_inputs(test)

        init = timeit.default_timer()
        d = Art(args)

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
