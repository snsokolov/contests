#!/usr/bin/env python
# 558C_chem.py - Codeforces.com 558C Chem quiz by Sergey 2015

# Standard modules
import unittest
import sys

# Additional modules
import itertools
###############################################################################
# Chem Class
###############################################################################


class Chem:
    """ Chem representation """
    MAX = 100001

    def __init__(self, args):
        """ Default constructor """

        self.n = args[0]
        self.list = args[1]

    def calculate(self):
        """ Main calcualtion function of the class """

        valid = set()
        stp = [0] * self.MAX
        first = 1
        for vol in self.list:
            new_valid = set()
            steps = 0
            prev = 1
            while vol > 0:
                if (first or vol in valid):
                    if prev % 2 == 1:
                        ssteps = steps + 1
                        svol = vol << 1
                        while svol <= self.MAX:
                            new_valid.add(svol)
                            stp[svol] += ssteps
                            svol <<= 1
                            ssteps += 1
                    new_valid.add(vol)
                    stp[vol] += steps
                prev = vol
                vol >>= 1
                steps += 1
            if not first:
                valid.intersection_update(new_valid)
            else:
                valid.update(new_valid)
            first = 0

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
    nums = list(map(int, uinput().split(), itertools.repeat(10, num)))

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
        imax = 10000
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
        self.assertEqual(d.list[0], 4)


if __name__ == "__main__":

    # Avoiding recursion limitaions
    sys.setrecursionlimit(100000)

    if sys.argv[-1] == "-ut":
        import random
        unittest.main(argv=[" "])

    # Print the result string
    sys.stdout.write(calculate())
