def game_board(board):
    print(" --- --- ---")
    print("| %s | %s | %s |" % (board[7], board[8], board[9]))
    print(" --- --- ---")
    print("| %s | %s | %s |" % (board[4], board[5], board[6]))
    print(" --- --- ---")
    print("| %s | %s | %s |" % (board[1], board[2], board[3]))
    print(" --- --- ---")


def player_input():
    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


def choose_first():
    import random
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or 
    (board[4] == mark and board[5] == mark and board[6] == mark) or 
    (board[1] == mark and board[2] == mark and board[3] == mark) or 
    (board[7] == mark and board[4] == mark and board[1] == mark) or 
    (board[8] == mark and board[5] == mark and board[2] == mark) or 
    (board[9] == mark and board[6] == mark and board[3] == mark) or 
    (board[7] == mark and board[5] == mark and board[3] == mark) or 
    (board[9] == mark and board[5] == mark and board[1] == mark))


def space_check(board, position):
    
    return board[position] == ' '


def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True


#_______________________________________
board = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
numbers = range(0, 10)
game_board(board)
game_board(numbers)
#_______________________________________
player1, player2 = player_input()
print("player 1 will play with : ",player1, "\n","player 2 will play with : ", player2)

choose_first()
if choose_first() == 'Player 1':
    player = player1
else:
    player = player2

add=""
while add!="yes":
	position = int(input("where do you want to play: "))
	if space_check(board, position)==True:
		place_marker(board, player, position)
		game_board(board)
		if win_check(board,"X")==True or win_check(board,"O")==True:
			print("winnnner")
			break
		if player == player1:
			player = player2
		else:
			player = player1
		#add=input("done: ")
		print("done: ")
	else:
		
		if full_board_check(board)==True:
			break
		else:
			print("\ntry agine\n")







'''
position = int(input("where do you want to play"))
place_marker(board, player, position)
game_board(board)
'''