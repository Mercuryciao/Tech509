import unittest
import logic

class TestLogic(unittest.TestCase):
    def test_get_winner(self):
        board = [
            [None, None, 'X'],
            ['O', 'X', None],
            ['O', 'O', 'O'],
        ]
        self.assertEqual(logic.Board().get_winner(board), 'O')

    def test_make_empty_board(self):
        board = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]
        self.assertEqual(logic.Board().make_empty_board(), board)

    def test_other_player(self):
        player = 'X'
        self.assertEqual(logic.Board().other_player(player), 'O')
    
    def test_bot_turn(self):
        board = [
            ['O', 'X', 'O'],
            [None, 'X', 'O'],
            [None, 'X', None],
        ]
        self.assertEqual(logic.Board().bot_turn(board), 'X')

    def test_human_turn(self):
        board = [
            ['O', 'X', 'O'],
            ['X', 'O', 'O'],
            ['O', 'X', 'X'],
        ]
        self.assertEqual(logic.Board().human_turn(board), True)


if __name__ == '__main__':
    unittest.main()