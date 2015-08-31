#!/usr/bin/env python
# 556D_fug.py - Codeforces.com 556D Fug quiz by Sergey 2015

# Standard modules
import unittest
import sys
import re

# Additional modules
import heapq


###############################################################################
# Fug Class
###############################################################################


class Fug:
    """ Fug representation """

    def __init__(self, args):
        """ Default constructor """
        self.list = args[0]
        self.alist = args[1]
        self.gn = len(self.list) - 1

        # Sorted list of bridges
        self.asrt = sorted((n, i) for i, n in enumerate(self.alist))

        # List of gaps between islands
        self.gaps = []
        prevli = self.list[0]
        for i in range(self.gn):
            li = self.list[i+1]
            min = li[0] - prevli[1]
            max = li[1] - prevli[0]
            self.gaps.append((min, max, i))
            prevli = li

        # Sorted list of gaps between islands
        self.gsrt = sorted(self.gaps)

        self.gmin = [n[0] for n in self.gsrt]
        self.result = [None]*self.gn
        self.heap = []

    def iterate(self):

        j = 0
        for (b, i) in self.asrt:

            # Traverse gmin array
            while j < self.gn and self.gmin[j] <= b:
                it = self.gsrt[j]
                heapq.heappush(self.heap, (it[1], it[0], it[2]))
                j += 1

            # Update result and remove the element from lists
            if self.heap:
                (mmax, mmin, mi) = self.heap[0]
                if mmin <= b and mmax >= b:
                    self.result[mi] = str(i + 1)
                    heapq.heappop(self.heap)

            yield

    def calculate(self):
        """ Main calcualtion function of the class """

        for it in self.iterate():
            pass

        for n in self.result:
            if n is None:
                return "No"
        answer = "Yes\n"
        answer += " ".join(self.result)

        return answer


###############################################################################
# Executable code
###############################################################################


def get_inputs(test_inputs=None):

    it = iter(test_inputs.split("\n")) if test_inputs else None

    def uinput():
        """ Unit-testable input function wrapper """
        if it:
            return next(it)
        else:
            return sys.stdin.readline()

    # Getting string inputs. Place all uinput() calls here
    num = [int(s) for s in uinput().split()]
    list = [[int(s) for s in uinput().split()] for i in range(num[0])]
    alist = [int(s) for s in uinput().split()]

    # Decoding inputs into a list
    inputs = [list, alist]

    return inputs


def calculate(test_inputs=None):
    """ Base class calculate method wrapper """
    return Fug(get_inputs(test_inputs)).calculate()


###############################################################################
# Unit Tests
###############################################################################


class unitTests(unittest.TestCase):

    def test_sample_tests(self):
        """ Quiz sample tests. Add \n to separate lines """

        # Sample test 1
        test = "4 4\n1 4\n7 8\n9 10\n12 14\n4 5 3 8"
        self.assertEqual(calculate(test), "Yes\n2 3 1")
        self.assertEqual(
            get_inputs(test),
            [[[1, 4], [7, 8], [9, 10], [12, 14]], [4, 5, 3, 8]])

        # My tests
        test = "5 5\n1 1\n2 7\n8 8\n10 10\n16 16\n1 1 5 6 2"
        self.assertEqual(calculate(test), "Yes\n1 2 5 4")

        # Other tests
        test = "2 2\n11 14\n17 18\n2 9"
        self.assertEqual(calculate(test), "No")

        # Other tests
        test = (
            "2 1\n1 1\n1000000000000000000 1000000000000000000" +
            "\n999999999999999999")
        self.assertEqual(calculate(test), "Yes\n1")

        test = ("5 9\n1 2\n3 3\n5 7\n11 13\n14 20\n2 3 4 10 6 2 6 9 5")
        self.assertEqual(calculate(test), "Yes\n1 6 3 2")

        size = 10000
        test = str(size) + " " + str(size) + "\n"
        x = size*1000
        for i in range(size):
            x += 2
            test += str(x) + " " + str(x+1) + "\n"
        for i in range(size):
            test += str(2) + " "
        self.assertEqual(calculate(test)[0], "Y")

    def test_Fug_class__basic_functions(self):
        """ Fug class basic functions testing """

        # Constructor test
        d = Fug([[[1, 5], [7, 8], [9, 10], [12, 14]], [4, 5, 3, 8]])
        self.assertEqual(d.list[0][0], 1)
        self.assertEqual(d.alist[0], 4)

        # Sort bridges
        self.assertEqual(d.asrt[0], (3, 2))

        # Sort Gaps
        self.assertEqual(d.gaps[0], (2, 7, 0))
        self.assertEqual(d.gsrt[0], (1, 3, 1))

        iter = d.iterate()
        next(iter)
        self.assertEqual(d.gmin, [1, 2, 2])
        self.assertEqual(d.heap, [(5, 2, 2), (7, 2, 0)])

if __name__ == "__main__":

    # Avoiding recursion limitaions
    sys.setrecursionlimit(100000)

    if sys.argv[-1] == "-ut":
        unittest.main(argv=[" "])

    # Print the result string
    sys.stdout.write(calculate())
