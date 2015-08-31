#!/usr/bin/env python
# 556D_fug.py - Codeforces.com 556D Fug quiz by Sergey 2015

# Standard modules
import unittest
import sys
import re

# Additional modules
import bisect

###############################################################################
# Fastlist Class
###############################################################################


class Fastlist(object):
    """ Fastlist representation """

    def __init__(self, l=[], load=5000, sorted=0):
        self._load = load
        self._sorted = sorted
        self._lists = []
        self._starts = []
        self._mins = []
        self._insert_list()
        self._irev = 0
        self._ii = 0
        self._il = 0
        self.extend(l)

    def _index_location(self, index):
        if len(self._lists[0]) == 0:
            raise IndexError("List index out of range")
        if index == 0:
            return (0, 0)
        if index == -1:
            return (len(self._lists) - 1, len(self._lists[-1]) - 1)
        if self._sorted:
            raise RuntimeError("No index access to the sorted list, exc 0, -1")
        length = len(self)
        if index < 0:
            index = length + index
        if index >= length:
            raise IndexError("List index out of range")
        il = bisect.bisect_right(self._starts, index) - 1
        return (il, index - self._starts[il])

    def _insert_list(self, il=None):
        if il is None:
            il = len(self._lists)
        self._lists.insert(il, [])
        if self._sorted:
            if il == 0:
                self._mins.insert(il, None)
            else:
                self._mins.insert(il, self._lists[il-1][-1])
        else:
            if il == 0:
                self._starts.insert(il, 0)
            else:
                start = self._starts[il-1] + len(self._lists[il-1])
                self._starts.insert(il, start)

    def _del_list(self, il):
        del self._lists[il]
        if self._sorted:
            del self._mins[il]
        else:
            del self._starts[il]

    def _rebalance(self, il):
        illen = len(self._lists[il])
        if illen >= self._load * 2:
            self._insert_list(il)
            self._even_lists(il)
        if illen <= self._load * 0.2:
            if il != 0:
                self._even_lists(il-1)
            elif len(self._lists) > 1:
                self._even_lists(il)

    def _even_lists(self, il):
        tot = len(self._lists[il]) + len(self._lists[il+1])
        if tot < self._load * 1:
            self._lists[il] += self._lists[il+1]
            self._del_list(il+1)
            if self._sorted:
                self._mins[il] = self._lists[il][0]
        else:
            half = tot//2
            ltot = self._lists[il] + self._lists[il+1]
            self._lists[il] = ltot[:half]
            self._lists[il+1] = ltot[half:]
            if self._sorted:
                self._mins[il] = self._lists[il][0]
                self._mins[il+1] = self._lists[il+1][0]
            else:
                self._starts[il+1] = self._starts[il] + len(self._lists[il])

    def _obj_location(self, obj, l=0):
        if not self._sorted:
            raise RuntimeError("No by-value access to an unserted list")
        il = 0
        if len(self._mins) > 1 and obj > self._mins[0]:
            if l:
                il = bisect.bisect_left(self._mins, obj) - 1
            else:
                il = bisect.bisect_right(self._mins, obj) - 1
        if l:
            ii = bisect.bisect_left(self._lists[il], obj)
        else:
            ii = bisect.bisect_right(self._lists[il], obj)
        return (il, ii)

    def insert(self, index, obj):
        (il, ii) = self._index_location(index)
        self._lists[il].insert(ii, obj)
        for j in range(il + 1, len(self._starts)):
            self._starts[j] += 1
        self._rebalance(il)

    def append(self, obj):
        if len(self._lists[-1]) >= self._load:
            self._insert_list()
        self._lists[-1].append(obj)
        if self._sorted and self._mins[0] is None:
            self._mins[0] = self._lists[0][0]

    def extend(self, iter):
        for n in iter:
            self.append(n)

    def pop(self, index=None):
        if index is None:
            index = -1
        (il, ii) = self._index_location(index)
        item = self._lists[il].pop(ii)
        if self._sorted:
            if ii == 0 and len(self._lists[il]) > 0:
                self._mins[il] = self._lists[il][0]
        else:
            for j in range(il + 1, len(self._starts)):
                self._starts[j] -= 1
        self._rebalance(il)
        return item

    def clear(self):
        self._lists.clear()
        self._starts.clear()
        self._mins.clear()
        self._insert_list()

    def as_list(self):
        return sum(self._lists, [])

    def insort(self, obj, l=0):
        (il, ii) = self._obj_location(obj, l)
        self._lists[il].insert(ii, obj)
        if ii == 0:
            self._mins[il] = obj
        self._rebalance(il)

    def insort_left(self, obj):
        self.insort(obj, l=1)

    def add(self, obj):
        if self._sorted:
            self.insort(obj)
        else:
            self.append(obj)

    def __str__(self):
        return str(self.as_list())

    def __setitem__(self, index, obj):
        if isinstance(index, int):
            (il, ii) = self._index_location(index)
            self._lists[il][ii] = obj
        elif isinstance(index, slice):
            raise RuntimeError("Slice assignment is not supported")

    def __getitem__(self, index):
        if isinstance(index, int):
            (il, ii) = self._index_location(index)
            return self._lists[il][ii]
        elif isinstance(index, slice):
            rg = index.indices(len(self))
            if rg[0] == 0 and rg[1] == len(self) and rg[2] == 1:
                return self.as_list()
            return [self.__getitem__(index) for index in range(*rg)]

    def __iadd__(self, obj):
        if self._sorted:
            [self.insort(n) for n in obj]
        else:
            [self.append(n) for n in obj]
        return self

    def __delitem__(self, index):
        if isinstance(index, int):
            self.pop(index)
        elif isinstance(index, slice):
            rg = index.indices(len(self))
            [self.__delitem__(rg[0]) for i in range(*rg)]

    def __len__(self):
        if self._sorted:
            return sum([len(l) for l in self._lists])
        return self._starts[-1] + len(self._lists[-1])

    def __contains__(self, obj):
        if self._sorted:
            it = self.lower_bound(obj)
            return not it.iter_end() and obj == it.iter_getitem()
        else:
            for n in self:
                if obj == n:
                    return True
            return False

    def __bool__(self):
        return len(self._lists[0]) != 0

    def __iter__(self):
        if not self._irev:
            self._il = self._ii = 0
        else:
            self._il = len(self._lists) - 1
            self._ii = len(self._lists[self._il]) - 1
        return self

    def __reversed__(self):
        self._irev = 1
        self.__iter__()
        return self

    def _iter_fix(self):
        if not self._irev:
            if (self._il != len(self._lists) - 1 and
                    self._ii == len(self._lists[self._il])):
                self._il += 1
                self._ii = 0
        else:
            if self._il != 0 and self._ii == -1:
                self._il -= 1
                self._ii = len(self._lists[self._il]) - 1

    def __next__(self):
        item = self.iter_getitem()
        if not self._irev:
            self._ii += 1
        else:
            self._ii -= 1
        return item

    def iter_end(self):
        if not self._irev:
            return (self._il == len(self._lists) - 1 and
                    self._ii == len(self._lists[self._il]))
        else:
            return (self._il == 0 and self._ii == -1)

    def iter_getitem(self):
        if self.iter_end() or len(self._lists[0]) == 0:
            raise StopIteration("Iteration stopped")
        self._iter_fix()
        return self._lists[self._il][self._ii]

    def iter_del(self):
        item = self._lists[self._il].pop(self._ii)
        if self._sorted:
            if self._ii == 0 and len(self._lists[self._il]) > 0:
                self._mins[self._il] = self._lists[self._il][0]
        else:
            for j in range(self._il + 1, len(self._starts)):
                self._starts[j] -= 1
        self._rebalance(self._il)
        return item

    def lower_bound(self, obj):
        (self._il, self._ii) = self._obj_location(obj, l=1)
        return self

    def upper_bound(self, obj):
        (self._il, self._ii) = self._obj_location(obj)
        return self


