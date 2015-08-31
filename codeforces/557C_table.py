#!/usr/bin/env python
# 557C_table.py - Codeforces.com 557C Table quiz by Sergey 2015

# Standard modules
import unittest
import sys
import re
import random
import bisect

# Additional modules


###############################################################################
# Table Class
###############################################################################


class Table:
    """ Table representation """

    LIM = 201

    def __init__(self, args):
        """ Default constructor """

        self.legs = args[0]
        self.energy = args[1]
        self.n = len(self.legs)

        # Sort lists
        self.srt = sorted((l, e) for l, e in zip(self.legs, self.energy))
        self.legs = []
        self.energy = []
        for n in self.srt:
            self.legs.append(n[0])
            self.energy.append(n[1])

        # Prepare accumulator variables

    def get_new_layer_info(self, legs, energy):

        ll = len(legs)
        for (i, l) in enumerate(legs):

            self.ilen = l
            e = energy[i]

            if i == 0:
                self.itop_eng = sum(energy)
                self.ieltot = [0 for i in range(self.LIM)]
                self.ielprev = [0 for i in range(self.LIM)]
                self.ielprev_eng = 0
                self.ires_eng = sys.maxsize

            if i == 0 or self.ilen != prev:
                self.irep = 0
                self.ielsum_eng = 0
                self.ielprev = list(self.ieltot)

            self.irep += 1
            self.itop_eng -= e
            self.ielprev_eng += e
            self.ielsum_eng += e
            self.ieltot[e] += 1

            if i == ll - 1 or legs[i+1] != self.ilen:
                self.irem = self.irep - 1
                self.irem_eng = self.ielprev_eng - self.ielsum_eng
                if self.irem != 0:
                    sumh = self.energyl_sum_high(self.ielprev, self.irem)
                    self.irem_eng -= sumh
                summ = self.itop_eng + self.irem_eng
                self.ires_eng = min(self.ires_eng, summ)
                yield
            prev = self.ilen

    def energyl_sum_high(self, l, n):
        result = 0
        for i in range(len(l) - 1, -1, -1):
            e = l[i]
            if e == 0:
                continue
            if n <= 0:
                break
            result += i * (n if e > n else e)
            n -= e
        return result

    def calculate(self):
        """ Main calcualtion function of the class """

        iter = self.get_new_layer_info(self.legs, self.energy)

        for g in iter:
            pass

        result = self.ires_eng

        return str(result)


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
            return input()

    # Getting string inputs. Place all uinput() calls here
    num = int(uinput())
    str1 = [int(s) for s in uinput().split()]
    str2 = [int(s) for s in uinput().split()]

    # Decoding inputs into a list
    inputs = []
    inputs.append(str1)
    inputs.append(str2)

    return inputs


def calculate(test_inputs=None):
    """ Base class calculate method wrapper """
    return Table(get_inputs(test_inputs)).calculate()


###############################################################################
# Unit Tests
###############################################################################


class unitTests(unittest.TestCase):

    def test_sample_tests(self):
        """ Quiz sample tests. Add \n to separate lines """

        # my tests
        imax = 10000
        test = "0\n"
        for i in range(imax):
            test += str(i) + " "
        test += "\n"
        for i in range(imax):
            test += str(random.randint(1, 200)) + " "
        calculate(test)

        # Sample test 1
        test = "2\n1 5\n3 2"
        self.assertEqual(calculate(test), "2")
        self.assertEqual(get_inputs(test), [[1, 5], [3, 2]])

        # Other tests
        test = "3\n2 4 4\n1 1 1"
        self.assertEqual(calculate(test), "0")
        test = "6\n2 2 1 1 3 3\n4 3 5 5 2 1"
        self.assertEqual(calculate(test), "8")

        test = (
            "10\n20 1 15 17 11 2 15 3 16 3\n" +
            "129 114 183 94 169 16 18 104 49 146")
        self.assertEqual(calculate(test), "652")

    def test_Table_class__basic_functions(self):
        """ Table class basic functions testing """

        # Constructor test
        d = Table([[2, 2, 1, 1, 3, 3], [2, 2, 3, 3, 1, 1]])
        self.assertEqual(d.legs[0], 1)
        self.assertEqual(d.energy[0], 3)

        # Get layer info (length, number of legs, energy list, energy sum)
        iter = d.get_new_layer_info([1, 1, 2, 2, 4, 5], [2, 2, 3, 3, 1, 1])
        next(iter)
        self.assertEqual(d.itop_eng, 8)
        self.assertEqual(d.ilen, 1)
        self.assertEqual(d.irep, 2)
        self.assertEqual(d.irem, 1)
        self.assertEqual(d.irem_eng, 0)
        self.assertEqual(d.ires_eng, 8)

        next(iter)
        self.assertEqual(d.ilen, 2)
        self.assertEqual(d.irep, 2)
        self.assertEqual(d.irem, 1)
        self.assertEqual(d.irem_eng, 2)
        self.assertEqual(d.ires_eng, 4)

        # Get layer info (length, number of legs, energy list, energy sum)
        d = Table([[], []])
        iter = d.get_new_layer_info([1, 1, 2, 2, 3, 3], [5, 5, 4, 3, 2, 1])
        next(iter)
        self.assertEqual(d.ilen, 1)
        self.assertEqual(d.irep, 2)
        self.assertEqual(d.irem, 1)
        self.assertEqual(d.irem_eng, 0)
        self.assertEqual(d.ires_eng, 10)
        next(iter)
        self.assertEqual(d.ilen, 2)
        self.assertEqual(d.irep, 2)
        self.assertEqual(d.irem, 1)
        self.assertEqual(d.irem_eng, 5)
        self.assertEqual(d.ires_eng, 8)
        next(iter)
        self.assertEqual(d.ilen, 3)
        self.assertEqual(d.irep, 2)
        self.assertEqual(d.irem, 1)
        self.assertEqual(d.irem_eng, 12)
        self.assertEqual(d.ires_eng, 8)

if __name__ == "__main__":

    # Avoiding recursion limitaions
    sys.setrecursionlimit(100000)

    if sys.argv[-1] == "-ut":
        unittest.main(argv=[" "])

    # Print the result string
    print(calculate())
