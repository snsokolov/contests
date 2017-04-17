#!/usr/bin/env python3
# snap.py - Snap program by Sergey 2017

import random
import unittest

###############################################################################
# Snap Class (Main Program)
###############################################################################


class Snap:
    """Snap Card Game"""

    ST_OK = 0  # Game is running, no winners yet
    ST_END = 1  # Game finished

    S = 0  # Spades
    H = 1  # Hearts
    D = 2  # Diamonds
    C = 3  # Clubs
    suits = [S, H, D, C]

    J = 11  # Jack
    Q = 12  # Queen
    K = 13  # King
    A = 14  # Ace
    ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A]

    def __init__(self, players=2, dealer=0):
        """Default constructor"""
        # Number of players
        assert(players > 1), "More than 2 players only"
        assert(dealer >= 0 and dealer < players), "Wrong dealer"
        self.players = players

        # Players in game
        self.active_players = set([i for i in range(self.players)])

        # Unsorted Deck of cards
        self.deck = []
        for suit in Snap.suits:
            for rank in Snap.ranks:
                self.deck.append((rank, suit))

        # Current game state
        self.state = Snap.ST_OK

        # Player 0 is the starting player
        self.curp = self.next_player(dealer)

        # Players piles
        self.piles = [[] for i in range(self.players)]

        # Init snap pools
        self.pools = []

        # Init discard piles
        self.discards = [[] for i in range(self.players)]

        # Init the winner
        self.winner = None

        # Shuffle the deck
        shuffled_deck = [i for i in range(len(self.deck))]
        random.shuffle(shuffled_deck)

        # Fill of players piles
        deal_player = self.curp
        for card in shuffled_deck:
            self.piles[deal_player].append(card)
            deal_player = self.next_player(deal_player)

    def move(self):
        """One moves of the game"""
        # No more moves if game is finished
        if self.state == Snap.ST_END:
            return

        # Show the card and put it into dicard pile
        cur_pile = self.piles[self.curp]
        cur_discard = self.discards[self.curp]
        if not cur_pile and not cur_discard:
            # Player is lost
            self.active_players.remove(self.curp)

            # Game ended, we have a winner
            if len(self.active_players) == 1:
                self.state = Snap.ST_END
                self.winner = list(self.active_players)[0]
        else:
            if not cur_pile:
                # Move cards from dicard pile
                self.move_pile(cur_discard, cur_pile)

            # Turn over one card
            cur_discard.append(cur_pile.pop())

        # Swith the current player to the next player
        self.curp = self.next_player(self.curp)

    def nmoves(self, num):
        """Consecutive move of a game"""
        for i in range(num):
            self.move()

    def snap_call(self, player):
        """Player calls Snap!"""
        # No more moves if game is finished
        if self.state == Snap.ST_END:
            return

        # Create a dict of maching top card ranks for all discard piles
        ranks = {}
        for discard_owner, discard in enumerate(self.discards):
            if discard:
                rank = self.deck[discard[-1]][0]
                if rank not in ranks:
                    ranks[rank] = []
                ranks[rank].append(discard_owner)

        good_call = False

        for rank in ranks.keys():
            # Take all discard piles with more than 1 matching rank
            if len(ranks[rank]) >= 2:
                good_call = True
                for discard_owner in ranks[rank]:
                    # Pop all discard cards into the caller's pile
                    self.move_pile(
                        self.discards[discard_owner], self.piles[player])

        # Create a new pool if snap attemp was not good
        if not good_call:
            self.pools.append(self.discards[player])
            self.discards[player] = []

    def snap_pool_call(self, player):
        """Player calls Snap!"""
        # No more moves if game is finished
        if self.state == Snap.ST_END:
            return

        # Create a dict of discard top card rank for each discard pile
        disc_rank = {}
        for discard_owner, discard in enumerate(self.discards):
            if discard:
                disc_rank[discard_owner] = self.deck[discard[-1]][0]

        # Create a dict of maching top card ranks for all pool piles
        pool_ranks = {}
        for pool_idx, pool in enumerate(self.pools):
            assert(pool), "No empty pools allowed"
            rank = self.deck[pool[-1]][0]
            if rank not in pool_ranks:
                pool_ranks[rank] = []
            pool_ranks[rank].append(pool_idx)

        good_call = False

        for discard_owner in disc_rank.keys():
            # Take all pool piles with at least 1 matching rank
            rank = disc_rank[discard_owner]
            if rank in pool_ranks:
                good_call = True
                # First pop all discard cards into the caller's pile
                self.move_pile(
                    self.discards[discard_owner], self.piles[player])

                # Then pop all pool cards into the caller's pile
                for pool_idx in pool_ranks[rank]:
                    self.move_pile(self.pools[pool_idx], self.piles[player])

        # Cleanup pools
        self.pools = list(filter(None, self.pools))

        # Create a new pool if snap attempt was not good
        if not good_call:
            self.pools.append(self.discards[player])
            self.discards[player] = []

    def next_player(self, player):
        assert(self.active_players), "No active players"
        while True:
            player = (player + 1) % self.players
            if player in self.active_players:
                break
        return player

    def move_pile(self, src, dst):
        while src:
            dst.append(src.pop())


