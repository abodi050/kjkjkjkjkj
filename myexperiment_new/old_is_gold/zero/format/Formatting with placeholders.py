print('hi\nmyname is : abdullah')
print("in this code we will do ")
#Formatting with placeholders
print("'Formatting with placeholders'")
#we have many type of format but the important are.

print("first: %s \nsecond:%d \nthried:%2.1f \n last:%r "%("hole world and number 123.456",56.22,33.1234,"evrything !"))

#as you can see {x:y} the X is number of word order inside the format and the Y is nuber of blanck after word to get them balnce

print('{0:<8} | {3:^8} | {2:>8}'.format('Left','Center','Right','example'))
#noitce the symbol before the ^
print('{0:-<8} | {1:o^8} | {2:+>8}'.format(11,22,33))

income = 990
spend = 550
remane = income - spend
print(f"\n\nmy salery is {income}\n and my spend {spend}\n so the remane will be {remane} ")
print("\n\n\n")
name = 'Fred'

print(f"He said his name is {name}.")