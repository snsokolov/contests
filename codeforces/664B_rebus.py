#!/usr/bin/env python3
# 664B_rebus.py - Codeforces.com/problemset/problem/664/B by Sergey 2016

import unittest
import sys
import re

###############################################################################
# Rebus Class (Main Program)
###############################################################################


class Rebus:
    """ Rebus representation """

    def __init__(self, test_inputs=None):
        """ Default constructor """

        it = iter(test_inputs.split("\n")) if test_inputs else None

        def uinput():
            return next(it) if it else sys.stdin.readline().rstrip()

        # Reading single elements
        self.str = uinput()
        
        # End value
        self.n = 0
        m = re.search("(\d+)", self.str)
        if m:
            self.n = int(m.group(1))

        # Signs
        self.signs = ["+"] + re.findall("\? ([+-])", self.str)
    
    def summ(self, nums, signs):
        result = 0
        for i in range(len(self.signs)):
            if self.signs[i] == "+":
                result += nums[i]
            else:
                result -= nums[i]
        return result

    def calculate(self):
        """ Main calcualtion function of the class """
        
        nums = [0] * len(self.signs)
        for i in range(len(self.signs)):
            nums[i] = 1

        sum = self.summ(nums, self.signs)

        for i in range(len(self.signs)):
            if sum != self.n:
                if self.signs[i] == "+" and sum < self.n:
                    nums[i] = min(self.n - sum + 1, self.n)
                    sum -= 1
                    sum += nums[i]
                if self.signs[i] == "-" and sum > self.n:
                    nums[i] = min(sum + 1 - self.n, self.n)
                    sum += 1
                    sum -= nums[i]

        if sum == self.n:
            result = "Possible\n"

            for i in range(len(self.signs)):
                if i != 0:
                    result += self.signs[i] + " "
                result += str(nums[i]) + " "
            result += "= " + str(self.n)
        else:
            result = "Impossible"

        return str(result)

###############################################################################
# Unit Tests
###############################################################################


class unitTests(unittest.TestCase):

    def test_single_test(self):
        """ Rebus class testing """

        # Constructor test
        test = "? + ? - ? + ? + ? = 42"
        d = Rebus(test)
        self.assertEqual(d.str, "? + ? - ? + ? + ? = 42")
        self.assertEqual(d.n, 42)
        self.assertEqual(d.signs, ["+", "+", "-", "+", "+"])

        # Sample test
        self.assertEqual(Rebus(test).calculate(), "Possible\n40 + 1 - 1 + 1 + 1 = 42")

        # Sample test
        test = "? - ? = 1"
        self.assertEqual(Rebus(test).calculate(), "Impossible")

        # Sample test
        test = "? = 1000000"
        self.assertEqual(Rebus(test).calculate(), "Possible\n1000000 = 1000000")

        test = "? + ? + ? + ? - ? = 2"
        self.assertEqual(Rebus(test).calculate(), "Possible\n1 + 1 + 1 + 1 - 2 = 2")

        # My tests
        test = ""
        # self.assertEqual(Rebus(test).calculate(), "0")

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
        d = Rebus(test)
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
    sys.stdout.write(Rebus().calculate())
