from sys import getsizeof
import timeit

N = 10000

def sum_squares_loop():
    total = 0
    for i in range(N + 1):
        if i % 2 == 0:
            total += i ** 2
    return total

def sum_squares_list():
    return sum([x**2 for x in range(N + 1) if x % 2 == 0])

def sum_squares_gen():
    return sum(x**2 for x in range(N + 1) if x % 2 == 0)

# By wrapping each in a function and passing the function object directly to timeit.timeit(), 
# you avoid the globals=globals() string-eval approach entirely — cleaner and avoids exactly the bug you hit.
timeit_loop = timeit.timeit(sum_squares_loop, number = 1000) 
timeit_list = timeit.timeit(sum_squares_list, number = 1000) 
timeit_gen  = timeit.timeit(sum_squares_gen, number = 1000) 

print(f"for loop: {timeit_loop:.4f} seconds")       # 4.0297 seconds
print(f"list comp: {timeit_list:.4f} seconds")      # 3.6169 seconds. Fastest!
print(f"gen expr: {timeit_gen:.4f} seconds")        # 3.9247 seconds

print("-" * 80)
# Memory efficient generator expression

comp = [i for i in range(10000)]
gen = (i for i in range(10000))

x = getsizeof(comp) 
print("Size for list comprehension = ", x)

y = getsizeof(gen) 
print("Size for generator expression = ", y)

print("-" * 80)
# Difference in execution time

print(timeit.timeit('''list_com = [i for i in range(100) if i % 2 == 0]''', number=1000000))
print(timeit.timeit('''gen_exp = (i for i in range(100) if i % 2 == 0)''', number=1000000))

'''
TODO: Generator expressions are preferred over list comprehensions 
when memory efficiency is critical  or when handling large or infinite datasets.

Why might a generator sometimes beat a list comprehension?
When the consumer (sum() here) can pull values one at a time without ever needing the full collection in memory, 
the generator avoids the cost of allocating and filling an entire list upfront.
At N=100,000 the difference is small; 
it grows dramatically at larger N or when not all elements are consumed (e.g. early-exit search).

For N = 1000000
list comp: 40.3158 seconds
gen expr: 40.3934 seconds

For N = 10000000
list comp: 448.1492 seconds
gen expr: 442.2175 seconds      --> Hence proved.

Feature                 List Comprehension                      Generator Expression
Evaluation              Eager (all items calculated upfront)    Lazy (calculated on demand)
Memory Allocation       High (scales linearly with data size)   Minimal (fixed footprint regardless of data size)
Access Patterns         Supports indexing, slicing, and reuse   Single-use iterable; no indexing/slicing
Execution Speed         Faster for small datasets               Ideal for large/infinite datasets


'''