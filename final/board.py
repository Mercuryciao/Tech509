import random

class Game():
    def __init__(self, playerX, playerO):
        self.board = [[None, None, None],
                    [None, None, None],
                    [None, None, None]]
        self.playerX = playerX
        self.playerO = playerO
        self.board_index = [(0, 0), (0 ,1), (0, 2), 
                            (1, 0), (1, 1), (1, 2), 
                            (2, 0), (2, 1), (2, 2)]

class Bot:
    def move(self, board, board_index, player):
        """When play with bot, it's the logic in bot turn."""
        print("It's bot turn!")
        row, col = random.choice(board_index)
        board[int(row)][int(col)] = player
        board_index.remove((int(row), int(col)))
        return board

class Human:
    def move(self, board, board_index, player):
        """When play with bot, it's the logic in human turn."""
        print("It's", player, "'s", "turn!")
        row, col = input("Enter row and col values: ").split()
        board[int(row)][int(col)] = player
        board_index.remove((int(row), int(col)))
        return board