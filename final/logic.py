def make_empty_board():
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]

def get_winner(board):
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

def other_player(player):
    if player == 'O':
        return 'X'
    elif player == 'X':
        return 'O'

def record_result(result_data, player1name, player2name, winner):
    max_game_id = result_data['Game'].max()
    df_id = len(result_data)

    if winner == 'O':
        result_data.loc[df_id] = {
            'Game': max_game_id+1, 
            'Player': player2name, 
            'Result': 'win'
        }
        result_data.loc[df_id+1] = {
            'Game': max_game_id+1, 
            'Player': player1name, 
            'Result': 'lose'
        }
    elif winner == 'X':
        result_data.loc[df_id] = {
            'Game': max_game_id+1, 
            'Player': player1name, 
            'Result': 'win'
        }
        result_data.loc[df_id+1] = {
            'Game': max_game_id+1, 
            'Player': player2name, 
            'Result': 'lose'
        }
    elif winner == None:
        result_data.loc[df_id] = {
            'Game': max_game_id+1, 
            'Player': player1name, 
            'Result': 'draw'
        }
        result_data.loc[df_id+1] = {
            'Game': max_game_id+1, 
            'Player': player2name, 
            'Result': 'draw'
        }


    return result_data