###############################################################################
# Fug Class
###############################################################################


class Fug:
    """ Fug representation """

    def __init__(self, args):
        """ Default constructor """
        self.gsrt = args[0]
        self.asrt = args[1]
        self.gn = args[2]
        self.result = [0]*self.gn
        self.a = Fastlist(self.asrt, load=500, sorted=1)

    def calculate(self):
        """ Main calcualtion function of the class """

        for i in range(self.gn):
            g = self.gsrt[i]
            it = self.a.lower_bound((g[1], 0))
            if not it.iter_end():
                alb = it.iter_getitem()
                if alb[0] > g[0]:
                    return "No"
                self.result[g[2]] = alb[1]+1
                it.iter_del()
            else:
                return "No"

        answer = "Yes\n" + " ".join(map(str, self.result))

        return answer


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
    num = list(map(int, uinput().split()))
    gaps = []
    prevli = list(map(int, uinput().split()))
    for i in range(num[0] - 1):
        li = list(map(int, uinput().split()))
        min = li[0] - prevli[1]
        max = li[1] - prevli[0]
        gaps.append((max, min, i))
        prevli = li
    a = list(map(int, uinput().split()))
    alist = [(n, i) for i, n in enumerate(a)]

    # Decoding inputs into a list

    inputs = [sorted(gaps), sorted(alist), num[0]-1]

    return inputs


