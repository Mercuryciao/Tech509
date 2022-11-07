# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import make_empty_board
from logic import get_winner
from logic import other_player


if __name__ == '__main__':
    board = make_empty_board()
    player = input("Enter player O or X: ")
    winner = None
    while winner == None:
        print("It's your turn: ", player)
        print(board[0], '\n', board[1], '\n', board[2])
        row, col = input("Enter row and col values: ").split()
        board[int(row)][int(col)] = player
        winner = get_winner(board)
        if winner:
            break
        player = other_player(player)
    print('Winner:', winner)