import random
class Board():
    def __init__(self):
        self.player = 'O'
        self.board_index = [(0, 0), (0 ,1), (0, 2), 
                            (1, 0), (1, 1), (1, 2), 
                            (2, 0), (2, 1), (2, 2)]

    def make_empty_board(self):
        return [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]
    
    def get_winner(self, board):
        """Determines the winner of the given board.
        Returns 'X', 'O', or None."""
        n = len(board)
        win = None
        # horizontal
        for row in board:
            player = row[0]
            if player:
                win = True
                for col in row:
                    if col != player:
                        win = False
                        break
                if win:
                    return player

        # vertical
        for i in range(n):
            player = board[0][i]
            if player:
                win = True
                for j in range(n):
                    if board[j][i] != player:
                        win = False
                        break
                if win:
                    return player

        # diagonal
        for i in range(n):
            player = board[0][0]
            if player:
                win = True
                if board[i][i] != player:
                    win = False
                    break
        if win:
            return player

        for i in range(n):
            player = board[0][n-1]
            if player:
                win = True
                if board[i][n-1-i] != player:
                    win = False
                    break
        if win:
            return player
        return None

    def other_player(self, player):
        if player == 'O':
            return 'X'
        elif player == 'X':
            return 'O'
    
    def bot_turn(self, board):
        """When play with bot, it's the logic in bot turn."""
        print("It's bot turn!")
        row, col = random.choice(self.board_index)
        board[int(row)][int(col)] = self.player
        self.board_index.remove((int(row), int(col)))
        print(board[0], '\n', board[1], '\n', board[2])
        self.player = self.other_player(self.player)
        return board
        

    def human_turn(self, board):
        """When play with bot, it's the logic in human turn."""
        print("It's your turn!")
        row, col = input("Enter row and col values: ").split()
        board[int(row)][int(col)] = self.player
        self.board_index.remove((int(row), int(col)))
        self.player = self.other_player(self.player)
        return board