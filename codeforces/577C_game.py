#!/usr/bin/env python
# 577C_game.py - Codeforces.com/problemset/problem/577/C by Sergey 2015

import unittest
import sys

###############################################################################
# Game Class (Main Program)
###############################################################################


class Game:
    """ Game representation """

    def __init__(self, test_inputs=None):
        """ Default constructor """

        it = iter(test_inputs.split("\n")) if test_inputs else None

        def uinput():
            return next(it) if it else sys.stdin.readline().rstrip()

        # Reading single elements
        [self.n] = map(int, uinput().split())

        self.sieve(self.n)

    def sieve(self, n):
        self.pf = [0] * (n+1)
        i = 2
        while i*i <= n:
            if self.pf[i] == 0:
                j = i*i
                while j <= n:
                    self.pf[j] = i
                    j += i
            i += 1

    def factorize(self, n):
        result = {}
        while n > 1:
            pf = self.pf[n]
            if pf == 0:
                pf = n
            if pf not in result.keys():
                result[pf] = 0
            result[pf] += 1
            n = n // pf
        return result

    def calculate(self):
        """ Main calcualtion function of the class """

        result = []
        for (i, k) in enumerate(self.pf):
            if k != 0 or i < 2:
                continue
            cur = i
            while cur <= self.n:
                result.append(cur)
                cur *= i

        return str(len(result)) + "\n" + " ".join(map(str, result))

###############################################################################
# Unit Tests
###############################################################################


class unitTests(unittest.TestCase):

    def test_single_test(self):
        """ Game class testing """

        # Constructor test
        test = "4"
        d = Game(test)
        self.assertEqual(d.n, 4)

        d = Game("1000")
        self.assertEqual(d.pf[:5], [0, 0, 0, 0, 2])
        self.assertEqual(d.factorize(40), {2: 3, 5: 1})

        # Sample test
        self.assertEqual(Game(test).calculate(), "3\n2 4 3")

        # Sample test
        test = "6"
        self.assertEqual(Game(test).calculate(), "4\n2 4 3 5")

        # Sample test
        test = ""
        # self.assertEqual(Game(test).calculate(), "0")

        # My tests
        test = ""
        # self.assertEqual(Game(test).calculate(), "0")

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
        d = Game(test)
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
    sys.stdout.write(Game().calculate())
