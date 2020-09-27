# class Name:
#     Statement 1
#     Statement 2
#     .
#     .
#     .
#     Statement n
#
# class Name(object):
#     Statement 1
#     Statement 2
#     .
#     .
#     .
#     Statement n


# class Dog:
#
#     # Attribute
#     attr1 = "mamal"
#     attr2 = "dog"
#
#     # A sample Method
#     def fun(self):
#
#         print("I'm a ", self.attr1)
#         print("I'm a ", self.attr2)
#
# # Driver code
#
# Rodger = Dog()
#
# print(Rodger.attr1)
# print(Rodger.attr2)
#
# Rodger.fun()



class Person:
    # init Constructor
    def __init__(self,name):
        self.name = name

    # Sample Method
    def say_hi(self):
        print("Hello, my name is ", self.name)

p = Person("Mehrdad")
p.say_hi()



class Dog:

    # Class Variable
    animal = "dog"

    def __init__(self, breed, color):

        # Instance Variable
        self.breed = breed
        self.color = color
# Driver code

Rodger = Dog("Pug", "Brown")
Buzo =  Dog("Bulldog", "Black")

print("Rodger Details: ")
print("Rodger is a", Rodger.animal)
print("Breed: ", Rodger.breed)
print("Color: ", Rodger.color)

print("\nBuzo Details")
print("Buzo is a", Buzo.animal)
print("Breed: ", Buzo.breed)
print("Color: ", Buzo.color)

print("\nAccessing class Variable using class name")
print(Dog.animal)


class Dog_2:

    animal = "dog"

    def __init__(self, breed):
        self.breed = breed

    # Adds an Instance Variable
    def setColor(self, color):
        self.color = color

    # Retrieves Instance Variable
    def getColor(self):
        return self.color
print("\n")
#Driver code
Rodger = Dog_2("Pug")
Rodger.setColor("Brown")
print(Rodger.getColor())


class Employee:

    def __init__(self):
        print("Employee created!")

    # Deleting
    def __del__(self):
        print("Destructor called, Employee deleted!")


obj = Employee()
