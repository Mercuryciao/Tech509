# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.
import board
import logic
import pandas as pd


if __name__ == '__main__':

    mode = input("Enter player(human or bot): ")
    winner = None
    player1name = None
    player2name = None
    result_data = pd.read_csv('database.csv')

    # Choose to play with bot or human
    if mode == 'bot':
        start_point = input("Who to start(bot or me): ")
        # Choose who is the first
        
        if start_point == 'bot':
            player1name = 'bot'
            player2name = input("What's your name: ")
            game = board.Game(board.Bot(), board.Human())
        elif start_point == 'me':
            player2name = 'bot'
            player1name = input("What's your name: ")
            game = board.Game(board.Human(), board.Bot())

    elif mode == 'human':
        # Choose to play with human
        player1name = input("What's your name player1: ")
        player2name = input("What's your name player2: ")
        game = board.Game(board.Human(), board.Human())
    
    while winner == None:
        # playerX turn
        game.board = game.playerX.move(game.board, game.board_index, 'X')
        print(game.board[0], '\n', game.board[1], '\n', game.board[2])
        winner = logic.get_winner(game.board)
        if winner:
            print('Winner: X!')
            result_data = logic.record_result(result_data, player1name, player2name, winner)
            break
        if len(game.board_index) == 0:
            print('It\'s a tie')
            print(winner)
            result_data = logic.record_result(result_data, player1name, player2name, winner)
            print(result_data)
            break

        # playerO turn
        game.board = game.playerO.move(game.board, game.board_index, 'O')
        print(game.board[0], '\n', game.board[1], '\n', game.board[2])
        winner = logic.get_winner(game.board)
        if winner:
            print('Winner: O!')
            result_data = logic.record_result(result_data, player1name, player2name, winner)
            break
        if len(game.board_index) == 0:
            print('It\'s a tie')
            print(winner)
            result_data = logic.record_result(result_data, player1name, player2name, winner)
            print(result_data)
            break

    print(result_data)
    result_data.to_csv('database.csv', index=False)