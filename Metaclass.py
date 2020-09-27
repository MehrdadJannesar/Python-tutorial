# Dynamic Object

# def choose_class(name):
#     if name == 'foo':
#         class Foo():
#             pass
#         return Foo
#     else:
#         class Bar():
#             pass
#         return Bar
#
# Myclass = choose_class('foo')
# print(Myclass)
# print(Myclass())
#
# print(type(2))
# print(type(int))

# class A(type):
#     pass
#
# type(
#
# .name ---> name Class
# .bases ---> parent
# .dict ---> attribute
#
#
# )

class A:

    def show(self):
        print("Hello World!")

class B(A):
    pass


def show():
    print("Hello World!")

ab = B()
ab.show()
# ac = A()
# ac.show()

b = type("B", (A,),{'show': show})
b.show()


# 1. __new__(cls)
# 2. __init__(self)
# 3. __call__(cls)


class C:

    def __init__(self):
        print("Init")


    def __call__(cls):
        print("call")



print("\n")

c = C()
c()
