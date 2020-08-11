import unittest
from tic_tac_toe.game import Game
import mock


class TestGame(unittest.TestCase):

    def setUp(self):
        self.the_game = Game()

    def test_init(self):
        self.assertEqual(self.the_game.board, [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']])

    def test_show_board(self):
        self.assertIsNone(self.the_game.show_board())

    def test_determine_win(self):
        with self.subTest():
            self.the_game.board = [['X', 'X', 'X'],
                                   ['4', '5', '6'],
                                   ['7', '8', '9']]
            row_win = self.the_game.determine_win((0, 0))
            self.assertTrue(row_win)

        with self.subTest():
            self.the_game.board = [['0', 'X', 'X'],
                                   ['0', '5', '6'],
                                   ['0', '8', '9']]
            column_win = self.the_game.determine_win((0, 0))
            self.assertTrue(column_win)

        with self.subTest():
            self.the_game.board = [['0', 'X', 'X'],
                                   ['X', '0', '6'],
                                   ['0', '8', '0']]
            diagonal_win = self.the_game.determine_win((0, 0))
            self.assertTrue(diagonal_win)

        with self.subTest():
            self.the_game.board = [['0', 'X', 'X'],
                                   ['X', 'X', '6'],
                                   ['X', '8', '0']]
            reverse_diagonal_win = self.the_game.determine_win((0, 2))
            self.assertTrue(reverse_diagonal_win)

    def test_determine_draw(self):

        with self.subTest():
            self.the_game.board = [['0', '5', 'X'], ['X', 'x', '0'], ['X', '0', '0']]
            blank_position_in_first_sublist = self.the_game.determine_draw()
            self.assertFalse(blank_position_in_first_sublist)

        with self.subTest():
            self.the_game.board = [['0', '0', 'X'], ['X', '5', '0'], ['X', '0', '0']]
            blank_position_in_second_sublist = self.the_game.determine_draw()
            self.assertFalse(blank_position_in_second_sublist)

        with self.subTest():
            self.the_game.board = [['0', '0', 'X'], ['X', 'x', '0'], ['X', '0', '5']]
            blank_position_in_last_sublist = self.the_game.determine_draw()
            self.assertFalse(blank_position_in_last_sublist)

    def tearDown(self):
        del self.the_game


if __name__ == '__main__':
    unittest.main()
