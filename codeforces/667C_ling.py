#!/usr/bin/env python3
# 667C_ling.py - Codeforces.com/problemset/problem/667/C by Sergey 2016

import unittest
import sys
from collections import deque

###############################################################################
# Ling Class (Main Program)
###############################################################################


class Ling:
    """ Ling representation """

    def __init__(self, test_inputs=None):
        """ Default constructor """

        it = iter(test_inputs.split("\n")) if test_inputs else None

        def uinput():
            return next(it) if it else sys.stdin.readline().rstrip()

        # Reading single elements
        self.s = uinput()

    def calculate(self):
        """ Main calcualtion function of the class """

        chars = list(self.s)
        slen = len(chars)
        result = set([])
        vis = set([])
        q = deque([(0, "")])
        while q:
            pos, prev = q.popleft()
            if pos in vis:
                continue
            pos2 = pos + 2
            if slen - pos2 > 4:
                new = str(chars[slen-1-pos-1]) + str(chars[slen-1-pos])
                if new != prev:
                    result.add(new)
                    q.append((pos2, new))
            pos3 = pos + 3
            if slen - pos3 > 4:
                new = (str(chars[slen-1-pos-2]) +
                       str(chars[slen-1-pos-1]) + str(chars[slen-1-pos]))
                if new != prev:
                    result.add(new)
                    q.append((pos3, new))

            vis.add(pos)

        return (str(len(result)) + "\n" + "\n".join(sorted(result))
                if result else "0")

###############################################################################
# Unit Tests
###############################################################################


class unitTests(unittest.TestCase):

    def test_single_test(self):
        """ Ling class testing """

        # Constructor test
        test = "abacabaca"
        d = Ling(test)
        self.assertEqual(d.s, "abacabaca")

        # Sample test
        self.assertEqual(Ling(test).calculate(), "3\naca\nba\nca")

        # Sample test
        test = "abaca"
        self.assertEqual(Ling(test).calculate(), "0")

        # My tests
        test = "fffffaafgfg"
        # self.assertEqual(Ling(test).calculate(), "0")

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
        d = Ling(test)
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
    sys.stdout.write(Ling().calculate())
