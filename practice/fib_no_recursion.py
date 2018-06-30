#!/usr/bin/env python3
# fib_no_recursion.py - Fib_no_recursion program by Sergey 2018
#
# Calculating n-th number in fibonaccy sequence without using recursion.
#   F0 = 0
#   F1 = 1
#   Fn = Fn-1 + Fn-2

import unittest
import timeit

###############################################################################
# Fib_no_recursion (Main Program)
###############################################################################


def fib_brute_force(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_brute_force(n-1) + fib_brute_force(n-2)


def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        result = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    memo[n] = result
    return result


def fib_loop(n):
    if n == 0:
        return 0
    fnm1 = 0
    fn = 1
    for i in range(n-1):
        fn, fnm1 = fn + fnm1, fn
    return fn


def fib_fast(n):

    def n_plus1(n, fnm1, fn):
        return n+1, fn, fnm1+fn if n > 0 else 1

    def n_mul2(n, fnm1, fn):
        f2n = fn * (fn + 2 * fnm1)
        f2nm1 = fn*fn + fnm1*fnm1
        return n*2, f2nm1, f2n

    if n == 0:
        return 0

    result = 1, 0, 1
    n_binary = list(map(int, bin(n)[2:]))[1:]
    for n_bit in n_binary:
        result = n_mul2(*result)
        if n_bit:
            result = n_plus1(*result)
    return result[2]  # f(n)


###############################################################################
# Unit Tests
###############################################################################


class unitTests(unittest.TestCase):

    def test_Fib_brute_force(self):
        """ Fib_brute_force function testing """
        self.assertEqual(fib_brute_force(25), 75025)

    def test_Fib_memo(self):
        """ Fib_memo function testing """
        self.assertEqual(fib_memo(0), 0)
        self.assertEqual(fib_memo(1), 1)
        self.assertEqual(fib_memo(25), 75025)

    def test_Fib_loop(self):
        """ Fib_loop function testing """
        self.assertEqual(fib_loop(0), 0)
        self.assertEqual(fib_loop(1), 1)
        self.assertEqual(fib_loop(25), 75025)

    def test_Fib_fast(self):
        """ Fib_loop function testing """
        self.assertEqual(fib_fast(0), 0)
        self.assertEqual(fib_fast(1), 1)
        self.assertEqual(fib_fast(25), 75025)

    def test_performance(self):
        print('Performance tests:')

        number = 18
        func = 'fib_brute_force'
        cmd = '%s(%d)' % (func, number)
        print(cmd, timeit.timeit(cmd,
              setup="from __main__ import %s" % func, number=1))

        number = 900
        func = 'fib_memo'
        cmd = '%s(%d)' % (func, number)
        print(cmd, timeit.timeit(cmd,
              setup="from __main__ import %s" % func, number=1))

        number = 8000
        func = 'fib_loop'
        cmd = '%s(%d)' % (func, number)
        print(cmd, timeit.timeit(cmd,
              setup="from __main__ import %s" % func, number=1))

        number = 80000
        func = 'fib_fast'
        cmd = '%s(%d)' % (func, number)
        print(cmd, timeit.timeit(cmd,
              setup="from __main__ import %s" % func, number=1))

if __name__ == "__main__":
    unittest.main(argv=[" "])
