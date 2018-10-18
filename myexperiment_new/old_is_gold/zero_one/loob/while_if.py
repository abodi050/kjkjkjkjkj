#we will use import here
#while x<3:
#keeping=input("do you want to continue : " )
name={}
z=0
x=1
while z!=55:
	name["name",x]=input("please type your name : ")
	name["age",x]=int(input("           age  : "))
	x+=1
	keeping=input("do you want to continue : " )
	if keeping == "yes":
		z+=1
	else:
		z=55 
print(name)
#print(age)