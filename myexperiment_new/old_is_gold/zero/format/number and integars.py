#we did the basic of board here
#in the end we try users


def game_board(u1, u2, u3, u4, u5, u6, u7, u8, u9):
    print(" --- --- ---")
    print("| %s | %s | %s |" % (u1, u2, u3))
    print(" --- --- ---")
    print("| %s | %s | %s |" % (u4, u5, u6))
    print(" --- --- ---")
    print("| %s | %s | %s |" % (u7, u8, u9))
    print(" --- --- ---")


loop = True
q1 = ""
q2 = ""
q3 = ""
q4 = ""
q5 = ""
q6 = ""
q7 = ""
q8 = ""
q9 = ""
while loop == True:
    q1 = input("please chose your:")
    game_board(q1, q2, q3, q4, q5, q6, q7, q8, q9)
    q2 = input("please chose your:")
    game_board(q1, q2, q3, q4, q5, q6, q7, q8, q9)
    q3 = input("please chose your:")
    game_board(q1, q2, q3, q4, q5, q6, q7, q8, q9)
    q4 = input("please chose your:")
    game_board(q1, q2, q3, q4, q5, q6, q7, q8, q9)
    q5 = input("please chose your:")
    game_board(q1, q2, q3, q4, q5, q6, q7, q8, q9)
    q6 = input("please chose your:")
    game_board(q1, q2, q3, q4, q5, q6, q7, q8, q9)
    q7 = input("please chose your:")
    game_board(q1, q2, q3, q4, q5, q6, q7, q8, q9)
    q8 = input("please chose your:")
    game_board(q1, q2, q3, q4, q5, q6, q7, q8, q9)
    q9 = input("please chose your:")
    game_board(q1, q2, q3, q4, q5, q6, q7, q8, q9)
    loop = False

game_board(q1, q2, q3, q4, q5, q6, q7, q8, q9)
'''
loop = True
while loop == True:
    name_player1 = input("player number one 1: ")
    name_player2 = input("player number two 2: ")
    loop==False
'''
