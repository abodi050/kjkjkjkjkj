#Range function (start:stop:step)
print(list(range(0, 20, 5)))
print("\n\n___________________________________")
#enumerate
#this for loop so ,dont need for x+=1:
for i, num in enumerate("0985789"):
    print("hi{} and{}".format(i, num))
print(list(enumerate("0985789")))
print("\n\n")
for i, letter in enumerate('abcde'):
    print("At index {} the letter is {}".format(i, letter))
print(list(enumerate("abcde")))

print("\n\n___________________________________")

mylist1 = [1, 2, 3, 4, 5]
mylist2 = ['a', 'b', 'c', 'd', 'e']
print(list(zip(mylist1, mylist2)))

print("\n\n")
lst = [x + 2 for x in range(0, 11)]
print(lst)
