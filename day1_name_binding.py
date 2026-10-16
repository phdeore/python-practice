a = [1, 2, 3]
b = a          # b and a point to the SAME list
b.append(4)
print(a)       # [1, 2, 3, 4]  ← a changed!
print(b)       # [1, 2, 3, 4]
print(id(a))
print(id(b))
