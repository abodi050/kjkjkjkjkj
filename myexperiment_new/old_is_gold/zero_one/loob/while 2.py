#__#
#import LIST.lists
num = open("list.txt","r")
#to count lines
num.seek(0)
x= 0
y=1
num = num.read().split(',')
while x < 10:
	print ("name :", num[x])
	print ("age :", num[y])
	x+=2
	y+=2
