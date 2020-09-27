from datetime import date

class Person:
    # Instance Method
    def __init__(self, name , age):
        self.name = name
        self.age = age
    # Instance Method
    def show(self):
        print("name is " + self.name + "and age is " + str(self.age))
    # Class Method
    @classmethod
    def fromBrithYear(cls, name , year):
        return cls(name, date.today().year - year )
    # Static Method
    @staticmethod
    def isAdult(age):
        return age > 18


p1 = Person.fromBrithYear("Mehrdad", 1991)
print(p1)
print(p1.name)

print(Person.isAdult(17))



# p1 = Person("Mehrdad", 29)
# print(Person.show())
