
import functools
def retry(n, exceptions=(Exception,)):
    """Decorator factory — retries the wrapped function up to n times
    if it raises one of `exceptions`. Re-raises the last exception
    if all attempts fail."""

    def decorator(func):
        count = 0
        last_exception = None
        @functools.wraps(func)
        def factory():
            for count in range(n):
                result = None
                try:
                    result = func()
                except Exception as e:
                    last_exception = e
                if result == None: result = last_exception
                print(result)
            return result
        return factory
    return decorator    

@retry(3, exceptions=(ValueError,))
def flaky():
    import random
    num = random.random()
    print(num)
    if num < 0.7:
        raise ValueError("failed!")
    return "success"

print(flaky())