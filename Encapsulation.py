class Base:
    def __init__(self):

        # Protected member
        self._a = 2

class Child(Base):
    def __init__(self):

        Base.__init__(self)
        print("Calling Protected member")
        print(self._a)


#Driver Code

obj1 = Child()

obj2 = Base()

# print(obj2.a)
print("\n")

class Base:
    def __init__(self):
        self.a = "Python Tutorial"
        self.__c = "Python 2020"


class Child(Base):
    def __init_(self):

        Base.__init__(self)
        print("Calling private member")
        print(self.__c)


#Driver Code

obj1 = Base()
print(obj1.a)
# print(obj1.c)
obj2 = Child()
print(obj2.c)
