#!/usr/bin/env python
# paper.py - Codeforces.com 527A Paper quiz by Sergey 2015

# Standard modules
import unittest
import sys
import re

# Additional modules


###############################################################################
# Paper Class
###############################################################################


class Paper:
    """ Paper representation """

    def __init__(self, args):
        """ Default constructor """

        self.args = args
        self.cur = self.args
        self.num = 0

    def iterate(self):

        # Re-order with higher number first
        if self.cur[0] < self.cur[1]:
            self.cur = (self.cur[1],  self.cur[0])

        # calculate
        self.num += self.cur[0] // self.cur[1]
        remainder = self.cur[0] % self.cur[1]
        self.cur = (remainder, self.cur[1])

        return 1 if remainder else 0

    def calculate(self):
        """ Main calcualtion function of the class """
        while self.iterate():
            pass
        return self.num

###############################################################################
# Executable code
###############################################################################


def decode_inputs(inputs):
    """ Decoding input string tuple into base class args tuple """

    # Decoding input into a tuple of integers
    ilist = [int(i) for i in inputs.split()]
    args = tuple(ilist)

    return args


def calculate(inputs):
    """ Base class calculate method wrapper """
    return Paper(decode_inputs(inputs)).calculate()


def main():
    """ Main function. Not called by unit tests """

    # Read test input string tuple
    inputs = (input())

    # Print the result
    print(calculate(inputs))

###############################################################################
# Unit Tests
###############################################################################


class unitTests(unittest.TestCase):

    def test_decode_inputs(self):
        """ Input string decoding testing """
        self.assertEqual(decode_inputs("2 5"), (2, 5))

    def test_Paper_class__basic_functions(self):
        """ Paper class basic functions testing """
        d = Paper((1, 2))
        self.assertEqual(d.args[0], 1)

        # Iteration variable
        self.assertEqual(d.cur[0], 1)

        # Iterate on a square sheet, return 0 - finished
        d = Paper((2, 2))
        self.assertEqual(d.iterate(), 0)
        self.assertEqual(d.num, 1)

        # Iterate on a rect sheet, return 1 - not finished
        d = Paper((10, 3))
        self.assertEqual(d.iterate(), 1)
        self.assertEqual(d.cur, (1, 3))
        self.assertEqual(d.num, 3)

    def test_calculate(self):
        """ Main calculation function """

        # Sample test 1
        self.assertEqual(calculate("2 2"), 1)

        # Sample test 2
        self.assertEqual(calculate("10 3"), 6)

        # Other tests
        self.assertEqual(calculate("10 7"), 6)
        self.assertEqual(calculate("1000000000000 1"), 1000000000000)


if __name__ == "__main__":
    if sys.argv[-1] == "-ut":
        unittest.main(argv=[" "])
    main()
