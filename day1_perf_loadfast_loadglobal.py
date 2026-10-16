# In a hot inner loop, pull globals into locals before the loop
import math
import dis
import timeit

points = [(1, 2)]
def slow_trig(points):
    return [math.sin(x) * math.cos(y) for x, y in points]

def fast_trig(points):
    sin, cos = math.sin, math.cos   # LOAD_GLOBAL once, then LOAD_FAST each iteration
    return [sin(x) * cos(y) for x, y in points]

dis.dis(slow_trig)
print('*' * 40)
dis.dis(fast_trig)

def slow_trig1(points):
    return [math.sin(x) * math.cos(y) for x, y in points]

def fast_trig1(points):
    sin, cos = math.sin, math.cos   # LOAD_GLOBAL once, then LOAD_FAST each iteration
    return [sin(x) * cos(y) for x, y in points]

timeit_slow = timeit.timeit(lambda: slow_trig1(points), number=1000)
timeit_fast = timeit.timeit(lambda: fast_trig1(points), number=1000)
print(f"slow_trig1: {timeit_slow:.6f}s")
print(f"fast_trig1: {timeit_fast:.6f}s")

'''
TODO: dis module for the analysis of CPython bytecode by disassembling it.

points (size)   Result
1               ~same (noise)
                slow_trig1: 0.000246s  (wins ~3%)
                fast_trig1: 0.000254s

5              fast_trig1 can be slow_trig1.
               slow_trig1: 0.000564s
               fast_trig1: 0.000744s

100+            fast starts winning (~7~10%)
                slow_trig1: 0.007916s
                fast_trig1: 0.006615s (wins ~10%)

The optimization saves work per loop iteration by avoiding repeated math.sin / math.cos lookups. 
With one iteration, that saving is tiny, while fast_trig1 still pays extra setup cost:
sin, cos = math.sin, math.cos   # runs every call

slow inner loop:  LOAD_GLOBAL math → LOAD_METHOD sin/cos  (each iteration)
fast inner loop:  LOAD_DEREF sin/cos                     (closure overhead)

Closures can cost more than cached global lookups when the loop is short.
Takeaway: This optimization matters in a hot inner loop with many iterations, 
ideally a plain for loop — not a one-item list comprehension benchmarked at the function level.

Try points = [(1, 2)] * 100

'''