###############################################################################
# Unit Tests
###############################################################################


class unitTests(unittest.TestCase):

    def test_Snap_game_start(self):
        """Check game start state"""
        d = Snap()

        # 2 players by default, each has half of the deck cards
        self.assertEqual(len(d.piles[0]), 26)
        self.assertEqual(len(d.piles[1]), 26)

        # Pool is empty
        self.assertEqual(len(d.pools), 0)

        # Discard pile per player are empty
        self.assertEqual(len(d.discards[0]), 0)
        self.assertEqual(len(d.discards[1]), 0)

        # Current player is player 1, because dealer is 0 by default
        self.assertEqual(d.curp, 1)

        # Current game state
        self.assertEqual(d.state, Snap.ST_OK)

    def test_Snap_game_first_moves(self):
        """Check game first move"""
        d = Snap()

        # Current player moves
        d.move()

        # Current player now is player 0
        self.assertEqual(d.curp, 0)

        # Piles are updated
        self.assertEqual(len(d.piles[1]), 25)

    def test_Snap_deck(self):
        """Check the deck is shuffled"""
        # First card in deck is 2 of Spades
        d = Snap()
        self.assertEqual(d.deck[0], (2, Snap.S))

        # Make sure piles for two different games are different (shuffled)
        self.assertNotEqual(Snap().piles[0], Snap().piles[0])

    def test_Snap_discard_pile_turn_over(self):
        """Check discard pile is re-used"""
        # Make 52 moves to deal all cards
        d = Snap()
        d.nmoves(53)

        # Check than discarded cards are re-used
        self.assertEqual(len(d.piles[1]), 25)

    def test_Snap_bad_snap_call(self):
        """Check bad snap call"""
        # Move and do a bad snap call from player 1 creates a snap pool
        d = Snap()
        d.move()
        d.snap_call(1)

        # Discard pile of a player is empty
        self.assertEqual(d.discards[1], [])

        # New pool added
        self.assertEqual(len(d.pools[0]), 1)

    def test_Snap_next_player_helping_function(self):
        d = Snap(3)
        # Default active players for a game of 3
        self.assertEqual(d.active_players, set([0, 1, 2]))

        # Next player after 2 is 0
        self.assertEqual(d.next_player(2), 0)

        # Remove player 1 from active players
        d.active_players = set([0, 2])

        # Next player after 0 should be 2
        self.assertEqual(d.next_player(0), 2)

    def test_Snap_game_end(self):
        """In three player game if two players out, last one is the winner"""
        # Player 1 has no more cards
        d = Snap(players=3)
        d.curp = 1
        d.piles[1] = []
        d.discards[1] = []
        d.move()

        # Player 1 is lost
        self.assertEqual(d.active_players, set([0, 2]))
        self.assertEqual(d.winner, None)

        # Player 2 has no more cards
        d.piles[2] = []
        d.discards[2] = []
        d.move()

        # Player 2 is lost, so player 0 is the winner
        self.assertEqual(d.state, Snap.ST_END)
        self.assertEqual(d.winner, 0)

        # No more moves after the game is finished
        d.move()
        self.assertEqual(len(d.piles[0]), 17)

    def test_Snap_good_snap_call(self):
        """Check good snap call"""
        # Good snap call from player one takes all matching cards
        d = Snap()
        d.piles[1] = []
        d.discards = [[3, 1], [2], [4, 1]]
        d.snap_call(1)

        # Player one takes all matching cards
        self.assertEqual(d.piles[1], [1, 3, 1, 4])

        # No pools added
        self.assertEqual(len(d.pools), 0)

    def test_Snap_good_snap_pool_call(self):
        """Check good snap pool call"""
        # Good snap call from player when top pool card matches discard card
        d = Snap()
        d.piles[1] = []
        d.discards = [[3, 1], [2], []]
        d.pools = [[5, 1], [6, 1], [7]]
        d.snap_pool_call(1)

        # Player one takes all matching cards
        self.assertEqual(d.piles[1], [1, 3, 1, 5, 1, 6])

        # No pools added
        self.assertEqual(d.pools, [[7]])

    def test_Snap_bad_snap_pool_call(self):
        """Check bad snap pool call"""
        # Bad snap call from player when top pool card doesn't match
        d = Snap()
        d.piles[1] = []
        d.discards = [[3, 1], [2], []]
        d.pools = [[5, 4], [6, 8], [7]]
        d.snap_pool_call(1)

        # Discard pile of a player is empty
        self.assertEqual(d.discards[1], [])

        # New pool added
        self.assertEqual(d.pools[3], [2])

    def test_Snap_move_pile_helping_function(self):
        """Reverse and add cards from one pile into another"""
        d = Snap()
        src = [1, 2]
        dst = [4, 3]
        d.move_pile(src, dst)
        self.assertEqual(dst, [4, 3, 2, 1])
        self.assertEqual(src, [])

if __name__ == "__main__":
    unittest.main(argv=[" "])
