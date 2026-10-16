import sys

# print without a new line
print("Hello World!", end = " ")
print("This is Paul!", end = "\n")
print("What is your name?")

# multiple print statements with semicolon
print("Hello"); print("How are you?");

print(sys.version)

if 5 > 2:
 print("Five is greater than two!")            # At least 1 space is required.
if 5 > 2:
        print("Five is greater than two!") 


x = y = z = "Hello World"
print(x, y, z)

# legal variable names
myvar = "John"
my_var = "John"         # snake case
_my_var = "John"
myVar = "John"          # Camel Case
MYVAR = "John"
myvar2 = "John"
MyVariableName = "John" # Pascal Case

try:
    x = 5
    y = "John"
    print(x + y)
except:
    print("Unsupported operand types")

# variable scope global vs local
# If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. 
# The global variable with the same name will remain as it was, global and with the original value.
x = "awesome"
def myfunc():
  x = "fantastic"
  print("Python is " + x)
myfunc()
print("Python is " + x)

def myfuncglobal():
    global x
    x = "fantastic"
    print("Python is " + x)
myfuncglobal()
print("Python is " + x)
