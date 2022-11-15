# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.
import random
import logic

if __name__ == '__main__':
    """Create board and choose to play with bot or human."""
    game_board = logic.Board()
    board = game_board.make_empty_board()
    mode = input("Enter player(human or bot): ")
    winner = None
    
    # Choose to play with bot
    if mode == 'bot':
        # Choose who to start first
        start_point = input("Who to start(bot or me): ")
        if start_point == 'bot':
            while winner == None:
                
                # bot turn
                board = game_board.bot_turn(board)
                winner = game_board.get_winner(board)
                if winner:
                    print('Winner: Bot!')
                    break
                if len(game_board.board_index) == 0:
                    print('It\'s a tie')
                    break

                # human turn
                board = game_board.human_turn(board)
                winner = game_board.get_winner(board)
                if winner:
                    print('Winner: You!')
                    break
                if len(game_board.board_index) == 0:
                    print('It\'s a tie')
                    break

        elif start_point == 'me':
            while winner == None:
                # human turn
                board = game_board.human_turn(board)
                winner = game_board.get_winner(board)

                if winner:
                    print('Winner: You!')
                    break
                if len(game_board.board_index) == 0:
                    print('It\'s a tie')
                    break

                # bot turn
                board = game_board.bot_turn(board)
                winner = game_board.get_winner(board)
                if winner:
                    print('Winner: Bot!')
                    break
                if len(game_board.board_index) == 0:
                    print('It\'s a tie')
                    break
                

    # Choose to play with human
    elif mode == 'human':
        while winner == None:
            board = game_board.human_turn(board)
            winner = game_board.get_winner(board)

            if winner:
                print('Winner: ', winner)
                break
            if len(game_board.board_index) == 0:
                print('It\'s a tie')
                break
            
