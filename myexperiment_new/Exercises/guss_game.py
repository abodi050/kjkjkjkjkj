from random import randint
gnum = randint(0, 2)
print(gnum)
print("welcome to the game\n\n")
print(
    "you will guess a number \nbetween 1 to 100 \nwe have selected for you\n\n"
)
print("hint: WARM! mean yor are close by 10 ")
print("\nlet's start\n")
z = 0
count_num = 0
out = 0
warm = 0
cold = 0
list1 = []
while z == 0:
    cnum = int(input("choose a number : "))
    #print(cnum)
    round_num1 = cnum - gnum
    round_num = abs(round_num1)
    if cnum > 100:
        print("beyond the limits (¬_¬) bi***!!!")
        z = 0
        out += 1
    elif round_num <= 10 and round_num != 0:
        print("WARM!!")
        z = 0
        warm += 1
        if gnum > cnum:
            print("higher -_-\n\n")
        elif gnum < cnum:
            print("lower -_-\n\n")
    elif round_num > 10:
        print("cold!!")
        z = 0
        cold += 1
        if gnum > cnum:
            print("higher -_-\n\n")
        elif gnum < cnum:
            print("lower -_-\n\n")
    elif cnum == gnum:
        print("yey you got it \n＼(^-^)／ \n≧◡≦\n\nGood job\n")
        z = 1
    list1.append(cnum)
    count_num = count_num + 1
print("you took %s tries to get it" % (count_num))
print(
    "from %s \nyou achieve %s for warm \nyou achieve %s for cold\nyou achieve %s for beyond"
    % (count_num, warm, cold, out))
print("\n\nyour numbers are ", list1)
print("see you agine")
#print(list1)
