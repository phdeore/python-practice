funcs = [lambda: i for i in range(3)]
print(f() for f in funcs)           # Returns generator object
print([f() for f in funcs])
# Why: closures capture the VARIABLE, not its value at creation time.
# By the time the lambdas are called, the loop has finished and i=2.

funcs = [lambda i=i: i for i in range(3)]       # Force early binding with a default argument
print([f() for f in funcs])