#first (done)


def writting_data():
    global dictionary
    dictionary = {}
    done = "no"
    while done != "YES":
        name = input("write the name: ")
        day = input("write %s's birthday:in day ")
        mounth = input("write %s's birthday:in mounth ")
        year = input("write %s's birthday:in year " % (name))
        dictionary[name] = day, mounth, year
        done = input("are you done :").upper()
    return dictionary

writting_data()
print(dictionary)

#second(in progrees)
#dictt = {"abodi": "12.12", "khalid": "11.11.1111"}

read_file = open("birthday_data.txt", "r")
from ast import literal_eval
python_dict = literal_eval(read_file.read())
python_dict.update(dictionary)
new_file = open("birthday_data.txt", "w")
new_file.write(json.dumps(python_dict))


#third(in progres)
print("Welcome to the birthday dictionary. We know the birthdays of:\n")


def find_names():
	for i in new_file:

	print(new_file[i])