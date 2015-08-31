#!/usr/bin/env python
# 560A_currency.py - Codeforces.com 560A Currency program by Sergey 2015

# Standard modules
import unittest
import sys

# Additional modules


###############################################################################
# Currency Class
###############################################################################


class Currency:
    """ Currency representation """

    def __init__(self, args):
        """ Default constructor """

        self.imax, self.nums = args

    def calculate(self):
        """ Main calcualtion function of the class """

        result = 1
        for n in self.nums:
            if n == 1:
                result = -1
                break

        return str(result)


###############################################################################
# Helping classes
###############################################################################


###############################################################################
# Currency Class testing wrapper code
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
    imax = int(uinput())
    nums = list(map(int, uinput().split()))

    # Decoding inputs into a list
    return [imax, nums]


def calculate(test_inputs=None):
    """ Base class calculate method wrapper """
    return Currency(get_inputs(test_inputs)).calculate()


###############################################################################
# Unit Tests
###############################################################################


class unitTests(unittest.TestCase):

    def test_Currency_class__basic_functions(self):
        """ Currency class basic functions testing """

        # Constructor test
        d = Currency([5, [1, 2, 3, 4, 5]])
        self.assertEqual(d.imax, 5)

    def test_sample_tests(self):
        """ Quiz sample tests. Add \n to separate lines """

        # Sample test 1
        test = "5\n1 2 3 4 5"
        self.assertEqual(calculate(test), "-1")
        self.assertEqual(get_inputs(test)[0], 5)
        self.assertEqual(list(get_inputs(test)[1]), [1, 2, 3, 4, 5])

        # Sample test 2
        test = "3\n5 6 2"
        self.assertEqual(calculate(test), "1")

        # Sample test 3
        test = "1\n12"
        # self.assertEqual(calculate(test), "0")

        # My test 4
        test = "1\n12"
        # self.assertEqual(calculate(test), "0")

    def test_time_limit_test(self):
        """ Quiz time limit test """

        import random

        # Time limit test
        imax = 1000
        num = str(imax)
        test = num + "\n"
        numnums = [str(i) + " " + str(i+1) for i in range(imax)]
        test += "\n".join(numnums) + "\n"
        nums = [random.randint(1, 10000) for i in range(imax)]
        test += " ".join(map(str, nums)) + "\n"

        import timeit

        start = timeit.default_timer()
        args = get_inputs(test)

        init = timeit.default_timer()
        d = Currency(args)

        calc = timeit.default_timer()
        d.calculate()

        stop = timeit.default_timer()
        print(
            "\nTime Test: " +
            "{0:.3f}s (inp {1:.3f}s init {2:.3f}s calc {3:.3f}s)".
            format(stop-start, init-start, calc-init, stop-calc))

if __name__ == "__main__":

    # Avoiding recursion limitaions
    sys.setrecursionlimit(100000)

    if sys.argv[-1] == "-ut":
        unittest.main(argv=[" "])

    # Print the result string
    sys.stdout.write(calculate())
