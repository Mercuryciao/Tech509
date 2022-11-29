# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.
import random
import board
import logic
import pandas as pd
import numpy as np


if __name__ == '__main__':
    mode = input("Enter player(human or bot): ")
    winner = None
    # Choose to play with bot or human

    if mode == 'bot':
        start_point = input("Who to start(bot or me): ")
        # Choose who is the first
        if start_point == 'bot':
            game = board.Game(board.Bot(), board.Human())
        elif start_point == 'me':
            game = board.Game(board.Human(), board.Bot())
    elif mode == 'human':
        # Choose to play with human
        game = board.Game(board.Human(), board.Human())
    
    while winner == None:
        # playerX turn
        game.board = game.playerX.move(game.board, game.board_index, 'X')
        print(game.board[0], '\n', game.board[1], '\n', game.board[2])
        winner = logic.get_winner(game.board)
        if winner:
            print('Winner: X!')
            break
        if len(game.board_index) == 0:
            print('It\'s a tie')
            break

        # playerO turn
        game.board = game.playerO.move(game.board, game.board_index, 'O')
        print(game.board[0], '\n', game.board[1], '\n', game.board[2])
        winner = logic.get_winner(game.board)
        if winner:
            print('Winner: O!')
            break
        if len(game.board_index) == 0:
            print('It\'s a tie')
            break
