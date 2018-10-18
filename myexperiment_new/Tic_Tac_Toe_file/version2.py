#we continued from version 2 then done with grade

def game_board(u1, u2, u3, u4, u5, u6, u7, u8, u9):
    print(" --- --- ---")
    print("| %s | %s | %s |" % (u1, u2, u3))
    print(" --- --- ---")
    print("| %s | %s | %s |" % (u4, u5, u6))
    print(" --- --- ---")
    print("| %s | %s | %s |" % (u7, u8, u9))
    print(" --- --- ---")

def board():
    print(" --- --- ---")
    print("| 1 | 2 | 3 |")
    print(" --- --- ---")
    print("| 4 | 5 | 6 |")
    print(" --- --- ---")
    print("| 7 | 8 | 9 |")
    print(" --- --- ---")

def grading(u1, u2, u3, u4, u5, u6, u7, u8, u9):
	if u1==u2 and u2==u3:
		print("you are a winner")
	elif u4==u5 and u5==u6:
		print("you are a winner")		
	elif u7==u8 and u8==u9:
		print("you are a winner")

def playing(u1, u2, u3, u4, u5, u6, u7, u8, u9):
	place_turn=int(input("choose the place you want by numbers"))
	for i in list_place:
		if place_turn==list_place[i]
		return 
	play_turn=input("your Turn: ")


listplace=[u1,u2,u3,u4,u5,u6,u7,u8,u9]
board()

loop = True
q1 = " "
q2 = " "
q3 = " "
q4 = " "
q5 = " "
q6 = " "
q7 = " "
q8 = " "
q9 = " "
user1=input("please type your name 1 : ")
user2=input("please type your name 2 : ")

while loop==True:

	





while loop == True:
    q1 = input("please chose your:")
    game_board(q1, q2, q3, q4, q5, q6, q7, q8, q9)
    q2 = input("please chose your:")
    game_board(q1, q2, q3, q4, q5, q6, q7, q8, q9)
    q3 = input("please chose your:")
    grading(q1, q2, q3, q4, q5, q6, q7, q8, q9)
    loop=False
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
