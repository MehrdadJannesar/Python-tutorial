import operator

# li = [1,5,6,7,8]
#
# print("The original list is: ", end="")
#
# for i in range(0, len(li)):
#     print(li[i], end = " ")
#
# print("\r")
# operator.setitem(li,3,3)
#
# print("The modified list after setitem() is : ", end="")
# for i in range(0,len(li)):
#     print(li[i], end = " ")
#
# print("\r")
#
# operator.delitem(li, 1)
#
# print("The modified list after delitem is : ", end="")
#
# for i in range(0,len(li)):
#     print(li[i], end=" ")
#
# print("\r")
#
# print("The 4th element of list is : ", end="")
# print(operator.getitem(li, 3))


#################################################

li = [1, 5, 6, 7, 8]

print("The original list is: ", end="")

for i in range(0, len(li)):
    print(li[i], end = " ")

print("\r")
# [include:up to]
operator.setitem(li, slice(1,4), [2,3,4])

print("The modified list after setitem() is : ", end = "")
for i in range(0, len(li)):
    print(li[i], end = " ")

print("\r")
