#!/usr/bin/env python3
# 558B_larray.py - Codeforces.com/problemset/problem/558/B Larray quiz by Sergey 2015

# Standard modules
import unittest
import sys
import re
import random
import bisect
import array

# Additional modules


###############################################################################
# Larray Class
###############################################################################


class Larray:
    """ Larray representation """

    def __init__(self, args):
        """ Default constructor """

        self.n = args[0]
        self.list = args[1]

        self.freq = {}
        for i in range(self.n):

            key = self.list[i]
            if key in self.freq:
                (it, len, min, max) = self.freq[key]
                it += 1
                if i < min:
                    min = i
                    len = min - max
                if i > max:
                    max = i
                    len = min - max
                self.freq[key] = (it, len, min, max)
            else:
                self.freq[key] = (1, 0, i, i)

    def calculate(self):
        """ Main calcualtion function of the class """

        values = sorted(self.freq.values())
        result = [values[-1][2]+1, values[-1][3]+1]

        return str(" ".join(map(str, result)))


###############################################################################
# Helping classes
###############################################################################


###############################################################################
# Executable code
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
    num = int(uinput())
    nums = list(map(int, uinput().split()))

    # Decoding inputs into a list
    return [num, nums]


def calculate(test_inputs=None):
    """ Base class calculate method wrapper """
    return Larray(get_inputs(test_inputs)).calculate()


###############################################################################
# Unit Tests
###############################################################################


class unitTests(unittest.TestCase):

    def test_sample_tests(self):
        """ Quiz sample tests. Add \n to separate lines """

        # Sample test 1
        test = "5\n1 1 2 2 1"
        self.assertEqual(calculate(test), "1 5")
        self.assertEqual(get_inputs(test)[0], 5)
        self.assertEqual(list(get_inputs(test)[1]), [1, 1, 2, 2, 1])

        # Sample test 2
        test = "5\n1 2 2 3 1"
        self.assertEqual(calculate(test), "2 3")

        # Sample test 3
        test = "6\n1 2 2 1 1 2"
        self.assertEqual(calculate(test), "2 6")

        # Time limit test
        imax = 10000
        test = str(imax)
        test += "\n" + " ".join(map(str, range(imax)))
        self.assertEqual(calculate(test), "10000 10000")

    def test_Larray_class__basic_functions(self):
        """ Larray class basic functions testing """

        # Constructor test
        d = Larray([5, [1, 1, 2, 2, 1]])
        self.assertEqual(d.list[0], 1)
        self.assertEqual(d.freq[1], (3, -4, 0, 4))

if __name__ == "__main__":

    # Avoiding recursion limitaions
    sys.setrecursionlimit(100000)

    if sys.argv[-1] == "-ut":
        unittest.main(argv=[" "])

    # Print the result string
    sys.stdout.write(calculate())
