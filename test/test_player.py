import unittest
import mock
from tic_tac_toe.player import Player


class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player('X')

    def test_init(self):
        self.assertEqual(self.player.symbol, 'X')

    def test_input_mark(self):
        with mock.patch('builtins.input', return_value='2'):
            marker_tuple = self.player.input_mark()
        self.assertEqual(marker_tuple, ('2', 'X'))

    def test_place_mark(self):
        with self.subTest():
            mark_indices = self.player.place_mark(board=[['X', 'X', 'X'], ['4', '5', '6'], ['7', '8', '9']],
                                                  player_input=('8', 'X'))
            self.assertEqual(mark_indices, (2, 1))

        with self.subTest():
            failed_placement = self.player.place_mark(board=[['X', 'X', 'X'], ['4', '5', '6'], ['7', 'X', '9']],
                                                      player_input=('8', 'X'))
            self.assertFalse(failed_placement)

    def tearDown(self):
        del self.player


if __name__ == '__main__':
    unittest.main()
