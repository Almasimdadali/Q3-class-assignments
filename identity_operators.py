a = [10, 20, 30]
b = a
c = [10, 20, 30]
print(a is b)      # True (Same object)
print(a is c)      # False (Different objects)
print(a is not c)  # True
