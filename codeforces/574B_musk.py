#!/usr/bin/env python
# 574B_musk.py - Codeforces.com/problemset/problem/574/B Musk program by Sergey 2015

import unittest
import sys

###############################################################################
# Musk Class
###############################################################################


class Musk:
    """ Musk representation """

    def __init__(self, test_inputs=None):
        """ Default constructor """

        it = iter(test_inputs.split("\n")) if test_inputs else None

        def uinput():
            return next(it) if it else sys.stdin.readline().rstrip()

        # Reading single elements
        self.n, self.m = map(int, uinput().split())

        # Reading multiple lines of pairs
        pairs = (" ".join(uinput() for i in range(self.m))).split()
        self.numa = [int(pairs[i])-1 for i in range(0, 2*self.m, 2)]
        self.numb = [int(pairs[i])-1 for i in range(1, 2*self.m, 2)]

        # Array of sets
        self.sets = [set() for i in range(self.n)]
        for i in range(self.m):
            self.sets[self.numa[i]].add(self.numb[i])
            self.sets[self.numb[i]].add(self.numa[i])

        MAX = 10000000000000000
        self.min_rank = MAX
        for i in range(self.n):
            for j in self.sets[i]:
                if j > i:
                    un = len(self.sets[i]) + len(self.sets[j])
                    intersect = self.sets[i].intersection(self.sets[j])
                    for s in intersect:
                        uns = un + len(self.sets[s])
                        rank = uns - 6
                        if rank < self.min_rank:
                            self.min_rank = rank
        if self.min_rank == MAX:
            self.min_rank = -1

    def calculate(self):
        """ Main calcualtion function of the class """

        result = self.min_rank

        return str(result)

###############################################################################
# Unit Tests
###############################################################################


class unitTests(unittest.TestCase):

    def test_single_test(self):
        """ Musk class testing """

        # Constructor test
        test = "5 6\n1 2\n1 3\n2 3\n2 4\n3 4\n4 5"
        d = Musk(test)
        self.assertEqual(d.n, 5)
        self.assertEqual(d.m, 6)
        self.assertEqual(d.numa, [0, 0, 1, 1, 2, 3])
        self.assertEqual(d.numb, [1, 2, 2, 3, 3, 4])

        self.assertEqual(d.sets[0], {1, 2})
        self.assertEqual(d.sets[3], {1, 2, 4})

        # Sample test
        self.assertEqual(Musk(test).calculate(), "2")

        # Sample test
        test = "7 4\n2 1\n3 6\n5 1\n1 7"
        self.assertEqual(Musk(test).calculate(), "-1")

        # Sample test
        test = "1\n1 2\n1"
        # self.assertEqual(Musk(test).calculate(), "0")

        # My tests
        test = "1\n1 2\n1"
        # self.assertEqual(Musk(test).calculate(), "0")

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
        d = Musk(test)
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
    sys.stdout.write(Musk().calculate())
