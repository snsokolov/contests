#!/usr/bin/env python3
# 672C_bottles.py - Codeforces.com/problemset/problem/672/C by Sergey 2016

import unittest
import sys
import math

###############################################################################
# Bottles Class (Main Program)
###############################################################################


class Bottles:
    """ Bottles representation """

    def __init__(self, test_inputs=None):
        """ Default constructor """

        it = iter(test_inputs.split("\n")) if test_inputs else None

        def uinput():
            return next(it) if it else sys.stdin.readline().rstrip()

        # Reading single elements
        [self.ax, self.ay, self.bx, self.by, self.tx, self.ty] = map(
            int, uinput().split())

        self.n = int(uinput())

        # Reading multiple number of lines of the same number of elements each
        l, s = self.n, 2
        inp = (" ".join(uinput() for i in range(l))).split()
        self.numm = [[int(inp[i]) for i in range(j, l*s, s)] for j in range(s)]
        self.numa, self.numb = self.numm

    def minn(self, l, skipi=set([])):
        result = None
        mini = None
        for i in range(len(l)):
            if i in skipi:
                continue
            if result is None or l[i] < result:
                mini = i
                result = l[i]
        return (result, mini)

    def calculate(self):
        """ Main calcualtion function of the class """

        distt = []
        dista = []
        distb = []
        for i in range(self.n):
            distt.append(math.sqrt(
                (self.numa[i] - self.tx)**2 + (self.numb[i] - self.ty)**2))
            dista.append(math.sqrt(
                (self.numa[i] - self.ax)**2 + (self.numb[i] - self.ay)**2))
            distb.append(math.sqrt(
                (self.numa[i] - self.bx)**2 + (self.numb[i] - self.by)**2))

        result = sum(distt)*2

        distat = math.sqrt(
            (self.tx - self.ax)**2 + (self.ty - self.ay)**2)
        distbt = math.sqrt(
            (self.tx - self.bx)**2 + (self.ty - self.by)**2)

        # Find first min
        mina, minai = self.minn(dista)
        minb, minbi = self.minn(distb)

        firstminisa = 1 if mina < minb else 0
        firstmin = mina if mina < minb else minb
        firstmini = minai if mina < minb else minbi

        result = result - distt[firstmini] + firstmin

        # Find the second min
        if firstminisa:
            ddd = []
            for i in range(self.n):
                ddd.append(distb[i] - distt[i])
            minb, minbi = self.minn(ddd, skipi=set([firstmini]))
            if minb < 0:
                result = result - distt[minbi] + distb[minbi]
        else:
            ddd = []
            for i in range(self.n):
                ddd.append(dista[i] - distt[i])
            mina, minai = self.minn(ddd, skipi=set([firstmini]))
            if mina < 0:
                result = result - distt[minai] + dista[minai]

        return str(result)

###############################################################################
# Unit Tests
###############################################################################


class unitTests(unittest.TestCase):

    def test_single_test(self):
        """ Bottles class testing """

        # Constructor test
        test = "3 1 1 2 0 0\n3\n1 1\n2 1\n2 3"
        d = Bottles(test)
        self.assertEqual(d.n, 3)
        self.assertEqual(d.numa, [1, 2, 2])
        self.assertEqual(d.numb, [1, 1, 3])

        # Sample test
        self.assertEqual(Bottles(test).calculate(), "11.084259940083")

        # Sample test
        test = "5 0 4 2 2 0\n5\n5 2\n3 0\n5 5\n3 5\n3 3"
        # self.assertEqual(Bottles(test).calculate(), "33.121375178000")

        # Sample test
        test = ""
        # self.assertEqual(Bottles(test).calculate(), "0")

        # My tests
        test = ""
        # self.assertEqual(Bottles(test).calculate(), "0")

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
        d = Bottles(test)
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
    sys.stdout.write(Bottles().calculate())
