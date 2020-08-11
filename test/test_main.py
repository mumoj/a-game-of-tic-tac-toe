import unittest
import mock
import main


class MainTests(unittest.TestCase):

    def test_initial_player(self):
        with self.subTest():
            with mock.patch('builtins.input', return_value='X'):
                first_player = main.initial_player()
                self.assertEqual(first_player, [True, 'X'])

        with self.subTest():
            with mock.patch('builtins.input', return_value='o'):
                first_player = main.initial_player()
                self.assertEqual(first_player, [True, 'O'])

    def test_change_turns(self):
        with self.subTest():
            player_on_turn = main.change_turns('X')
            self.assertEqual(player_on_turn, [False, 'O'])

        with self.subTest():
            player_on_turn = main.change_turns('O')
            self.assertEqual(player_on_turn, [False, 'X'])

    def test_exit_condition(self):

        with self.subTest():
            with mock.patch('builtins.input', return_value='Y'):
                exit_condition = main.exit_condition()
                self.assertTrue(exit_condition)

            with self.subTest():

                with mock.patch('builtins.input', return_value='N'):
                    exit_condition = main.exit_condition()
                    self.assertFalse(exit_condition)


if __name__ == '__main__':
    unittest.main(verbosity=2)
