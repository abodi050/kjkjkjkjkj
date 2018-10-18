class Person:
	def __init__(self,name,mat):
		self.name=name
		self.mat=mat
		
	def count(self):
		return len(mat)
		

P_1=Person("abdullah",{"tea":230,"coffee":30})	

print(P_1.mat["tea"])

add="";done="";new_dict={};i=0;the_new_new_dict={};new_done=""
counter=0
while add!="YES":
	while new_done!="YES":
		#counter+=1
		name=input("please type your name: ")
		while done!="YES":
			i+=1
			mat=input("Martial: ")
			count=int(input("enter your number:"))
			new_dict[mat]=count
			done=input("are you done : ").upper()
		
		p_=Person(name,new_dict)
		the_new_new_dict[name]=new_dict
		print(the_new_new_dict)
		print(P_.name)
		print(list(P_.mat)[0])
		print(new_dict)
		new_done=input("Done??? : ").upper()
	add=input("Done??? : ").upper()
		
	

	'''
class Person:
	def __init__(self,name,mat):
		self.name=name
		self.mat=mat
		
	def count(self):
		return len(mat)
		

P_1=Person("abdullah",{"tea":230,"coffee":30})	

print(P_1.mat["tea"])

add="";done="";new_dict={};i=0
counter=0
while add!="YES":
	counter=+1
	name=input("please type your name: ")
	while done!="YES":
		i+=1
		mat=input("Martial: ")
		count=int(input("enter your number:"))
		new_dict[mat]=count
		done=input("are you done : ").upper()
		
	P_2=Person(name,new_dict)
	print(P_2.name)
	print(list(P_2.mat.values())[0])
	print(new_dict)
	add=input("Done??? : ").upper()
		
	
'''