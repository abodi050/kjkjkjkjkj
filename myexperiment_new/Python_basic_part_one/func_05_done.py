#WE WILL COLLECT DATA FROM USER IN *args and **kwargs STYLE

gen_users = {}


def user_dic(**data1):
    global x
    counter = str(x)
    piar = "person " + counter
    gen_users[piar] = data1
    print(data1)


x = 1

add = True
while add == True:
    name2 = input("please type your name:")
    age2 = int(input("enter your age:"))
    hight2 = int(input("whats your hight:"))
    user_dic(name=name2, age=age2, hight=hight2)
    x += 1

    if name2 == "hello":
        add = False

print(gen_users)
