# Basic Syntax:
#
# try:
#     # code
# except:
#     # code


# def divide(x, y):
#
#     try:
#         result = x // y
#         print("Your answer is : ", result)
#
#     except Exception as e:
#         print(e)
#
#
# divide(3,0)

# Basic Syntax with final:
#
# try:
#     # code
# except:
#     # code
# finally:
#     # code


# try:
#     print("Code Start")
#
#     print(1/0)
# except:
#
#     print("an error !")
#
# finally:
#     print("Python Tutorial!")


# Raise
try:
    raise NameError("Hi there!")
except NameError:
    print("An error!")
    raise
