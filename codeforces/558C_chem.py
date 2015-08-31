#!/usr/bin/env python
# 558C_chem.py - Codeforces.com 558C Chem quiz by Sergey 2015

# Standard modules
import unittest
import sys
import re
import random
import bisect
import array

# Additional modules


###############################################################################
# Chem Class
###############################################################################


class Chem:
    """ Chem representation """

    def __init__(self, args):
        """ Default constructor """

        self.n = args[0]
        self.list = sorted(args[1])
        self.max = self.list[-1]

    def decant(self, valid, stp, vol, max):
        new_valid = set()
        first = 1 if not valid else 0
        steps = 0
        prev = None
        while vol > 0:
            if (first or vol in valid) and (prev is None or prev % 2 == 1):
                ssteps = steps + 1
                svol = vol * 2
                while svol <= max:
                    if first:
                        valid.add(svol)
                        stp[svol] = ssteps
                    elif svol in valid:
                        new_valid.add(svol)
                        stp[svol] += ssteps
                    else:
                        break
                    svol *= 2
                    ssteps += 1
            if first:
                valid.add(vol)
                stp[vol] = steps
            elif vol in valid:
                new_valid.add(vol)
                stp[vol] += steps
            prev = vol
            vol >>= 1
            steps += 1
        if not first:
            valid.intersection_update(new_valid)

    def calculate(self):
        """ Main calcualtion function of the class """

        valid = set()
        stp = dict()
        for n in self.list:
            self.decant(valid, stp, n, self.max)

        result = None
        for n in valid:
            if result is None or result > stp[n]:
                result = stp[n]

        return str(result)


###############################################################################
# Helping classes
###############################################################################


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
    num = int(uinput())
    nums = map(int, uinput().split())

    # Decoding inputs into a list
    return [num, nums]


def calculate(test_inputs=None):
    """ Base class calculate method wrapper """
    return Chem(get_inputs(test_inputs)).calculate()


###############################################################################
# Unit Tests
###############################################################################


class unitTests(unittest.TestCase):

    def test_sample_tests(self):
        """ Quiz sample tests. Add \n to separate lines """

        # Sample test 1
        test = "3\n4 8 2"
        self.assertEqual(calculate(test), "2")
        self.assertEqual(get_inputs(test)[0], 3)
        self.assertEqual(list(get_inputs(test)[1]), [4, 8, 2])

        # Sample test 2
        test = "3\n3 5 6"
        self.assertEqual(calculate(test), "5")

        # Sample test 3
        test = "3\n10 4 4"
        self.assertEqual(calculate(test), "3")

    def test_timelimit_tests(self):

        # Time limit test
        imax = 1000
        test = str(imax)
        nums = [random.randint(1, 100000) for i in range(imax)]
        test += "\n" + " ".join(map(str, nums))

        import timeit

        start = timeit.default_timer()
        args = get_inputs(test)

        init = timeit.default_timer()
        d = Chem(args)

        calc = timeit.default_timer()
        d.calculate()

        stop = timeit.default_timer()
        print("\nTime Test: {0:.3f} (inp {1:.3f} init {2:.3f} calc {3:.3f})".
              format(stop-start, init-start, calc-init, stop-calc))

    def test_Chem_class__basic_functions(self):
        """ Chem class basic functions testing """

        # Constructor test
        d = Chem([3, [4, 8, 2]])
        self.assertEqual(d.list[0], 2)

        valid = set()
        stp = [0]*11
        d.decant(valid, stp, 5, 10)
        self.assertEqual(valid, {1, 2, 4, 5, 8, 10})
        self.assertEqual(stp, [0, 2, 1, 0, 2, 0, 0, 0, 3, 0, 1])

        valid = set()
        stp = [0]*11
        d.decant(valid, stp, 3, 10)
        self.assertEqual(valid, {8, 1, 2, 4, 3, 6})
        self.assertEqual(stp, [0, 1, 2, 0, 3, 0, 1, 0, 4, 0, 0])
        d.decant(valid, stp, 5, 10)
        self.assertEqual(valid, {8, 1, 2, 4})

if __name__ == "__main__":

    # Avoiding recursion limitaions
    sys.setrecursionlimit(100000)

    if sys.argv[-1] == "-ut":
        unittest.main(argv=[" "])

    # Print the result string
    sys.stdout.write(calculate())
