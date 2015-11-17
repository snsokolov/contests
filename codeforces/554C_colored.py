#!/usr/bin/env python3
# 554C_colored.py - Codeforces.com/problemset/problem/554/C Colored quiz by Sergey 2015

# Standard modules
import unittest
import sys
import re

# Additional modules


###############################################################################
# Colored Class
###############################################################################


class Colored:
    """ Colored representation """

    MOD = 1000000007

    def __init__(self, args):
        """ Default constructor """

        self.list = args

    def fact(self, n):
        result = 1
        for i in range(n):
            result *= i + 1
        return result

    def binom(self, n, k):
        return (self.fact(n) // (self.fact(n - k) * self.fact(k)))

    def f(self, i):
        if i == 0:
            return 1
        bin = self.binom(sum(self.list[:i+1]) - 1, self.list[i] - 1)

        return (bin % self.MOD) * self.f(i - 1)

    def calculate(self):
        """ Main calcualtion function of the class """
        result = self.f(len(self.list) - 1) % self.MOD

        return str(result)


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
    nums = [int(uinput()) for i in range(num)]

    # Decoding inputs
    inputs = nums

    return inputs


def calculate(test_inputs=None):
    """ Base class calculate method wrapper """
    return Colored(get_inputs(test_inputs)).calculate()


###############################################################################
# Unit Tests
###############################################################################


class unitTests(unittest.TestCase):

    def test_sample_tests(self):
        """ Quiz sample tests. Add \n to separate lines """
        self.assertEqual(calculate("3\n2\n2\n1"), "3")
        self.assertEqual(calculate("4\n1\n2\n3\n4"), "1680")
        self.assertEqual(calculate(
            "10\n100\n100\n100\n100\n100\n100\n100" +
            "\n100\n100\n100"), "12520708")

    def test_get_inputs(self):
        """ Input string decoding testing """
        self.assertEqual(get_inputs("2\n1\n3"), [1, 3])

    def test_Colored_class__basic_functions(self):
        """ Colored class basic functions testing """

        # Constructor test
        d = Colored([2, 1])
        self.assertEqual(d.list, [2, 1])

        # Factorial using modulo
        self.assertEqual(d.fact(4), 24)

        # Binominal
        self.assertEqual(d.binom(2, 1), 2)

        # Dynamic programming function, solution for i colors
        self.assertEqual(d.f(0), 1)
        self.assertEqual(d.f(1), 1)


if __name__ == "__main__":

    # Avoiding recursion limitaions
    sys.setrecursionlimit(100000)

    if sys.argv[-1] == "-ut":
        unittest.main(argv=[" "])

    # Print the result string
    print(calculate())
