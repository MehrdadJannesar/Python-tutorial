#Single Inheritance
#Base Class
class Parent(object):
    def func1(self):
        print("This Function is in Parent!")

class Child(Parent):
    def func2(self):
        print("This Function is in Child!")

#Driver's code

obj = Child()
obj.func1()
obj.func2()
print("\n")
#Multiple Inheritance
#Base class 1
class Mother:
    mothername = ""
    def mother(self):
        print(self.mothername)

# Base class 2
class Father:
    fathername = ""
    def father(self):
        print(self.fathername)


class Son(Mother,Father):
    def parents(self):
        print("Father : ", self.fathername)
        print("Mother : ", self.mothername)


#Driver code
s1 = Son()
s1.fathername = "Hassan"
s1.mothername = "Mina"
s1.father()
s1.mother()
s1.parents()

print("\n")
#Multilevel Inheritance

#Base Class
class Grandfather:
    grandfathername = ""
    def grandfather(self):
        print(self.grandfathername)

#Intermediate Class
class Father(Grandfather):
    fathername = ""
    def father(self):
        print(self.fathername)

#Child Class
class Son(Father):
    def parent(self):
        print("Grandfather :", self.grandfathername)
        print("Father :", self.fathername)

# Driver Code
s1 = Son()
s1.grandfathername = "Ashkan"
s1.fathername = "Daryosh"
s1.parent()

print("\n")

# Hierarchical Inheritance
# Base Class
class Parent:
    def func1(self):
        print("This Function is in parent class!")

#Child Class 1
class Child1(Parent):
    def func2(self):
        print("This Function is in child class 1 !")

#Child class 2
class Child2(Parent):
    def func3(self):
        print("This Function is in child class 2 !")

#Driver code
obj1 = Child1()
obj2 = Child2()
obj1.func1()
obj1.func2()
obj2.func1()
obj2.func3()
