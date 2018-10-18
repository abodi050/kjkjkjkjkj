#write a python function that takes a sequence of numbers and ditermines if all the numbers are different from each other 

done=""

new_list=[]
while done!="YES":
	user_input=int(input("write your number: "))
	new_list.append(user_input)
	print("these are your number \n",new_list)
	done=input("do you want to contuino: ").upper()
print(new_list)

if len(new_list)!=len(set(new_list)):
	print("we have similer")
else:
	print("your safe")