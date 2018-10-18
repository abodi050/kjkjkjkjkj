#Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn



def user_input():
	user= input("please input your number : ")
	return user

def user_func(user):
	new_user=int(user)+int(user+user)+int(user+user+user)
	return new_user


user=user_input()
print(user_func(user))

