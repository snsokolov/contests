#!/usr/bin/env python3
# table.py - Codeforces.com/problemset/problem/552/A Table quiz by Sergey 2015

# Standard modules
import unittest
import sys
import re

# Additional modules


###############################################################################
# Table Class
###############################################################################


class Table:
    """ Table representation """

    N = 100

    def __init__(self, args):
        """ Default constructor """

        self.args = args
        self.starts = args[1]
        self.ends = args[2]

    def calculate(self):
        """ Main calcualtion function of the class """
        sum = 0
        for y in range(1, self.N+2):
            for x in range(1, self.N+2):
                for (start, end) in zip(self.starts, self.ends):
                    inside = (
                        x >= start[0] and y >= start[1] and
                        x <= end[0] and y <= end[1])
                    if inside:
                        sum += 1
        return sum


###############################################################################
# Executable code
###############################################################################


def decode_inputs(inputs):
    """ Decoding input string list into base class args list """

    num = int(inputs[0])

    # Decoding input into a list of integers
    ilist = [[int(n) for n in i.split()] for i in inputs[1:]]
    starts = [(rec[0], rec[1]) for rec in ilist]
    ends = [(rec[2], rec[3]) for rec in ilist]

    args = [num, starts, ends]

    return args


def calculate(inputs):
    """ Base class calculate method wrapper """
    return Table(decode_inputs(inputs)).calculate()


def main():
    """ Main function. Not called by unit tests """

    # Read test input string list
    n = input()
    squares = [input() for i in range(int(n))]

    inputs = [n, squares]

    # Print the result
    print(calculate(inputs))

###############################################################################
# Unit Tests
###############################################################################


class unitTests(unittest.TestCase):

    def test_decode_inputs(self):
        """ Input string decoding testing """
        self.assertEqual(
            decode_inputs(["2", "1 2 3 4", "5 6 7 8"]),
            [2, [(1, 2), (5, 6)], [(3, 4), (7, 8)]])

    def test_Table_class__basic_functions(self):
        """ Table class basic functions testing """
        d = Table([1, [(1, 1)], [(2, 2)]])
        self.assertEqual(d.args[0], 1)

        # Calculate function
        self.assertEqual(d.calculate(), 4)

    def test_calculate(self):
        """ Main calculation function """

        # Sample tests
        self.assertEqual(calculate(["2", "1 1 2 3", "2 2 3 3"]), 10)
        self.assertEqual(calculate(["2", "1 1 3 3", "1 1 3 3"]), 18)

if __name__ == "__main__":
    if sys.argv[-1] == "-ut":
        unittest.main(argv=[" "])
    main()
