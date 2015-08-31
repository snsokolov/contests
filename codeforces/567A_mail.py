#!/usr/bin/env python
# 567A_mail.py - Codeforces.com 567A Mail program by Sergey 2015

import unittest
import sys

###############################################################################
# Mail Class
###############################################################################


class Mail:
    """ Mail representation """

    def __init__(self, test_inputs=None):
        """ Default constructor """

        it = iter(test_inputs.split("\n")) if test_inputs else None

        def uinput():
            return next(it) if it else sys.stdin.readline().rstrip()

        # Reading single elements
        self.imax = int(uinput())

        # Reading a single line of multiple elements
        self.nums = list(map(int, uinput().split()))

    def calculate(self):
        """ Main calcualtion function of the class """

        result = []

        for i in range(self.imax):
            dmin = min(
                abs(self.nums[i] - self.nums[(i-1) % self.imax]),
                abs(self.nums[i] - self.nums[(i+1) % self.imax]))
            dmax = max(
                abs(self.nums[i] - self.nums[0]),
                abs(self.nums[i] - self.nums[-1]))
            result.append((dmin, dmax))

        return str("\n".join(" ".join(map(str, n)) for n in result))

###############################################################################
# Unit Tests
###############################################################################


class unitTests(unittest.TestCase):

    def test_single_test(self):
        """ Mail class testing """

        # Constructor test
        test = "4\n-5 -2 2 7"
        d = Mail(test)
        self.assertEqual(d.imax, 4)
        self.assertEqual(d.nums, [-5, -2, 2, 7])

        # Sample test
        self.assertEqual(Mail(test).calculate(), "3 12\n3 9\n4 7\n5 12")

        # Sample test
        test = "2\n-1 1"
        self.assertEqual(Mail(test).calculate(), "2 2\n2 2")

        # Time limit test
        # self.time_limit_test(5000)

    def time_limit_test(self, imax):
        """ Timelimit testing """
        import random
        import timeit

        # Random inputs
        test = str(imax) + "\n"
        numnums = [str(i) + " " + str(i+1) for i in range(imax)]
        test += "\n".join(numnums) + "\n"
        nums = [random.randint(1, 10000) for i in range(imax)]
        test += " ".join(map(str, nums)) + "\n"

        # Run the test
        start = timeit.default_timer()
        d = Mail(test)
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
    sys.stdout.write(Mail().calculate())
