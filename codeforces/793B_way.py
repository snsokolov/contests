#!/usr/bin/env python3
# 793B_way.py - Codeforces.com/problemset/problem/793/B by Sergey 2017

import unittest
import sys

###############################################################################
# Way Class (Main Program)
###############################################################################


class Way:
    """ Way representation """

    def __init__(self, test_inputs=None):
        """ Default constructor """

        it = iter(test_inputs.split("\n")) if test_inputs else None

        def uinput():
            return next(it) if it else sys.stdin.readline().rstrip()

        # Reading single elements
        [self.n, self.m] = map(int, uinput().split())

        # Reading the grid into a single line
        self.line = "".join(uinput() for i in range(self.n))

        self.grid = []
        for col in range(self.m):
            self.grid.append([0] * self.n)
            for row in range(self.n):
                symb = self.line[(row * self.m) + col]
                if symb == "*":
                    self.grid[col][row] = 1
                else:
                    self.grid[col][row] = 0
                    if symb == "S":
                        self.start = (col, row)
                    if symb == "T":
                        self.end = (col, row)

        # Cells linked to the start
        self.start_linkedx = self.get_linkedx(self.start)
        self.start_linkedy = self.get_linkedy(self.start)

        # Cells linked to the end
        self.end_linkedx = self.get_linkedx(self.end)
        self.end_linkedy = self.get_linkedy(self.end)

        self.linkedx = list(
            set(self.start_linkedx).intersection(self.end_linkedx))
        self.linkedy = list(
            set(self.start_linkedy).intersection(self.end_linkedy))

    def is_linked(self, start, end):
        if start[0] != end[0] and start[1] != end[1]:
            return False
        if self.grid[start[0]][start[1]]:
            return False
        if self.grid[end[0]][end[1]]:
            return False
        if start[0] == end[0]:
            y = min(start[1], end[1]) + 1
            while y < max(start[1], end[1]):
                if self.grid[start[0]][y]:
                    return False
                y += 1
        if start[1] == end[1]:
            x = min(start[0], end[0]) + 1
            while x < max(start[0], end[0]):
                if self.grid[x][start[1]]:
                    return False
                x += 1
        return True

    def get_linkedx(self, start):
        result = []
        y = start[1]
        for x in range(start[0], -1, -1):
            if self.grid[x][y]:
                break
            result.append(x)
        for x in range(start[0] + 1, self.m):
            if self.grid[x][y]:
                break
            result.append(x)
        return sorted(result)

    def get_linkedy(self, start):
        result = []
        x = start[0]
        for y in range(start[1], -1, -1):
            if self.grid[x][y]:
                break
            result.append(y)
        for y in range(start[1] + 1, self.n):
            if self.grid[x][y]:
                break
            result.append(y)
        return sorted(result)

    def calculate(self):
        """ Main calcualtion function of the class """

        result = "NO"

        for x in self.linkedx:
            if self.is_linked((x, self.start[1]), (x, self.end[1])):
                result = "YES"
                break
        for y in self.linkedy:
            if self.is_linked((self.start[0], y), (self.end[0], y)):
                result = "YES"
                break

        return str(result)

###############################################################################
# Unit Tests
###############################################################################


class unitTests(unittest.TestCase):

    def test_single_test(self):
        """ Way class testing """

        # Constructor test
        test = "5 5\n..S..\n****.\nT....\n****.\n....."
        d = Way(test)
        self.assertEqual(d.n, 5)
        self.assertEqual(d.m, 5)
        self.assertEqual(d.line, "..S..****.T....****......")
        self.assertEqual(d.grid[0][0], 0)  # Empty cell
        self.assertEqual(d.grid[0][1], 1)  # Road work
        self.assertEqual(d.start, (2, 0))
        self.assertEqual(d.end, (0, 2))

        self.assertEqual(d.is_linked((0, 0), (1, 1)), False)
        self.assertEqual(d.is_linked((0, 0), (4, 0)), True)
        self.assertEqual(d.is_linked((0, 0), (0, 1)), False)
        self.assertEqual(d.is_linked((0, 0), (0, 2)), False)

        self.assertEqual(d.get_linkedx((0, 0)), [0, 1, 2, 3, 4])
        self.assertEqual(d.get_linkedy((0, 0)), [0])

        self.assertEqual(d.start_linkedx, [0, 1, 2, 3, 4])
        self.assertEqual(d.end_linkedx, [0, 1, 2, 3, 4])
        self.assertEqual(d.linkedx, [0, 1, 2, 3, 4])

        # Sample test
        self.assertEqual(Way(test).calculate(), "YES")

        # Sample test
        test = "5 5\nS....\n****.\n.....\n.****\n..T.."
        self.assertEqual(Way(test).calculate(), "NO")

        # Sample test
        test = ""
        # self.assertEqual(Way(test).calculate(), "0")

        # My tests
        test = ""
        # self.assertEqual(Way(test).calculate(), "0")

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
        d = Way(test)
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
    sys.stdout.write(Way().calculate())
