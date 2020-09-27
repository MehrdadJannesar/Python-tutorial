# def name(args):
#     Statements

def evenOdd(x):
    if (x % 2 == 0):
        print("Even")
    else:
        print("Odd")

evenOdd(13)

def myFun(x):
    x[0] = 10


lst = [1,20,30,40,50,60]
myFun(lst)
print(lst)

def myFun_2(x):
    x = [20,30,40]
    # x.append()

lst_2 = [10,50,70]
myFun_2(lst_2)
print(lst_2)

def myFun_3(x):
    x = 20

x = 10
myFun_2(x)
print(x)


def swap(x,y):
    temp = x
    x = y
    y = temp

#Driver Code
x = 2
y = 3
swap(x,y)
print(x)
print(y)


def myFun_4(x, y = 50):
    print("x: ", x)
    print("y: ", y)

myFun_4(10,30)


print("\n")

def student(firstname, lastname):
    print(firstname, lastname)

student(firstname = "Mehrdad", lastname = "Jannesar")
student(lastname = "Ahmadi", firstname = "ali")
#
# *args
# **kwargs

# firstname = "Mehrdad"
# {firstname : "Mehrdad"}

def myFun_5(*args):
    for arg in args:
        print(arg)

myFun_5("Hello","Python","Tutorial",2020)


def myFun_6(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" %(key,value))


# Driver Code
myFun_6(firstname = "Mehrdad", lastname = "Jannesar", age=20)



def even_with_return(x):
    if (x % 2 == 0):
        return True
    else:
        return False


if even_with_return(13):
    print("Even")
else:
    print("Odd")


def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3


for value in simpleGeneratorFun():
    print(value)



print("\n")

def cubeFun(y):
    return y*y*y

cube = lambda y: y*y*y

print(cubeFun(2))
print(cube(2))

print("\n")
# filter / map (Function, Seq)

a = [100,2,8,60,5,4,3,31,1,10,11]

filtered = filter(lambda x: x % 2 == 0, a)
print(list(filtered))

maped = map(lambda x: x % 2 == 0, a)
print(list(maped))
print("\n")
a = 1

def f():
    print("Inside f() : ", a)


def g():
    a = 2
    print("inside g() : ", a)

def h():
    global a
    a = 3
    print("Inside h() : ", a)

print("global : ", a)
f()
print("global : ", a)
g()
print("global : ", a)
h()
print("global : ", a)

def creater_adder(x):
    def adder(y):
        return x + y
    return adder

add_fun = creater_adder(15)
print(add_fun(10))

def my_decrator(func):

    def wrapper():
        print("Inside of decorator before calling the func.")
        func()
        print("Inside of decorator after calling the func.")

    return wrapper

@my_decrator
def printname():
    print("Mehrdad")

printname()
