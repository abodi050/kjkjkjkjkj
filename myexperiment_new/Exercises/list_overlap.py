
def list_overlap(lst1,lst2):
	new_list=[]
	for a in lst1:
		if a in lst2:
			new_list.append(a)
	new_list=set(new_list)
	return new_list
lst1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
lst2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(list_overlap(lst1,lst2))
