import functools

def memoize(func):
    cache = {}
    cache_stats = {"hits": 0, "misses": 0}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(slow_fib.__name__, slow_fib.__doc__)
        key = args + tuple(sorted(kwargs.items()))  # full signature as key
        print(type(key), key)
        if key in cache:
            cache_stats["hits"] += 1        # cache hit
            return cache[key]

        cache_stats["misses"] += 1          # cache miss
        result = func(*args, **kwargs)
        cache[key] = result
        return result

    def cache_clear():
        cache.clear()
        cache_stats.update({"hits": 0, "misses": 0})

    wrapper.cache_clear = cache_clear
    wrapper.cache_info = lambda: cache_info

    return wrapper

@memoize
def slow_fib(n):
    """Returns nth number from the fibonacci series"""
    if n < 2: return n
    return slow_fib(n-1) + slow_fib(n-2)

print(slow_fib(n=10))

'''
print(slow_fib(10))
print(slow_fib.cache_info())

print(slow_fib(8))
print(slow_fib.cache_info())

print(slow_fib(9))
print(slow_fib.cache_info())

slow_fib.cache_clear()
print(slow_fib.cache_info())

print(slow_fib(9))
print(slow_fib.cache_info())
'''
'''
for i in range(20):
    print(i, slow_fib(i))
'''

'''
TODO: Revise this.
'''