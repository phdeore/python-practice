
# Function pipeline

from functools import reduce

def pipe(*funcs):
    #pipe(f, g, h)(x) == h(g(f(x)))
    return lambda x: reduce(lambda current_value, func: func(current_value), funcs, x)
    #pass

process = pipe(
    lambda x: x + 1,
    lambda x: x * 2,
    lambda x: x - 3
)
print(process(5))   # ((5+1)*2)-3 = 9

'''
TODO: Understand this thoroughly.

The functools.reduce is exactly the right tool — it threads the accumulated value through each function in sequence, 
and the one-liner is genuinely readable once you know reduce. 
The initializer (x as the third argument to reduce) is the correct way to handle the "starting value" case.

'''