#!/usr/bin/env python3
# 669C_matrix.py - Codeforces.com/problemset/problem/669/C by Sergey 2016

import unittest
import sys

###############################################################################
# Matrix Class (Main Program)
###############################################################################


class Matrix:
    """ Matrix representation """

    def __init__(self, test_inputs=None):
        """ Default constructor """

        it = iter(test_inputs.split("\n")) if test_inputs else None

        def uinput():
            return next(it) if it else sys.stdin.readline().rstrip()

        # Reading single elements
        [self.n, self.m, self.q] = map(int, uinput().split())

        # Reading a single line of multiple elements
        self.nums = []
        for i in range(self.q):
            self.nums.append(list(map(int, uinput().split())))

    def calculate(self):
        """ Main calcualtion function of the class """

        matrix = []
        for r in range(self.n):
            row = [0] * self.m
            matrix.append(row)

        for cmd in reversed(self.nums):
            if cmd[0] == 3:
                matrix[cmd[1]-1][cmd[2]-1] = cmd[3]
            elif cmd[0] == 1:
                rep = matrix[cmd[1]-1][-1]
                for i in range(self.m):
                    matrix[cmd[1]-1][i], rep = rep, matrix[cmd[1]-1][i]
            elif cmd[0] == 2:
                rep = matrix[-1][cmd[1]-1]
                for i in range(self.n):
                    matrix[i][cmd[1]-1], rep = rep, matrix[i][cmd[1]-1]

        rows = [" ".join(map(str, row)) for row in matrix]
        result = "\n".join(rows)

        return str(result)

###############################################################################
# Unit Tests
###############################################################################


class unitTests(unittest.TestCase):

    def test_single_test(self):
        """ Matrix class testing """

        # Constructor test
        test = "2 2 6\n2 1\n2 2\n3 1 1 1\n3 2 2 2\n3 1 2 8\n3 2 1 8"
        d = Matrix(test)
        self.assertEqual(d.n, 2)
        self.assertEqual(d.m, 2)
        self.assertEqual(d.q, 6)
        self.assertEqual(d.nums[0], [2, 1])

        # Sample test
        self.assertEqual(Matrix(test).calculate(), "8 2\n1 8")

        # Sample test
        test = "3 3 2\n1 2\n3 2 2 5"
        self.assertEqual(Matrix(test).calculate(), "0 0 0\n0 0 5\n0 0 0")

        # Sample test
        test = ""
        # self.assertEqual(Matrix(test).calculate(), "0")

        # My tests
        test = ""
        # self.assertEqual(Matrix(test).calculate(), "0")

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
        d = Matrix(test)
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
    sys.stdout.write(Matrix().calculate())
