class Person(object):

    #Constructor
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def isEmployee(self):
        return False

class Employee(Person):
    pass
    # def isEmployee(self):
    #     return True

#Driver Code
emp = Person("Python") # An object of person
print(emp.getName(), emp.isEmployee())

emp = Employee("Python_2")
print(emp.getName(), emp.isEmployee())
