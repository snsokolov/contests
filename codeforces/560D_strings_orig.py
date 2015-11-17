#!/usr/bin/env python3
# 560D_strings.py - Codeforces.com/problemset/problem/560/D Strings program by Sergey 2015

# Standard modules
import unittest
import sys

# Additional modules


###############################################################################
# Strings Class
###############################################################################


class Strings:
    """ Strings representation """

    def __init__(self, args):
        """ Default constructor """

        self.stra, self.strb = args

    def splitcheck(self, a, b):
        la = len(a)
        lb = len(b)
        if la != lb:
            return 0
        if a == b:
            return 1
        if la % 2 == 1 or lb % 2 == 1:
            return 0

        a1, a2 = a[la//2:], a[:la//2]
        b1, b2 = b[lb//2:], b[:lb//2]
        if self.splitcheck(a1, b1) and self.splitcheck(a2, b2):
            return 1
        if self.splitcheck(a1, b2) and self.splitcheck(a2, b1):
            return 1
        return 0

    def calculate(self):
        """ Main calcualtion function of the class """

        result = self.splitcheck(self.stra, self.strb)

        return str("YES" if result else "NO")


###############################################################################
# Helping classes
###############################################################################


###############################################################################
# Strings Class testing wrapper code
###############################################################################


def get_inputs(test_inputs=None):

    it = iter(test_inputs.split("\n")) if test_inputs else None

    def uinput():
        """ Unit-testable input function wrapper """
        if it:
            return next(it)
        else:
            return sys.stdin.readline().rstrip()

    # Getting string inputs. Place all uinput() calls here
    stra = uinput()
    strb = uinput()
    # Decoding inputs into a list
    return [stra, strb]


def calculate(test_inputs=None):
    """ Base class calculate method wrapper """
    return Strings(get_inputs(test_inputs)).calculate()


###############################################################################
# Unit Tests
###############################################################################


class unitTests(unittest.TestCase):

    def test_Strings_class__basic_functions(self):
        """ Strings class basic functions testing """

        # Constructor test
        d = Strings(["aaaabbbb", "ababbaba"])
        self.assertEqual(d.stra, "aaaabbbb")

        self.assertEqual(d.splitcheck("a", "a"), 1)
        self.assertEqual(d.splitcheck("ab", "a"), 0)
        self.assertEqual(d.splitcheck("abb", "aba"), 0)
        self.assertEqual(d.splitcheck("ab", "ba"), 1)
        self.assertEqual(d.splitcheck("abcdefgh", "efhgdcba"), 1)

    def test_sample_tests(self):
        """ Quiz sample tests. Add \n to separate lines """

        # Sample test 1
        test = "aaba\nabaa"
        self.assertEqual(calculate(test), "YES")
        self.assertEqual(get_inputs(test)[0], "aaba")
        self.assertEqual(get_inputs(test)[1], "abaa")

        # Sample test 2
        test = "aabb\nabab"
        self.assertEqual(calculate(test), "NO")

        # Sample test 3
        test = "abddbbdd\nddbbddba"
        self.assertEqual(calculate(test), "YES")

        # My test
        test = "aabb\nbbaa"
        self.assertEqual(calculate(test), "YES")

    def test_time_limit_test(self):
        """ Quiz time limit test """

        import random

        # Time limit test
        imax = 100000
        numnums = ["ab" for i in range(imax)]
        test = "".join(numnums) + "\n"
        numnums = ["aa" for i in range(imax)]
        test += "".join(numnums) + "\n"

        import timeit

        start = timeit.default_timer()
        args = get_inputs(test)

        init = timeit.default_timer()
        d = Strings(args)

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
