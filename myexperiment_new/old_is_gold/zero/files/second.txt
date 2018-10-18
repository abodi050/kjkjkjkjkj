#40. Write a Python program to compute the distance between the points (x1, y1) and (x2, y2). 
import math

def user_input(order):
	x=int(input("where your %s X : "%(order)))
	y=int(input("what about %s Y : "%(order)))
	return (x,y)
result=0

done="NO"
while done=="NO":
	add=0
	x_value_1 , y_value_1 =user_input("First")
	x_value_2 , y_value_2 =user_input("Second")
	result=((x_value_1-x_value_2)**2+(y_value_1-y_value_2)**2)**0.5
	print("here your result : ",result)
	while add==0:
		add=input("are you finish (Yes or No)").upper()
		if (add=="YES" or add=="NO"):
			add=1
		else:
			add=0

		
		
		




