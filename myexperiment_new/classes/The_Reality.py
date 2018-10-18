class Student:
    def __init__(self, name, ID, section):
        self.name = name
        self.ID = ID
        self.section = section

    def str(self):
     return "Student name: "+self.name+"Student Id: "+self.ID+"Student Section: "+self.section



def function():
    name = input("whats your name:  ")
    ID = input("please write your ID student: ")
    section = int(input("enter your section: "))
    person = Student(name, ID, section)
    person_list.append(person)


person_list = []
x = 0
NumOfStd = int(input("how many Student in a class"))
while x <= NumOfStd-1:
    function()
    x += 1

print(person_list[0])