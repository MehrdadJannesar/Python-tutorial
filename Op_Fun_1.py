import operator

a = 4
b = 5

print("The addition of numbers is: ", end="") # +
print(operator.add(a,b))

print("The difference of numbers is: ", end="") # -
print(operator.sub(a,b))

print("The product of numbers is: ", end="") # *
print(operator.mul(a,b))


# truediv
print("The true division of numbers is: ", end="") # /
print(operator.truediv(a,b))

# floordiv
print("The floor division of numbers is: ", end="") # //
print(operator.floordiv(a,b))

# pow
print("The exponentiation of numbers is: ", end="") # **
print(operator.pow(a,b))

# mod
print("The moduls of numbers is: ", end="") # %
print(operator.mod(a,b))
