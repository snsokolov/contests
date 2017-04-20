#!/usr/bin/env python3

import unittest


class Tictac:
    ST_OK = 0  # Game is not finished
    ST_END = 1  # Game finished

    MV_OK = 0  # Valid move
    MV_BAD = 1  # Invalid move, out of bounds or not empty
    MV_GAMEOVER = 2  # Invalid move, game is over

    def __init__(self, players=2, size=3):
        self.size = size
        self.players = players
        self.current_player = 0
        self.empty = set([(i % size, i // size) for i in range(size**2)])
        self.moves = [set([]) for player in range(players)]
        self.state = Tictac.ST_OK
        self.winner = None

    def move(self, cell):
        # Check that game is not over
        if self.state != Tictac.ST_OK:
            return Tictac.MV_GAMEOVER

        # Check that cell is empty
        if cell not in self.empty:
            return Tictac.MV_BAD

        # Move the cell from empty set to a player's set
        self.empty.remove(cell)
        self.moves[self.current_player].add(cell)

        # Check for the winner
        if self.check_winner(self.current_player):
            self.state = Tictac.ST_END
            self.winner = self.current_player
            return Tictac.MV_OK

        # Check for the draw result
        if not self.empty:
            self.state = Tictac.ST_END
            return Tictac.MV_OK

        # Switch to the next player
        self.current_player = self.next_player(self.current_player)

        return Tictac.MV_OK

    def next_player(self, player):
        return (player + 1) % self.players

    def check_winner(self, player):
        cols = [0] * self.size
        rows = [0] * self.size
        diag1 = 0
        diag2 = 0

        for move in self.moves[player]:
            cols[move[1]] += 1
            rows[move[0]] += 1
            if move[0] == move[1]:
                diag1 += 1
            if move[0] + move[1] == self.size - 1:
                diag2 += 1
        for col in cols:
            if col == self.size:
                return True
        for row in rows:
            if row == self.size:
                return True
        if diag1 == self.size or diag2 == self.size:
            return True
        return False

    def sprint_result(self):
        result = []
        if self.state != Tictac.ST_OK:
            if self.winner is None:
                result.append("Result: Draw")
            else:
                result.append("Result: Winner player " + str(self.winner))
        return result

    def sprint_board(self):
        result = []
        for col in range(self.size):
            row_chars = []
            for row in range(self.size):
                cell_char = " "
                for player in range(self.players):
                    if (col, row) in self.moves[player]:
                        cell_char = str(player)
                row_chars.append(cell_char)
            result.append("|".join(row_chars))
        return result


###############################################################################
# Unit Tests
###############################################################################

class unitTests(unittest.TestCase):

    def test_tictac_start_game(self):
        # Start a new game
        t = Tictac()

        # Check that the game size is 3 by default
        self.assertEqual(t.size, 3)
        # Check that 2 players by default
        self.assertEqual(t.players, 2)
        # Check that starting player is player 0
        self.assertEqual(t.current_player, 0)
        # Check that there are 9 empty cells
        self.assertEqual(len(t.empty), 9)
        # Check that cell (2, 2) is empty
        self.assertTrue((2, 2) in t.empty)
        # Check that players haven't made any moves yet
        self.assertEqual(t.moves, [set([]), set([])])
        # Check that game is not finished
        self.assertEqual(t.state, Tictac.ST_OK)
        # Check that Winner is None i.e. it's a draw
        self.assertEqual(t.winner, None)

    def test_tictac_make_a_move(self):
        # Start a new game
        t = Tictac()
        # First move to a cell (0, 0)
        cell = (0, 0)

        # Check that move return value is okay
        self.assertEqual(t.move(cell), Tictac.MV_OK)
        # Check that cell is no longer empty
        self.assertTrue(cell not in t.empty)
        # Check that cell is in player 0 moves set
        self.assertTrue(cell in t.moves[0])
        # Check that current player is player 1
        self.assertEqual(t.current_player, 1)
        # Check that move to the same cell gives you an error
        self.assertEqual(t.move(cell), Tictac.MV_BAD)

    def test_tictac_next_player_helping_function(self):
        # Start a new game with 3 players
        t = Tictac(players=3)

        # Check that the next player after 0 is 1
        self.assertEqual(t.next_player(0), 1)
        # Check that the next player after 2 is 0
        self.assertEqual(t.next_player(2), 0)

    def test_tictac_make_a_winning_move(self):
        # Start a new game
        t = Tictac()
        # Add two moves for the player 1
        t.moves[1] = set([(0, 0), (0, 1)])
        # Set the current player to player 1
        t.current_player = 1
        # Make a winning move to a cell (0, 2)
        t.move((0, 2))

        # Check that the game ends after this move
        self.assertEqual(t.state, Tictac.ST_END)
        # Check that player 1 is the winner
        self.assertEqual(t.winner, 1)
        # Check that we can't make a move after the game ends
        self.assertEqual(t.move((2, 2)), Tictac.MV_GAMEOVER)

    def test_tictac_winner_helping_function(self):
        # Start a new game
        t = Tictac()

        # Check that player 1 is not the winner
        self.assertEqual(t.check_winner(1), False)

        # Check that 3 cells in a row make you the winner
        t.moves[1] = set([(0, 0), (1, 0), (2, 0)])
        self.assertEqual(t.check_winner(1), True)

        # Check that 3 cells in a column make you the winner
        t.moves[0] = set([(1, 0), (1, 1), (1, 2)])
        self.assertEqual(t.check_winner(0), True)

        # Check that 3 cells in a diagonal 1 make you the winner
        t.moves[0] = set([(0, 0), (1, 1), (2, 2)])
        self.assertEqual(t.check_winner(0), True)

        # Check that 3 cells in a diagonal 2 make you the winner
        t.moves[0] = set([(2, 0), (1, 1), (0, 2)])
        self.assertEqual(t.check_winner(0), True)

    def test_tictac_make_a_draw_move(self):
        # Start a new game
        t = Tictac()
        # Make only one empty cell remaining
        t.empty = set([(0, 0)])
        # Make the move
        t.move((0, 0))

        # Check that the game ends after this move
        self.assertEqual(t.state, Tictac.ST_END)
        # Check that None is the winner
        self.assertEqual(t.winner, None)

    def test_tictac_sprint_helping_function(self):
        # Start a new game
        t = Tictac()

        # Check not finished game result string
        self.assertEqual(t.sprint_result(), [])
        # Check finished game Draw result string
        t.state = Tictac.ST_END
        self.assertEqual(t.sprint_result(), ["Result: Draw"])
        # Check finished game winner result string
        t.winner = 1
        self.assertEqual(t.sprint_result(), ["Result: Winner player 1"])

        # Check empty board string
        self.assertEqual(t.sprint_board(), [" | | ", " | | ", " | | "])

        # Check non-empty board string
        t.moves = [set([(0, 0)]), set([(1, 1)])]
        self.assertEqual(t.sprint_board(), ["0| | ", " |1| ", " | | "])

    def test_tictac_play_a_random_game(self):
        t = Tictac()
        while t.state == Tictac.ST_OK:
            print()
            t.move(list(t.empty)[98 % len(t.empty)])
            print("\n".join(t.sprint_board()))
        print("\n".join(t.sprint_result()))

if __name__ == "__main__":
    unittest.main(argv=[" "])
