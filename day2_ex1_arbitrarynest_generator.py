
def flatten(lst):
    for x in lst:
        if isinstance(x, (list, tuple, set)):
            print('inside list, tuple or set')
            yield from flatten(x)
        else:
            print(x)
            yield x


data = [1, [2, 3], [4, [5, [6, 7]]], 8]
print(list(flatten(data)))   # [1, 2, 3, 4, 5, 6, 7, 8]

print('--------------------------------')

# Must also handle non-list iterables except strings:
data2 = [1, (2, 3), {4, 5}]
print(list(flatten(data2)))  # [1, 2, 3, 4, 5]  (order of set elements may vary)

print('--------------------------------')

# Strings must NOT be flattened (they're iterable but should be leaf values):
data3 = ["hello", ["world"]]
print(list(flatten(data3)))  # ["hello", "world"]


'''
TODO: Flattening using yield
Use of type() instead of isinstance() is a problem. 
It breaks for subclasses i.e. custom class inheriting from list.

'''