#!/usr/bin/env python3
# 580B_company.py - Codeforces.com/problemset/problem/580/B by Sergey 2015

import unittest
import sys

###############################################################################
# Company Class (Main Program)
###############################################################################


class Company:
    """ Company representation """

    def __init__(self, test_inputs=None):
        """ Default constructor """

        it = iter(test_inputs.split("\n")) if test_inputs else None

        def uinput():
            return next(it) if it else sys.stdin.readline().rstrip()

        # Reading single elements
        [self.n, self.d] = map(int, uinput().split())

        # Reading multiple number of lines of the same number of elements each
        l, s = self.n, 2
        inp = (" ".join(uinput() for i in range(l))).split()
        self.numm = [[int(inp[i]) for i in range(j, l*s, s)] for j in range(s)]
        self.numa, self.numb = self.numm

    def calculate(self):
        """ Main calcualtion function of the class """

        result = 0

        # Sorting both arrays by using first array as a key
        self.numa, self.numb = zip(*sorted(zip(self.numa, self.numb)))

        # Calculating partial sums
        self.psum = [0]
        for i in range(self.n):
            self.psum.append(self.psum[-1] + self.numb[i])

        # Calculating result
        for i in range(self.n):
            mrb = self.numa[i] + self.d
            sum = self.psum[lbound(self.numa, mrb)] - self.psum[i]
            result = max(result, sum)

        return str(result)


# Find lower bound - leftmost position for new element to be inserted
def lbound(v, n):
    b = 0
    e = len(v)
    while b != e:
        mid = (b + e) // 2
        if v[mid] < n:
            b = mid + 1
        else:
            e = mid
    return b

###############################################################################
# Unit Tests
###############################################################################


class unitTests(unittest.TestCase):

    def test_single_test(self):
        """ Company class testing """

        # Constructor test
        test = "4 5\n75 5\n0 100\n150 20\n75 1"
        d = Company(test)
        self.assertEqual(d.n, 4)
        self.assertEqual(d.d, 5)
        self.assertEqual(d.numa, [75, 0, 150, 75])
        self.assertEqual(d.numb, [5, 100, 20, 1])

        # Sample test
        self.assertEqual(Company(test).calculate(), "100")

        # Sample test
        test = "5 100\n0 7\n11 32\n99 10\n46 8\n87 54"
        self.assertEqual(Company(test).calculate(), "111")

        # Sample test
        test = ""
        # self.assertEqual(Company(test).calculate(), "0")

        # My tests
        test = ""
        # self.assertEqual(Company(test).calculate(), "0")

        # Time limit test
        self.time_limit_test(1000)

    def time_limit_test(self, nmax):
        """ Timelimit testing """
        import random
        import timeit

        # Random inputs
        test = str(nmax) + " " + str(nmax) + "\n"
        numnums = [str(i) + " " + str(i+1) for i in range(nmax)]
        test += "\n".join(numnums) + "\n"

        # Run the test
        start = timeit.default_timer()
        d = Company(test)
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
    sys.stdout.write(Company().calculate())
