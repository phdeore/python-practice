x = "Hello World"	                    # str	
x = 20                                  # int	
x = 20.5	                            # float	
x = 1j	                                # complex	
x = ["apple", "banana", "cherry"]	    # list	
x = ("apple", "banana", "cherry")	    # tuple	
x = range(6)	                        # range	
x = {"name" : "John", "age" : 36}	    # dict	
x = {"apple", "banana", "cherry"}	    # set	
x = frozenset({"apple", "banana", "cherry"})	# frozenset	
x = True	                            # bool	
x = b"Hello"	                        # bytes	
x = bytearray(5)	                    # bytearray	
x = memoryview(bytes(5))	            # memoryview	
x = None	                            # NoneType

# Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
x = 1
y = 35656222554887711
z = -3255522

# Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
x = 1.10
y = 1.0
z = -35.59

# Float can also be scientific numbers with an "e" to indicate the power of 10.
x = 35e3
y = 12E4
z = -87.7e100

# Complex numbers are written with a "j" as the imaginary part.
x = 3+5j
y = 5j
z = -5j

# type conversion
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

'''
import random
for i in range(10):
    print(random.randrange(1, 10))
''' 

# multiline strings
a = """Hi there!
What's up?"""
print(a)

x = "abcdefghi"
# positive indexing
print(x[2:5])
print(x[:5])
print(x[5:])
# negative indexing
print(x[-1:])
print(x[-5:-2])

print(x.upper())

y = "  hi  there  "
print(y.strip().split())
print(y.replace('e', 'a'))

txt = "Hello World"
txt = txt.replace('H', 'J')
print(y+txt)

age = 47
print(f"I'm {age} years old.")