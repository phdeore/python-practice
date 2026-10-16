import sys, time

# List comprehension — builds entire list immediately, uses memory
squares_list = [x**2 for x in range(10_000_000)]   # ~80MB
print(sys.getsizeof(squares_list))

# Generator expression — computes each value on demand
squares_gen = (x**2 for x in range(10_000_000))    # ~200 bytes
print(sys.getsizeof(squares_gen))

# Both work the same way with consumers:
print(time.time())
print(sum(squares_list))   # works
print(time.time())
print(sum(squares_gen))    # also works, but uses almost no memory
print(time.time())

# TODO
# Key rule: if you only need to iterate ONCE, use a generator expression.
# If you need to iterate multiple times, or index into it, use a list.