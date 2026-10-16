def greet(name, *, greeting="Hello"):   # greeting MUST be keyword
    return f"{greeting}, {name}!"

greet("Pankaj")                    # "Hello, Pankaj!"
greet("Pankaj", greeting="Hi")     # "Hi, Pankaj!"
try:
    greet("Pankaj", "Hi")              # TypeError — greeting is keyword-only
except TypeError as te:
    message = str(te)
    print(f"TypeError: {message}")
# greet(greeting = "Hello", "Pankaj")     # SyntaxError: positional argument follows keyword argument