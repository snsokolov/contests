#!/usr/bin/env python
# books.py - Codeforces.com 552B Books quiz by Sergey 2015
#
# Copyright (C) 2015 Sergey

# Standard modules
import unittest
import sys
import re

# Additional modules


###############################################################################
# Books Class
###############################################################################


class Books:
    """ Books representation """

    def __init__(self, args):
        """ Default constructor """

        self.args = args
        self.books = args[0]

    def lowest(self, num):
        return(int(pow(10, (num - 1))))

    def highest(self, num):
        return(self.lowest(num + 1) - 1)

    def calculate(self):
        """ Main calcualtion function of the class """
        result = 0
        for n in range(11):
            h = self.highest(n)
            l = self.lowest(n)
            if self.books >= l:
                if self.books >= h:
                    result += n * (h - l + 1)
                else:
                    result += n * (self.books - l + 1)
        return result


###############################################################################
# Executable code
###############################################################################


def decode_inputs(inputs):
    """ Decoding input string list into base class args list """

    # Decoding input into a list of integers
    ilist = [int(i) for i in inputs[0].split()]

    return ilist


def calculate(inputs):
    """ Base class calculate method wrapper """
    return Books(decode_inputs(inputs)).calculate()


def main():
    """ Main function. Not called by unit tests """

    # Read test input string list
    inputs = [input()]

    # Print the result
    print(calculate(inputs))

###############################################################################
# Unit Tests
###############################################################################


class unitTests(unittest.TestCase):

    def test_decode_inputs(self):
        """ Input string decoding testing """
        self.assertEqual(decode_inputs("2"), [2])

    def test_Books_class__basic_functions(self):
        """ Books class basic functions testing """
        d = Books([1])
        self.assertEqual(d.books, 1)

        # lowest number
        self.assertEqual(d.lowest(1), 1)
        self.assertEqual(d.lowest(3), 100)

        # Highest
        self.assertEqual(d.highest(2), 99)

    def test_calculate(self):
        """ Main calculation function """

        # Sample tess
        self.assertEqual(calculate(["13"]), 17)
        self.assertEqual(calculate(["20"]), 31)

if __name__ == "__main__":
    if sys.argv[-1] == "-ut":
        unittest.main(argv=[" "])
    main()
