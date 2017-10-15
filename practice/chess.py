#!/usr/bin/env python3

import unittest


class Chess:

    PL_W = 'white'
    PL_B = 'black'

    def __init__(self, args=None):
        self.current_player = Chess.PL_W


class unitTests(unittest.TestCase):

    def test_Chess_(self):
        d = Chess()
        # Starting player plays white
        self.assertEqual(d.current_player, Chess.PL_W)
        # Each player has 16 pices
        self.assertEqual(

if __name__ == "__main__":
    unittest.main(argv=[" "])
