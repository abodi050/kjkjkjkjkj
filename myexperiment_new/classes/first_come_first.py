class Person:
    def __init__(self, name, age, car):
        self.name = name
        self.age = age
        self.car = car
	
    def __setUniversity__(self, kfupm):
        self.kfupm = kfupm

name = None
age = None
car = None
person_1 = Person("abdullah", age, car)
person_2 = Person("ali", age, car)
##Person_3 = Person("hello")
print(person_1.name)
print(person_2.name)
person_1.name = "khalid"
print(person_1.name)
#print(person_3.kfupm)
person_1.__setUniversity__("kfupm")
print(person_1.kfupm)