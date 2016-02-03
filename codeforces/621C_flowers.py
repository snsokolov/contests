#!/usr/bin/env python3
# 621C_flowers.py - Codeforces.com/problemset/problem/621/C by Sergey 2016

import unittest
import sys

###############################################################################
# Flowers Class (Main Program)
###############################################################################


class Flowers:
    """ Flowers representation """

    def __init__(self, test_inputs=None):
        """ Default constructor """

        it = iter(test_inputs.split("\n")) if test_inputs else None

        def uinput():
            return next(it) if it else sys.stdin.readline().rstrip()

        # Reading single elements
        [self.n, self.p] = map(int, uinput().split())

        # Reading multiple number of lines of the same number of elements each
        l, s = self.n, 2
        inp = (" ".join(uinput() for i in range(l))).split()
        self.numm = [[int(inp[i]) for i in range(j, l*s, s)] for j in range(s)]
        self.numa, self.numb = self.numm

    def prob(self, l, r, p):
        """ Probability of a number in range divided by prime """
        w = r - l + 1
        lm = l % p
        rm = r % p
        n = (r - rm - (l - lm)) // p
        if lm == 0:
            n += 1
        return n / w

    def calculate(self):
        """ Main calcualtion function of the class """

        self.pr = []
        for i in range(self.n):
            self.pr.append(1 - self.prob(self.numa[i], self.numb[i], self.p))

        result = 0
        prev = self.pr[-1]
        for p in self.pr:
            result += (1 - p*prev)
            prev = p

        return str(result*2000)

###############################################################################
# Unit Tests
###############################################################################


class unitTests(unittest.TestCase):

    def test_single_test(self):
        """ Flowers class testing """

        # Constructor test
        test = "3 2\n1 2\n420 421\n420420 420421"
        d = Flowers(test)
        self.assertEqual(d.n, 3)
        self.assertEqual(d.p, 2)
        self.assertEqual(d.numa, [1, 420, 420420])
        self.assertEqual(d.prob(2, 5, 3), 0.25)
        self.assertEqual(d.prob(2, 3, 3), 0.5)
        self.assertEqual(d.prob(3, 4, 3), 0.5)
        self.assertEqual(d.prob(3, 3, 3), 1)
        self.assertEqual(d.prob(1, 4, 5), 0)

        # Sample test
        self.assertEqual(Flowers(test).calculate(), "4500.0")

        # Sample test
        test = "3 5\n1 4\n2 3\n11 14"
        self.assertEqual(Flowers(test).calculate(), "0.0")

        # Sample test
        test = ""
        # self.assertEqual(Flowers(test).calculate(), "0")

        # My tests
        test = ""
        # self.assertEqual(Flowers(test).calculate(), "0")

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
        d = Flowers(test)
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
    sys.stdout.write(Flowers().calculate())
