def game_board(board):
    print(" --- --- ---")
    print("| %s | %s | %s |" % (board[7], board[8],board[9]))
    print(" --- --- ---")
    print("| %s | %s | %s |" % (board[4],board[5],board[6]))
    print(" --- --- ---")
    print("| %s | %s | %s |" % (board[1],board[2],board[3]))
    print(" --- --- ---")

numbers=range(0,10)
game_board(numbers)

def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or 
    (board[4] == mark and board[5] == mark and board[6] == mark) or 
    (board[1] == mark and board[2] == mark and board[3] == mark) or 
    (board[7] == mark and board[4] == mark and board[1] == mark) or 
    (board[8] == mark and board[5] == mark and board[2] == mark) or 
    (board[9] == mark and board[6] == mark and board[3] == mark) or 
    (board[7] == mark and board[5] == mark and board[3] == mark) or 
    (board[9] == mark and board[5] == mark and board[1] == mark))


def place_marker(board, marker, position):
	 board[position] = marker

#now for input
def player_input_fits_time():
    marker= ''
    
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

import random

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


