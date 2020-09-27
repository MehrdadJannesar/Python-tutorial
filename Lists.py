lst = []

lst1 = [10,20,40,20,20,40,40]
print(lst1)
print("\n")
lst2 = ["Python", "Tutorial", "World"]
print(lst2)
print("\n")

lst3 = ["Python", 2020, 19.5]
print(lst3)
print("\n")

print(lst2[1])
print("\n")

lst4 = [["Python",2020], ["Tutorial"]]
print(lst4)
print("\n")

print(len(lst1))


list_1 = []
list_1.append(1)
list_1.append(2)
print(list_1)
print("\n")
list_1.append(40)
print(list_1)

for i in range(1,4):
    list_1.append(i)

print("\n")
print(list_1)

list_1.insert(2,33)
list_1.insert(0,"Python")
list_1.insert(3,(2,3))

print("\n")
print(list_1)



list_2 = [1,0,8,2,3,4]

# list_2.extend([2020,"python","tutorial","jannesar"])
# print("\n")
# print(list_2)


# list_2.remove(2)

print(list_2)

list_2.pop()
print(list_2)


List = ["P","Y","T","H","O","N","T","U","R"]
# ---> [include:up to]
print(List[2:5])
print(List[3:])
print(List[:])
print(List[-1])
print(List[-5:-1])
print(List[::-1])

print(List.index("Y"))
