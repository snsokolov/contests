#!/usr/bin/env python
# 556A_zeroes.py - Codeforces.com 556A Zeroes quiz by Sergey 2015

# Standard modules
import unittest
import sys
import re

# Additional modules


###############################################################################
# Zeroes Class
###############################################################################


class Zeroes:
    """ Zeroes representation """

    def __init__(self, args):
        """ Default constructor """

        self.list = args

    def calculate(self):
        """ Main calcualtion function of the class """
        result = 0
        for n in self.list:
            result += 1 if n else -1

        return str(abs(result))


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
            return input()

    # Getting string inputs
    num = int(uinput())
    ints = [int(n) for n in uinput()]

    return ints


def calculate(test_inputs=None):
    """ Base class calculate method wrapper """
    return Zeroes(get_inputs(test_inputs)).calculate()


###############################################################################
# Unit Tests
###############################################################################


class unitTests(unittest.TestCase):

    def test_sample_tests(self):
        """ Quiz sample tests. Add \n to separate lines """
        self.assertEqual(calculate("4\n1100"), "0")
        self.assertEqual(calculate("5\n01010"), "1")
        self.assertEqual(calculate("8\n11101111"), "6")

        str = "1\n"
        for i in range(2*pow(10, 5)):
            str += "0"
        self.assertEqual(calculate(str), "200000")

    def test_get_inputs(self):
        """ Input string decoding testing """
        self.assertEqual(get_inputs("4\n1100"), [1, 1, 0, 0])

    def test_Zeroes_class__basic_functions(self):
        """ Zeroes class basic functions testing """

        # Constructor test
        d = Zeroes([1, 0, 0, 1])
        self.assertEqual(d.list[0], 1)

        self.assertEqual(d.calculate(), "0")

        d.list = [1, 0, 0, 0]
        self.assertEqual(d.calculate(), "2")

if __name__ == "__main__":

    # Avoiding recursion limitaions
    sys.setrecursionlimit(100000)

    if sys.argv[-1] == "-ut":
        unittest.main(argv=[" "])

    # Print the result string
    print(calculate())
