#!/usr/bin/env python3
# 580C_park.py - Codeforces.com/problemset/problem/580/C by Sergey 2015

import unittest
import sys
import collections

###############################################################################
# Park Class (Main Program)
###############################################################################


class Node:

    def __init__(self, i, n):
        self.i = i
        self.n = n
        self.children = []
        self.edges = []
        self.parent = -1

    def add_child(self, c):
        c.parent = self
        self.children.append(c)

    def add_edge(self, e):
        e.edges.append(self)
        self.edges.append(e)


class Park:
    """ Park representation """

    def __init__(self, test_inputs=None):
        """ Default constructor """

        it = iter(test_inputs.split("\n")) if test_inputs else None

        def uinput():
            return next(it) if it else sys.stdin.readline().rstrip()

        # Reading single elements
        [self.n, self.m] = map(int, uinput().split())

        # Reading a single line of multiple elements
        self.nums = list(map(int, uinput().split()))

        # Reading multiple number of lines of the same number of elements each
        l, s = self.n-1, 2
        inp = (" ".join(uinput() for i in range(l))).split()
        self.numm = [[int(inp[i]) for i in range(j, l*s, s)] for j in range(s)]
        self.numa, self.numb = self.numm

        # Building the tree
        self.nodes = [Node(i, self.nums[i]) for i in range(len(self.nums))]

        for i in range(len(self.numa)):
            self.nodes[self.numa[i]-1].add_edge(self.nodes[self.numb[i]-1])

    def calculate(self):
        """ Main calcualtion function of the class """

        result = 0

        # DFS to determine parent-child
        d = collections.deque([self.nodes[0]])
        visited = set()
        while d:
            v = d.pop()
            visited.add(v.i)
            for e in v.edges:
                if e.i not in visited:
                    v.add_child(e)
                    d.append(e)

        # DFS to calculate consecutive cats
        d = collections.deque([self.nodes[0]])
        while d:
            v = d.pop()
            v.cons = v.n if v.i == 0 else (v.parent.cons + 1 if v.n else 0)
            if v.cons <= self.m:
                d.extend(v.children)
                if not v.children:
                    result += 1

        return str(result)

###############################################################################
# Unit Tests
###############################################################################


class unitTests(unittest.TestCase):

    def test_single_test(self):
        """ Park class testing """

        # Constructor test
        test = "4 1\n1 1 0 0\n1 2\n1 3\n1 4"
        d = Park(test)
        self.assertEqual(d.n, 4)
        self.assertEqual(d.m, 1)
        self.assertEqual(d.numa, [1, 1, 1])
        self.assertEqual(d.numb, [2, 3, 4])
        self.assertEqual(d.nums, [1, 1, 0, 0])

        # Sample test
        self.assertEqual(Park(test).calculate(), "2")

        # Sample test
        test = "7 1\n1 0 0 1 0 0 1\n1 2\n1 7\n2 4\n2 5\n6 3\n7 3"
        self.assertEqual(Park(test).calculate(), "2")

        # Sample test
        test = "7 1\n0 0 1 1 0 0 1\n1 2\n1 3\n2 4\n2 5\n3 6\n3 7"
        self.assertEqual(Park(test).calculate(), "3")

        # My tests
        test = ""
        # self.assertEqual(Park(test).calculate(), "0")

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
        d = Park(test)
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
    sys.stdout.write(Park().calculate())
