#!/usr/bin/env python3
# 664C_olymp.py - Codeforces.com/problemset/problem/664/C by Sergey 2016

import unittest
import sys
import re

###############################################################################
# Olymp Class (Main Program)
###############################################################################


class Olymp:
    """ Olymp representation """

    def __init__(self, test_inputs=None):
        """ Default constructor """

        it = iter(test_inputs.split("\n")) if test_inputs else None

        def uinput():
            return next(it) if it else sys.stdin.readline().rstrip()

        # Reading single elements
        [self.n] = map(int, uinput().split())

        # Reading a single line of multiple elements
        self.nums = []
        for i in range(self.n):
            strs = uinput()
            m = re.search("(\d+)", strs)
            if m:
                self.nums.append(m.group(1))

        used = set([])
        self.years = dict()
        self.revyears = dict()
        for i in range(1989, 10000):
            cur = i
            yr = str(cur % 10)
            while yr in used:
                cur //= 10
                yr = str(cur % 10) + yr
            used.add(yr)
            self.years[i] = yr
            self.revyears[yr] = i

    def translate(self, s):
        if len(s) <= 3:
            return self.revyears[s]
        else:
            if(int(s[0:4]) > 1989 and int(s[0:4]) < 9999):
                s = "1" + s
                return(int(s))
            else:
                return int(s)

    def calculate(self):
        """ Main calcualtion function of the class """

        outs = map(str, map(self.translate, self.nums))
        result = "\n".join(outs)

        return str(result)

###############################################################################
# Unit Tests
###############################################################################


class unitTests(unittest.TestCase):

    def test_single_test(self):
        """ Olymp class testing """

        # Constructor test
        test = "5\nIAO'15\nIAO'2015\nIAO'1\nIAO'9\nIAO'0"
        d = Olymp(test)
        self.assertEqual(d.n, 5)
        self.assertEqual(d.nums[0:2], ["15", "2015"])

        # Sample test
        self.assertEqual(
            Olymp(test).calculate(), "2015\n12015\n1991\n1989\n1990")

        # Sample test
        test = "4\nIAO'9\nIAO'99\nIAO'999\nIAO'9999"
        self.assertEqual(Olymp(test).calculate(), "1989\n1999\n2999\n9999")

        # Sample test
        test = ""
        # self.assertEqual(Olymp(test).calculate(), "0")

        # My tests
        test = ""
        # self.assertEqual(Olymp(test).calculate(), "0")

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
        d = Olymp(test)
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
    sys.stdout.write(Olymp().calculate())
