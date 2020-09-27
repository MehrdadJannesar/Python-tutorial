# if condition:
#     # Statments - Event

#
# i = 17
# if ( i > 15 ):
#     print("10 is less than 15")
#
# # if condition:
# #     Execute this block
# #     condition is true
# # else:
# #     condition is false
#
# i = 20
# if (i < 15):
#     print("i is smaller than 15")
#     print("I'm in if block")
# else:
#     print("i is greater than 15")
#     print("I'm in else block")
#
#
# # if condition:
# #     if condition:
# #         if condition:
# print("\n")
#
# i = 13
#
# if (i == 13):
#     # First if Statments
#     if (i < 15):
#         print("i is smaller than 15")
#     # Sec if Statments
#     if (i < 12):
#         print("i is smaller than 12 too")
#     else:
#         print("else block")
#
#
#
# # if condition:
# #     # Statments
# # elif condition:
# #     # Statments
# # else:
# #     # Statments
#
# print("\n")
# i = 20
# if (i == 10): # --> false
#     print( "i is 10" )
# elif (i == 15): # --> false
#     print( "i is 15" )
# elif (i == 20): # --> true
#     print( "i is 20 ")
# else:
#     print("Not Found!")
#
#
# # if condition : Statments
# i = 10
# if i < 15: print("i is less than 15")


# for var in iterable:
#     # Statments


l = ["Python","Tutorial","2020"]

for item in l:
    print(item)

print("\n")

s = "Python"
for item in s:
    print(item)

t = ("Python","Tutorial","2020")
for item in t:
    print(item)


# d = dict()
#
# d['xyz'] = 123
# d['abc'] = 345
# for item in d:
#     print("%s %d" %(item, d[item]))
# #
# print("\n")
# for letter in "Python":
#     if letter == 'P' or letter == 'y':
#         continue
#     print("Current Letter :", letter)
#
#
#         # include , upto
# # range(start, stop, step)
#
# for i in range(10):
#     print(i, end = " ")
#
# print("\n")
# for i in range(0,10,2):
#     print(i, end = " ")
#
# print("\n")
# for i in range(1,4):
#     print(i)
#     break
# else:
#     print("Done!")


# while expression:
#     Statments

# count = 0
# while (count < 3):
#     count = count + 1
#     print("Hello All!")
#
# a = [1,2,3,4]
# while a:
#     print(a.pop())
#
# count = 0
# while (count<5): count += 1; print("Hello All!")
#
# print("\n")
# i = 0
# a = "Python"
#
# while i < len(a):
#     if a[i] == 'P' or a[i] == 'o':
#         i+=1
#         continue
#     print('Current Letter : ', a[i])
#     i+=1
