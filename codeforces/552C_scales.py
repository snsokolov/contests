#!/usr/bin/env python3
# scales.py - Codeforces.com/problemset/problem/552/C quiz by Sergey 2015

# Standard modules
import unittest
import sys
import re

# Additional modules


###############################################################################
# Scales Class
###############################################################################


class Scales:
    """ Scales representation """

    N = 100

    def __init__(self, args):
        """ Default constructor """

        self.args = args
        self.w = args[0]
        self.m = args[1]

        # Iterator starting position
        self.maxwp = self.calc_maxwp()
        self.it_min = 0
        self.it_max = int(3 ** (self.maxwp + 1)) - 1

        self.yes = 0

    def calc_maxwp(self):
        """ Max weight power """
        for p in range(self.N+1):
            if self.w ** p > self.m:
                return p

    def list2dec(self, it):
        result = 0
        for (n, i) in enumerate(it):
            result += i * int(3 ** n)
        return result

    def dec2list(self, dec):
        result = []
        remainder = dec
        for n in range(self.maxwp + 1):
            pow = int(3 ** (self.maxwp - n))
            div = remainder // pow
            remainder -= div * pow
            result.insert(0, div)
        return result

    def step(self):
        """ Step to the next iteration """
        mid = (self.it_max + self.it_min)//2

        if mid in (self.it_max, self.it_min):
            return 0

        w = self.calc_weight(mid)
        if w > self.m:
            self.it_max = mid
        elif w < self.m:
            self.it_min = mid
        else:
            self.yes = 1
            return 0

        return 1

    def calc_weight(self, dec):
        result = 0
        it = self.dec2list(dec)
        for i in range(len(it)):
            s = it[i]
            w = self.w ** i
            if s == 2:
                result += w
            if s == 0:
                result -= w
        return result

    def calculate(self):
        """ Main calcualtion function of the class """

        while self.step():
            pass

        return "YES" if self.yes else "NO"

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
    return Scales(decode_inputs(inputs)).calculate()


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
        self.assertEqual(decode_inputs(["2 5"]), [2, 5])

    def test_Scales_class__basic_functions(self):
        """ Scales class basic functions testing """
        d = Scales([3, 7])
        self.assertEqual(d.w, 3)
        self.assertEqual(d.m, 7)

        # Find the maximum size (power) of the weight we are need
        self.assertEqual(d.maxwp, 2)

        # Base 3 Iterator value, digits: 0 - -, 1 - 0, 2 - "+"
        self.assertEqual(d.list2dec([1, 0, 2]), 19)
        self.assertEqual(d.dec2list(19), [1, 0, 2])

        # Check starting iterator
        d = Scales([2, 3])
        self.assertEqual(d.it_min, 0)
        self.assertEqual(d.it_max, 26)

        # Step function 1 - success, 0 - final step
        d = Scales([2, 3])
        self.assertEqual(d.step(), 1)
        self.assertEqual(d.it_min, 13)
        self.assertEqual(d.it_max, 26)

        # Weight from the iterator
        d = Scales([3, 7])
        self.assertEqual(d.calc_weight(d.list2dec([0, 1, 2])), 8)

    def test_calculate(self):
        """ Main calculation function """

        # Sample test 1
        self.assertEqual(calculate(["3 7"]), "YES")

        # Sample test 1
        self.assertEqual(calculate(["100 99"]), "YES")

        # Sample test 1
        self.assertEqual(calculate(["2 92600"]), "YES")

if __name__ == "__main__":
    if sys.argv[-1] == "-ut":
        unittest.main(argv=[" "])
    main()
