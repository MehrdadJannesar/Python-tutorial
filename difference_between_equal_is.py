list1 = []
list2 = []
list3 = list1

if (list1 == list2):
    print("True")
else:
    print("False")

if (list1 is list2):
    print("True")
else:
    print("False")

if (list1 is list3):
    print("True")
else:
    print("False")


print(id(list1))
print(id(list2))
print(id(list3))
