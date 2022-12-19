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
        board = [
            [None, None, 'X'],
            ['O', 'X', None],
            ['X', 'O', 'O'],
        ]
        self.assertEqual(logic.get_winner(board), 'X')
        board = [
            ['X', 'O', 'X'],
            ['O', 'X', 'O'],
            ['O', 'X', 'O'],
        ]
        self.assertEqual(logic.get_winner(board), None)

    def test_make_empty_board(self):
        board = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]
        self.assertEqual(logic.make_empty_board(), board)

    def test_other_player(self):
        player = 'X'
        self.assertEqual(logic.other_player(player), 'O')
        player = 'O'
        self.assertEqual(logic.other_player(player), 'X')

if __name__ == '__main__':
    unittest.main()