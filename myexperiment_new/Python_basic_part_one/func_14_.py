#challenge from https://www.reddit.com/r/dailyprogrammer/comments/8xzwl6/20180711_challenge_365_intermediate_sales/

'''
def screen(**data):
	print("%s\n\n\n"%(data["main"]))
	print("{0:10} {1:10} {2:10}".format(data["mat_1"],data["num_1"],data["num_2"]))
	print("{0:10} {1:10} {2:10} ".format(data["mat_2"],data["num_3"],data["num_4"]))
	
screen(main="Revenue",name_1="Franck",name_2="Robot",mat_1="tea",mat_2="coffee",num_1=1,num_2=2,num_3=3,num_4=4)

'''
import sys

def screen(**data):
	for i in x:
	sys.stdout.flush()
	sys.stdout.write(i+"	") 

x=["abdullah	",'khalid	','sysss	']

'''
sys.stdout.flush()
sys.stdout.write('hello')
print('hello',end='',flush=true)
'''