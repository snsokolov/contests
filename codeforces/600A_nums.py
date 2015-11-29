#!/usr/bin/env python3
# 600A_nums.py - Codeforces.com/problemset/problem/600/A by Sergey 2015

import unittest
import sys
import re

###############################################################################
# Nums Class (Main Program)
###############################################################################


class Nums:
    """ Nums representation """

    def __init__(self, test_inputs=None):
        """ Default constructor """

        it = iter(test_inputs.split("\n")) if test_inputs else None

        def uinput():
            return next(it) if it else sys.stdin.readline().rstrip()

        # Reading single elements
        self.s = uinput()
        self.t = re.split(';|,', self.s)
        self.al = []
        self.bl = []
        for n in self.t:
            try:
                if str(int(n)) == n:
                    self.al.append(n)
                else:
                    self.bl.append(n)
            except:
                self.bl.append(n)

    def calculate(self):
        """ Main calcualtion function of the class """

        result = ""
        result += "-" if not self.al else ("\"" + ",".join(self.al) + "\"")
        result += "\n"
        result += "-" if not self.bl else ("\"" + ",".join(self.bl) + "\"")

        return result

###############################################################################
# Unit Tests
###############################################################################


class unitTests(unittest.TestCase):

    def test_single_test(self):
        """ Nums class testing """

        # Constructor test
        test = "aba,123;1a;0"
        d = Nums(test)

        # Sample test
        self.assertEqual(Nums(test).calculate(), "\"123,0\"\n\"aba,1a\"")

        # Sample test
        test = "1;;01,a0,"
        self.assertEqual(Nums(test).calculate(), "\"1\"\n\",01,a0,\"")

        # Sample test
        test = "1"
        self.assertEqual(Nums(test).calculate(), "\"1\"\n-")

        # My tests
        test = "a"
        self.assertEqual(Nums(test).calculate(), "-\n\"a\"")

        # Time limit test
        # self.time_limit_test(5000)

    def time_limit_test(self, nmax):
        """ Timelimit testing """
        import random
        import timeit

        # Random inputs
        test = str(nmax) + " " + str(nmax) + "\n"
        numnums = [str(i) + " " + str(i+1) for i in range(nmax)]
        test += "\n".join(numnums) + "\n"
        nums = [random.randint(1, 10000) for i in range(nmax)]
        test += " ".join(map(str, nums)) + "\n"

        # Run the test
        start = timeit.default_timer()
        d = Nums(test)
        calc = timeit.default_timer()
        d.calculate()
        stop = timeit.default_timer()
        print("\nTimelimit Test: " +
              "{0:.3f}s (init {1:.3f}s calc {2:.3f}s)".
              format(stop-start, calc-start, stop-calc))

if __name__ == "__main__":

    # Avoiding recursion limitaions
    sys.setrecursionlimit(100000)

    if sys.argv[-1] == "-ut":
        unittest.main(argv=[" "])

    # Print the result string
    sys.stdout.write(Nums().calculate())
