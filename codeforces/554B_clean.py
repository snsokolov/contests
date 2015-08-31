#!/usr/bin/env python
# 554B_clean.py - Codeforces.com 554B Clean quiz by Sergey 2015

# Standard modules
import unittest
import sys
import re

# Additional modules


###############################################################################
# Clean Class
###############################################################################


class Clean:
    """ Clean representation """

    def __init__(self, args):
        """ Default constructor """

        self.list = args

    def r2dec(self, row):
        """ Convert row binary into decimal """
        return int(self.list[row], 2)

    def calculate(self):
        """ Main calcualtion function of the class """

        result = 0
        d = {}
        for i in range(len(self.list)):
            key = self.r2dec(i)
            if key in d:
                d[key] += 1
            else:
                d[key] = 1
        for n in d:
            if result < d[n]:
                result = d[n]
        return result

###############################################################################
# Executable code
###############################################################################


def get_inputs(test_inputs=None):

    it = iter(test_inputs) if test_inputs else None

    def uinput():
        """ Unit-testable input function wrapper """
        if it:
            return next(it)
        else:
            return input()

    # Getting string inputs
    num = int(uinput())
    strs = [uinput() for i in range(num)]

    # Decoding inputs
    return strs


def calculate(test_inputs=None):
    """ Base class calculate method wrapper """
    return Clean(get_inputs(test_inputs)).calculate()


def main():
    """ Main function. Not called by unit tests """

    # Print the result
    print(calculate())

###############################################################################
# Unit Tests
###############################################################################


class unitTests(unittest.TestCase):

    def test_get_inputs(self):
        """ Input string decoding testing """
        self.assertEqual(get_inputs(["2", "00", "10"]), ["00", "10"])

    def test_Clean_class__basic_functions(self):
        """ Clean class basic functions testing """
        d = Clean(["00", "11"])
        self.assertEqual(d.list[1], "11")

        # Convert
        self.assertEqual(d.r2dec(1), 3)

    def test_calculate(self):
        """ Main calculation function """

        # Sample tests
        self.assertEqual(
            calculate(["4", "0101", "1000", "1111", "0101"]), 2)
        self.assertEqual(
            calculate(["3", "111", "111", "111"]), 3)

if __name__ == "__main__":
    if sys.argv[-1] == "-ut":
        unittest.main(argv=[" "])
    main()
