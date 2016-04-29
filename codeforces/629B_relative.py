#!/usr/bin/env python3
# 629B_relative.py - Codeforces.com/problemset/problem/629/B by Sergey 2016

import unittest
import sys

###############################################################################
# Relative Class (Main Program)
###############################################################################


class Relative:
    """ Relative representation """

    def __init__(self, test_inputs=None):
        """ Default constructor """

        it = iter(test_inputs.split("\n")) if test_inputs else None

        def uinput():
            return next(it) if it else sys.stdin.readline().rstrip()

        # Reading single elements
        [self.n] = map(int, uinput().split())

        # Reading multiple number of lines of the same number of elements each
        l, s = self.n, 3
        inp = (" ".join(uinput() for i in range(l))).split()
        self.numm = [[(int(inp[i]) if j != 0 else inp[i] == 'M')
                     for i in range(j, l*s, s)] for j in range(s)]
        self.nums, self.numa, self.numb = self.numm

        self.dts = []
        for i in range(self.n):
            self.dts.append((self.numa[i], 1, self.nums[i]))
            self.dts.append((self.numb[i]+1, 0, self.nums[i]))
        self.sdts = sorted(self.dts)

        mcnt, fcnt = 0, 0
        self.ms, self.fs = {}, {}
        for i in range(len(self.sdts)):
            day = self.sdts[i][0]
            if self.sdts[i][2]:
                if self.sdts[i][1]:
                    mcnt += 1
                else:
                    mcnt -= 1
            else:
                if self.sdts[i][1]:
                    fcnt += 1
                else:
                    fcnt -= 1
            self.ms[day] = mcnt
            self.fs[day] = fcnt
        self.cr = []
        for d in self.ms:
            self.cr.append(min(self.ms[d], self.fs[d])*2)

    def calculate(self):
        """ Main calcualtion function of the class """

        result = max(self.cr)

        return str(result)

###############################################################################
# Unit Tests
###############################################################################


class unitTests(unittest.TestCase):

    def test_single_test(self):
        """ Relative class testing """

        # Constructor test
        test = "4\nM 151 307\nF 343 352\nF 117 145\nM 24 128"
        d = Relative(test)
        self.assertEqual(d.n, 4)
        self.assertEqual(d.numa, [151, 343, 117, 24])
        self.assertEqual(d.nums, [1, 0, 0, 1])

        # Sample test
        self.assertEqual(Relative(test).calculate(), "2")

        # Sample test
        test = "6\nM 128 130\nF 128 131\nF 131 140\nF 131 141\nM 131 200\nM 140 200"
        self.assertEqual(Relative(test).calculate(), "4")

        # Sample test
        test = ""
        # self.assertEqual(Relative(test).calculate(), "0")

        # My tests
        test = ""
        # self.assertEqual(Relative(test).calculate(), "0")

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
        d = Relative(test)
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
    sys.stdout.write(Relative().calculate())