def calculate(test_inputs=None):
    """ Base class calculate method wrapper """
    return Fug(get_inputs(test_inputs)).calculate()


###############################################################################
# Unit Tests
###############################################################################


class unitTests(unittest.TestCase):

    def test_sample_tests(self):
        """ Quiz sample tests. Add \n to separate lines """

        # Sample test 1
        test = "4 4\n1 4\n7 8\n9 10\n12 14\n4 5 3 8"
        self.assertEqual(calculate(test), "Yes\n2 3 1")
        self.assertEqual(
            get_inputs(test),
            [[(3, 1, 1), (5, 2, 2), (7, 3, 0)],
             [(3, 2), (4, 0), (5, 1), (8, 3)], 3])

        # My tests
        test = "5 5\n1 1\n2 7\n8 8\n10 10\n16 16\n1 1 5 6 2"
        self.assertEqual(calculate(test), "Yes\n1 2 5 4")

        # Other tests
        test = "2 2\n11 14\n17 18\n2 9"
        self.assertEqual(calculate(test), "No")

        # Other tests
        test = (
            "2 1\n1 1\n1000000000000000000 1000000000000000000" +
            "\n999999999999999999")
        self.assertEqual(calculate(test), "Yes\n1")

        test = ("5 9\n1 2\n3 3\n5 7\n11 13\n14 20\n2 3 4 10 6 2 6 9 5")
        self.assertEqual(calculate(test), "Yes\n1 6 3 2")

        size = 2000
        test = str(size) + " " + str(size) + "\n"
        x = size*1000
        for i in range(size):
            test += str(x) + " " + str(x + i + 1) + "\n"
            x += 2 * (i + 1)
        for i in reversed(range(size)):
            test += str(i) + " "
        self.assertEqual(calculate(test)[0], "Y")

    def test_Fug_class__basic_functions(self):
        """ Fug class basic functions testing """

        # Constructor test
        d = Fug([[(1, 3, 1), (2, 5, 2), (3, 7, 0)],
                 [(3, 2), (4, 0), (5, 1), (8, 3)], 3])

        # Sort bridges
        self.assertEqual(d.asrt[0], (3, 2))

        # Sort Gaps
        self.assertEqual(d.gsrt[0], (1, 3, 1))

if __name__ == "__main__":

    # Avoiding recursion limitaions
    sys.setrecursionlimit(100000)

    if sys.argv[-1] == "-ut":
        unittest.main(argv=[" "])

    # Print the result string
    sys.stdout.write(calculate())
