#17. Write a Python program to test whether a number is within 100 of 1000 or 2000

def user_input():
	add=True
	
	while add==True:
		user=int(input("please write a number with in 100 out of 1000 or 2000:"))
		if ( user <=1100 and user >=900 ) or (user <=2100 and user >=1900):
			print("you got it ")
			add=False
		else:
			print("try agine")
			add=True 
		

user_input()
		

