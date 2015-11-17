#!/usr/bin/env python3
# 557B_tea.py - Codeforces.com/problemset/problem/557/B Tea quiz by Sergey 2015

# Standard modules
import unittest
import sys
import re

# Additional modules


###############################################################################
# Tea Class
###############################################################################


class Tea:
    """ Tea representation """

    def __init__(self, args):
        """ Default constructor """

        self.list = args[2]
        self.n = args[0]
        self.w = args[1]

        self.slist = sorted(self.list)

        self.b = self.slist[self.n]
        self.g = self.slist[0]

        self.wmax = (
            self.n * min(self.b, self.g * 2) + self.n * min(self.b/2, self.g))

    def calculate(self):
        """ Main calcualtion function of the class """

        result = min(self.wmax, self.w)

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

    # Getting string inputs. Place all uinput() calls here
    nums = [int(s) for s in uinput().split()]
    cups = [int(s) for s in uinput().split()]

    # Decoding inputs into a list
    inputs = nums
    inputs.append(cups)

    return inputs


def calculate(test_inputs=None):
    """ Base class calculate method wrapper """
    return Tea(get_inputs(test_inputs)).calculate()


###############################################################################
# Unit Tests
###############################################################################


class unitTests(unittest.TestCase):

    def test_sample_tests(self):
        """ Quiz sample tests. Add \n to separate lines """

        # Sample test 1
        test = "2 4\n1 1 1 1"
        self.assertEqual(calculate(test), "3.0")
        self.assertEqual(get_inputs(test), [2, 4, [1, 1, 1, 1]])

        # Other tests
        test = "3 18\n4 4 4 2 2 2"
        self.assertEqual(calculate(test), "18.0")
        test = "1 5\n2 3"
        self.assertEqual(calculate(test), "4.5")

        test = "2 5\n1 2 3 4"
        self.assertEqual(calculate(test), "5")

    def test_Tea_class__basic_functions(self):
        """ Tea class basic functions testing """

        # Constructor test
        d = Tea([2, 4, [1, 1, 2, 1]])
        self.assertEqual(d.list[0], 1)
        self.assertEqual(d.w, 4)
        self.assertEqual(d.n, 2)

        # Sort cups
        self.assertEqual(d.slist[-1], 2)
        self.assertEqual(d.b, 1)
        self.assertEqual(d.g, 1)

        self.assertEqual(d.wmax, 3)

if __name__ == "__main__":

    # Avoiding recursion limitaions
    sys.setrecursionlimit(100000)

    if sys.argv[-1] == "-ut":
        unittest.main(argv=[" "])

    # Print the result string
    print(calculate())
