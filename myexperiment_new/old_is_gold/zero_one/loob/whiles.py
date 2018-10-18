a = [1, 1, 2, 3, 5, 8, 13, 4, 34, 55, 89]
x = 0
num_list =len(a)
z=0
new_list=[]
while z < num_list:
    #x+=1
    if a[x] <= 5:
        print(a[x])
	elmint = a[x]
	new_list.append(elmint)
    z+=1
    x += 1
print(new_list)