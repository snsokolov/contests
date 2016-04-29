#!/usr/bin/env python3
# 629A_cake.py - Codeforces.com/problemset/problem/629/A by Sergey 2016

import unittest
import sys

###############################################################################
# Cake Class (Main Program)
###############################################################################


class Cake:
    """ Cake representation """

    def __init__(self, test_inputs=None):
        """ Default constructor """

        it = iter(test_inputs.split("\n")) if test_inputs else None

        def uinput():
            return next(it) if it else sys.stdin.readline().rstrip()

        # Reading single elements
        [self.n] = map(int, uinput().split())

        # Reading multiple number of lines of the same number of elements each
        l, s = self.n, self.n
        inp = list("".join(uinput() for i in range(l)))
        self.numm = (
            [[inp[i] == 'C' for i in range(j, l*s, s)] for j in range(s)])

        self.numr = []
        for i in range(self.n):
            s = 0
            for j in range(self.n):
                s += self.numm[j][i]
            self.numr.append(s*(s-1)//2)

        self.numc = []
        for i in range(self.n):
            s = 0
            for j in range(self.n):
                s += self.numm[i][j]
            self.numc.append(s*(s-1)//2)

    def calculate(self):
        """ Main calcualtion function of the class """

        result = sum(self.numc) + sum(self.numr)

        return str(result)

###############################################################################
# Unit Tests
###############################################################################


class unitTests(unittest.TestCase):

    def test_single_test(self):
        """ Cake class testing """

        # Constructor test
        test = "3\n.CC\nC..\nC.C"
        d = Cake(test)
        self.assertEqual(d.n, 3)
        self.assertEqual(d.numm, [[0, 1, 1], [1, 0, 0], [1, 0, 1]])
        self.assertEqual(d.numr, [1, 0, 1])
        self.assertEqual(d.numc, [1, 0, 1])

        # Sample test
        self.assertEqual(Cake(test).calculate(), "4")

        # Sample test
        test = "4\nCC..\nC..C\n.CC.\n.CC."
        self.assertEqual(Cake(test).calculate(), "9")

        # Sample test
        test = ""
        # self.assertEqual(Cake(test).calculate(), "0")

        # My tests
        test = ""
        # self.assertEqual(Cake(test).calculate(), "0")

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
        d = Cake(test)
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
    sys.stdout.write(Cake().calculate())
