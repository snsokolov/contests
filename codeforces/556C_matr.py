#!/usr/bin/env python
# 556C_matr.py - Codeforces.com/problemset/problem/556/C Matr quiz by Sergey 2015

# Standard modules
import unittest
import sys
import re

# Additional modules


###############################################################################
# Matr Class
###############################################################################


class Matr:
    """ Matr representation """

    def __init__(self, args):
        """ Default constructor """

        self.n = args[0]
        self.k = args[1]
        self.list = args[2]

    def turns(self):
        result = 0
        for l in self.list:
            result += len(l) - 1
        result += self.n - 1
        return result

    def reduce(self):
        result = 0
        for l in self.list:
            max = 0
            for i in range(len(l)):
                if l[i] == i + 1:
                    max = i
            result += max * 2
        return result

    def calculate(self):
        """ Main calcualtion function of the class """
        turns = self.turns()
        reduce = self.reduce()
        result = turns - reduce

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
    nums = [int(s) for s in uinput().split()]
    strs = []
    for i in range(nums[1]):
        list = [int(s) for s in uinput().split()]
        list.pop(0)
        strs.append(list)

    # Decoding inputs
    inputs = nums
    inputs.append(strs)

    return inputs


def calculate(test_inputs=None):
    """ Base class calculate method wrapper """
    return Matr(get_inputs(test_inputs)).calculate()


###############################################################################
# Unit Tests
###############################################################################


class unitTests(unittest.TestCase):

    def test_sample_tests(self):
        """ Quiz sample tests. Add \n to separate lines """
        self.assertEqual(calculate("3 2\n2 1 2\n1 3"), "1")
        self.assertEqual(calculate("7 3\n3 1 3 7\n2 2 5\n2 4 6"), "10")

    def test_get_inputs(self):
        """ Input string decoding testing """
        self.assertEqual(
            get_inputs("3 2\n2 1 2\n1 3"), [3, 2, [[1, 2], [3]]])

    def test_Matr_class__basic_functions(self):
        """ Matr class basic functions testing """

        # Constructor test
        d = Matr([3, 2, [[1, 2], [3]]])

        self.assertEqual(d.turns(), 3)

        self.assertEqual(d.reduce(), 2)

if __name__ == "__main__":

    # Avoiding recursion limitaions
    sys.setrecursionlimit(100000)

    if sys.argv[-1] == "-ut":
        unittest.main(argv=[" "])

    # Print the result string
    print(calculate())
