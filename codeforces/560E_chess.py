#!/usr/bin/env python
# 560E_chess.py - Codeforces.com/problemset/problem/560/E Chess program by Sergey 2015

# Standard modules
import unittest
import sys

# Additional modules


###############################################################################
# Chess Class
###############################################################################


class Chess:
    """ Chess representation """

    def __init__(self, args, N=200001, MOD=10**9+7):
        """ Default constructor """

        self.h, self.w, self.imax, self.numa, self.numb = args
        self.MOD = MOD
        self.N = min(N, self.h + self.w)

        # Sort black cells
        self.pt = sorted(zip(self.numa, self.numb))
        self.pt.append((self.h, self.w))

        # Populate factorial
        self.fact = [1]
        prev = 1
        for i in range(1, self.N):
            f = (prev * i) % self.MOD
            self.fact.append(f)
            prev = f

        # Populate Inv factorial
        self.inv = [0] * self.N
        self.inv[self.N-1] = self.modInvfact(self.N-1)
        for i in range(self.N-2, -1, -1):
            self.inv[i] = (self.inv[i+1] * (i+1)) % self.MOD

        # Populate number of ways
        self.ways = []
        for i in range(len(self.pt)):
            (h, w) = self.pt[i]
            self.ways.append(self.modC(h + w - 2, h - 1))
            for j in range(i):
                (hj, wj) = self.pt[j]
                if (hj <= h and wj <= w):
                    mult = self.modC(h - hj + w - wj, h - hj)
                    self.ways[i] = self.modSub(
                        self.ways[i], self.ways[j] * mult, self.MOD)

    def modC(self, n, k):
        return (
            self.fact[n] *
            ((self.inv[k] * self.inv[n-k]) % self.MOD)) % self.MOD

    def modInvfact(self, n):
        return self.modExp(self.fact[n], self.MOD-2, self.MOD)

    def modExp(self, n, e, p):
        res = 1
        while e > 0:
            if (e % 2 == 1):
                res = (res * n) % p
            e >>= 1
            n = (n * n) % p
        return res

    def modSub(self, a, b, p):
        return ((a - b) % p + p) % p

    def calculate(self):
        """ Main calcualtion function of the class """

        result = self.ways[-1]

        return str(result)


###############################################################################
# Helping classes
###############################################################################


###############################################################################
# Chess Class testing wrapper code
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
    h, w, imax = list(map(int, uinput().split()))
    numnums = list(map(int, " ".join(uinput() for i in range(imax)).split()))

    # Splitting numnums into n arrays
    numa = []
    numb = []
    for i in range(0, 2*imax, 2):
        numa.append(numnums[i])
        numb.append(numnums[i+1])

    # Decoding inputs into a list
    return [h, w, imax, numa, numb]


def calculate(test_inputs=None):
    """ Base class calculate method wrapper """
    return Chess(get_inputs(test_inputs)).calculate()


###############################################################################
# Unit Tests
###############################################################################


class unitTests(unittest.TestCase):

    def test_Chess_class__basic_functions(self):
        """ Chess class basic functions testing """

        # Constructor test
        d = Chess([3, 4, 2, [2, 2], [2, 3]])
        self.assertEqual(d.imax, 2)
        self.assertEqual(d.pt[0], (2, 2))

        # modExp
        self.assertEqual(d.modExp(3, 3, 6), 3)

        # Factorials
        self.assertEqual(d.fact[3], 6)
        self.assertEqual(d.inv[3], d.modInvfact(3))

        # Binominal
        self.assertEqual(d.modC(4, 2), 6)

        # Ways
        self.assertEqual(d.ways[0], 2)

    def test_sample_tests(self):
        """ Quiz sample tests. Add \n to separate lines """

        # Sample test 1
        test = "3 4 2\n2 2\n2 3"
        self.assertEqual(calculate(test), "2")
        self.assertEqual(get_inputs(test)[0], 3)
        self.assertEqual(list(get_inputs(test)[3]), [2, 2])
        self.assertEqual(list(get_inputs(test)[4]), [2, 3])

        # Sample test 2
        test = "100 100 3\n15 16\n16 15\n99 88"
        self.assertEqual(calculate(test), "545732279")

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
        imax = 20
        h = 100000
        w = 99000
        num = str(imax)
        test = str(h) + " " + str(w) + " " + num + "\n"
        numnums = [str(i) + " " + str(i+1) for i in range(imax)]
        test += "\n".join(numnums) + "\n"

        import timeit

        start = timeit.default_timer()
        args = get_inputs(test)

        init = timeit.default_timer()
        d = Chess(args)

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
