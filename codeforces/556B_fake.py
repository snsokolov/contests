#!/usr/bin/env python
# 556B_fake.py - Codeforces.com 556B Fake quiz by Sergey 2015

# Standard modules
import unittest
import sys
import re

# Additional modules


###############################################################################
# Fake Class
###############################################################################


class Fake:
    """ Fake representation """

    def __init__(self, args):
        """ Default constructor """

        self.list = args
        self.n = len(self.list)

    def rotate(self):
        for i in range(self.n):
            if not i % 2:
                self.list[i] += 1
            else:
                self.list[i] -= 1
            self.list[i] %= self.n

    def calculate(self):
        """ Main calcualtion function of the class """
        result = 0
        for i in range(self.n):
            prev = -1
            match = 1
            for n in self.list:
                if n == prev + 1:
                    pass
                else:
                    match = 0
                prev = n
            if match:
                result = 1
                break
            self.rotate()

        return "Yes" if result else "No"


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
    nums = [int(s) for s in uinput().split()]

    return nums


def calculate(test_inputs=None):
    """ Base class calculate method wrapper """
    return Fake(get_inputs(test_inputs)).calculate()


###############################################################################
# Unit Tests
###############################################################################


class unitTests(unittest.TestCase):

    def test_sample_tests(self):
        """ Quiz sample tests. Add \n to separate lines """
        self.assertEqual(calculate("3\n1 0 0"), "Yes")
        self.assertEqual(calculate("5\n4 2 1 4 3"), "Yes")
        self.assertEqual(calculate("4\n0 2 3 1"), "No")

    def test_get_inputs(self):
        """ Input string decoding testing """
        self.assertEqual(get_inputs("3\n1 0 0"), [1, 0, 0])

    def test_Fake_class__basic_functions(self):
        """ Fake class basic functions testing """

        # Constructor test
        d = Fake([1, 0, 0])
        self.assertEqual(d.list, [1, 0, 0])
        self.assertEqual(d.n, 3)

        d.rotate()
        self.assertEqual(d.list, [2, 2, 1])

if __name__ == "__main__":

    # Avoiding recursion limitaions
    sys.setrecursionlimit(100000)

    if sys.argv[-1] == "-ut":
        unittest.main(argv=[" "])

    # Print the result string
    print(calculate())
