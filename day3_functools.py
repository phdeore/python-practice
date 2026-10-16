import functools

def timer(func):
    @functools.wraps(func)   # preserves func.__name__, __doc__, etc.
    def wrapper(*args, **kwargs):
        import time
        start = time.perf_counter()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.perf_counter()-start:.4f}s")
        return result
    return wrapper

@timer
def slow_add(a, b):
    """Adds two numbers slowly."""
    return a + b

print(slow_add.__name__)   # "slow_add" — WITHOUT @wraps this would print "wrapper"
print(slow_add.__doc__)    # "Adds two numbers slowly." — also preserved

# partial — pre-fill some arguments, get a new callable
double = functools.partial(lambda x, y: x * y, y=2)
print(double(5))   # 10


double_twoargs = functools.partial(lambda x: x * 2)
print(double_twoargs(23))

#print(slow_add(3, 4))