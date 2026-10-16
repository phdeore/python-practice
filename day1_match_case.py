# Value Matching

print(":::Value Matching:::")
def http_status_code(status_code):
    match status_code:
        case 200:
            return "OK"
        case 301 | 302:
            return "Moved Permanently. Or Redirect"
        case 401:
            return "Unauthorized"
        case 403:
            return "Forbidden"
        case 404:
            return "Requested Resource Not Found"
        case 405:
            return "Requested Method Not Allowed"
        case 406:
            return "Requested Resource Not Acceptable"
        case 407:
            return "Requested Proxy Authentication Required"
        case 500:
            return "Internal Server Error"
        case _:
            return f"Unknown HTTP Status Code: {status_code}"

print(http_status_code(200))
print(http_status_code(404))
print(http_status_code(101))

print(":::Sequence Patterns:::")
def describe_list(items):
    match items:
        case []:
            return "An empty list"
        case [x]:
            return f"A list with one item: {x}"
        case [x, y]:
            return f"A list with two items: {x} and {y}"
        case [first, *rest]:
            return f"A list with three items: {first}, {rest}"
        case _:
            return f"A list with {len(items)} items"

lst = [1,2,3,4,5]
print(describe_list(lst))
lst = [1, 2]
print(describe_list(lst))
lst = [1, 2, 3]
print(describe_list(lst))

print(":::Mapping Patterns:::")
def handle_event(event):
    match event:
        case {"type": "click", "x": x, "y": y}:
            return f"click at ({x}, {y})"
        case {"type": "keydown", "key": k}:
            return f"key pressed: {k}"
        case {"type": t}:
            return f"unknown event: {t}"

# Extra keys in the dict are IGNORED (open matching)
# Captured variables (x, y, k) are bound in the case body
print(handle_event({"type": "click", "x": 100, "y": 200}))
print(handle_event({"type": "keydown", "result": "Done", "key": "Enter"}))
print(handle_event({"type": "scroll", "delta": 5}))


print(":::Guard Clauses:::")
def classify_point(point):
    x, y = point
    match point:
        case (0, 0):
            return "origin"
        case (x, 0) if x > 0:
            return f"positive x-axis at {x}"
        case (0, y) if y > 0:
            return f"positive y-axis at {y}"
        case (x, y):
            return f"quadrant point ({x}, {y})"

# 'if' after case = guard clause
# Only matches if pattern AND guard are both true

print(classify_point((0, 0)))
print(classify_point((1, 0)))
print(classify_point((0, 1)))
print(classify_point((-1, 1)))
print(classify_point((1, -1)))
print(classify_point((-1, -1)))
print(classify_point((1, 1)))

print(":::Class Patterns:::")
from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float

def describe(shape):
    match shape:
        case Point(x=0, y=0):
            return "origin"
        case Point(x=x, y=0):
            return f"on x-axis at {x}"
        case Point(x=0, y=y):
            return f"on y-axis at {y}"
        case Point(x=x, y=y):
            return f"point at ({x}, {y})"

# Class patterns check isinstance() AND extract attributes
# Works with dataclasses, namedtuples, any class with __match_args__

print(describe(Point(0, 0)))
print(describe(Point(1, 0)))
print(describe(Point(0, 1)))
print(describe(Point(-1, 1)))
print(describe(Point(1, -1)))
print(describe(Point(-1, -1)))
print(describe(Point(1, 1)))