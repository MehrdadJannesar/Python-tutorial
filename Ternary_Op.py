# [on_true] if [expression] else [on_false]

# a, b = 10, 20

# min = a if a < b else b
#
# print(min)

# Use tuple for selecting an item
# if (test is false, if test is true) [test]
# print((b,a) [a<b])

# Use dictionary for selecting an item
# print({True:a, False:b} [a<b])


# lambda
# print((lambda: b, lambda: a) [a < b]())

# print("Both a and b are equal" if a==b else "a is greater than b" if a > b else "b is greater than a" )

# and - or
# [expression] and [on_true] or [on_false]
a, b = 30, 20
min = a < b and a or b
print(min)
