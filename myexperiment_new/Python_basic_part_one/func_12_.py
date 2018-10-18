#write a python program to remove and print every third number from list of numbers until the list becomes empty


new_list=list(range(0,20))
print(new_list)
add=True
while add==True:
	number=new_list.pop(3)
	print(number)
	if number not in range(0,21):
		add=False
	else:
		add=True
print("finish")