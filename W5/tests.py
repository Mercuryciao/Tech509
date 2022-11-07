import unittest
import logic


class TestLogic(unittest.TestCase):

    def test_get_winner(self):
        board = [
            [None, None, 'X'],
            ['O', 'X', None],
            ['O', 'O', 'O'],
        ]
        self.assertEqual(logic.get_winner(board), 'O')

    def test_make_empty_board(self):
        board = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]
        self.assertEqual(logic.make_empty_board(), board)

    def test_other_player(self):
        self.assertEqual(logic.other_player('X'), 'O')


if __name__ == '__main__':
    unittest.main()