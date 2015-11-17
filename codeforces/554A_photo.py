#!/usr/bin/env python3
# 554A_photo.py - Codeforces.com/problemset/problem/554/A Photo quiz by Sergey 2015

# Standard modules
import unittest
import sys
import re

# Additional modules


###############################################################################
# Photo Class
###############################################################################


class Photo:
    """ Photo representation """

    LC = 'abcdefghijklmnopqrstuvwxyz'

    def __init__(self, args):
        """ Default constructor """

        self.list = args
        self.str = args

    def insert(self, i, c):
        l = list(self.str)
        l.insert(i, c)
        return ''.join(l)

    def calculate(self):
        """ Main calcualtion function of the class """

        s = set()
        # Brute force loop
        for i in range(len(self.str) + 1):
            for c in list(self.LC):
                s.add(self.insert(i, c))

        return len(s)

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
    str = uinput()

    return str


def calculate(test_inputs=None):
    """ Base class calculate method wrapper """
    return Photo(get_inputs(test_inputs)).calculate()


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
        self.assertEqual(get_inputs(["a"]), "a")

    def test_Photo_class__basic_functions(self):
        """ Photo class basic functions testing """
        d = Photo("a")
        self.assertEqual(d.str, "a")

        self.assertEqual(d.insert(0, "b"), "ba")

    def test_calculate(self):
        """ Main calculation function """

        # Sample tests
        self.assertEqual(calculate(["a"]), 51)
        self.assertEqual(calculate(["hi"]), 76)

if __name__ == "__main__":
    if sys.argv[-1] == "-ut":
        unittest.main(argv=[" "])
    main()
