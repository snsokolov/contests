#!/usr/bin/env python
# 557A_diploma.py - Codeforces.com 557A Diploma quiz by Sergey 2015

# Standard modules
import unittest
import sys
import re

# Additional modules


###############################################################################
# Diploma Class
###############################################################################


class Diploma:
    """ Diploma representation """

    def __init__(self, args):
        """ Default constructor """

        self.list = args
        self.n = args[0]
        self.ranges = args[1:]
        self.range = [0, 0, 0]

    def set_range(self):

        reminder = self.n
        min0 = reminder - self.ranges[2][0] - self.ranges[1][0]
        self.range[0] = min(min0, self.ranges[0][1])
        reminder -= self.range[0]
        self.range[1] = min(reminder - self.ranges[2][0], self.ranges[1][1])
        reminder -= self.range[1]
        self.range[2] = min(reminder, self.ranges[2][1])

    def calculate(self):
        """ Main calcualtion function of the class """

        self.set_range()
        result = self.range

        return str(" ".join([str(n) for n in result]))


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

    # Getting string inputs. Place all uinput() calls here
    num = int(uinput())
    nums = [[int(s) for s in uinput().split()] for i in range(3)]

    # Decoding inputs into a list
    inputs = []
    inputs.append(num)
    inputs += nums

    return inputs


def calculate(test_inputs=None):
    """ Base class calculate method wrapper """
    return Diploma(get_inputs(test_inputs)).calculate()


###############################################################################
# Unit Tests
###############################################################################


class unitTests(unittest.TestCase):

    def test_sample_tests(self):
        """ Quiz sample tests. Add \n to separate lines """

        # Sample test 1
        test = "6\n1 5\n2 6\n3 7"
        self.assertEqual(calculate(test), "1 2 3")
        self.assertEqual(get_inputs(test), [6, [1, 5], [2, 6], [3, 7]])

        # Other tests
        test = "10\n1 2\n1 3\n1 5"
        self.assertEqual(calculate(test), "2 3 5")
        test = "6\n1 3\n2 2\n2 2"
        self.assertEqual(calculate(test), "2 2 2")

    def test_Diploma_class__basic_functions(self):
        """ Diploma class basic functions testing """

        # Constructor test
        d = Diploma([6, [1, 5], [2, 6], [3, 7]])
        self.assertEqual(d.list[0], 6)
        self.assertEqual(d.n, 6)
        self.assertEqual(d.ranges[0], [1, 5])

        # Calculate ranges
        d.set_range()
        self.assertEqual(d.range, [1, 2, 3])


if __name__ == "__main__":

    # Avoiding recursion limitaions
    sys.setrecursionlimit(100000)

    if sys.argv[-1] == "-ut":
        unittest.main(argv=[" "])

    # Print the result string
    print(calculate())
