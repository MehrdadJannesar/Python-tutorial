# print(any([False,False,False,True]))
#
# print(all([True,False,True]))

list1 = []
list2 = []

for i in range(1,11):
    list1.append(4*i)

for i in range(0,10):
    list2.append(list1[i] % 5 == 0)

# print('see whether at least one number is divisible by 5 in list 1 =>')
# print(any(list2))

print(all(list2))


# print(list1, list2)
