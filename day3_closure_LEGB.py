def make_counter():
    count = 0                 # enclosing scope
    def increment():
        nonlocal count      # without this, count += 1 would raise UnboundLocalError
                            # UnboundLocalError: cannot access local variable 'count' where it is not associated with a value
        # count = 5         # With local assignment, it will always return 6 irrespective of invocation count.
        count += 1
        return count
    return increment

counter = make_counter()
print(counter())   # 1
print(counter())   # 2
print(counter())   # 3 — count persisted between calls, captured in the closure


'''
TODO: Revise this.

Python treats variables differently depending on whether you are mutating an object in place 
(like a dictionary) or reassigning a variable name (like an integer or string) inside a nested function.

def outer():
    count = 0
    def inner():
        # ❌ Raises UnboundLocalError!
        # Python thinks 'count' is local because of the += assignment
        count += 1 
    return inner

When you use code like count += 1 inside a inner function, Python sees the assignment operator (=). 
It automatically assumes count is a local variable to that specific nested function.
When the function runs, it tries to read count to add 1 to it, 
but it hasn't been defined inside that inner scope yet, triggering the UnboundLocalError.

------------------------------------

def outer():
    stats = {"hits": 0}
    def inner():
        #  Works perfectly!
        # Python looks up 'stats' in the outer scope and modifies its keys
        stats["hits"] += 1 
    return inner

When you modify a dictionary inside a closure using stats["hits"] += 1, 
you are not reassigning the variable name stats. 
You are looking up the existing stats object in the outer scope and mutating its internal contents.
Because Python does not see stats = ... inside the inner function, it doesn't assume stats is local, 
and looks it up in the parent closure perfectly fine.
'''