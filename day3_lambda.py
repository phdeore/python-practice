# Regular Function
def square(x):
    return x * x

# Equivalent Lambda Function
square_lambda = lambda x: x * x

print(square(5))         # Output: 25
print(square_lambda(5))  # Output: 25

# Using with filter()
numbers = [1, 2, 3, 4, 5, 6]
# Keep only the even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens) # Output: [2, 4, 6]

# Using with map()
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x : x **2, numbers))
print(squared)

# Using with sorted()
pairs = [(1, 'one'), (2, 'two'), (3, 'three')]
# Sort based on the string word instead of the number
pairs.sort(key=lambda item: item[1])
print(pairs)


check_num = lambda x : "Even" if x % 2 == 0 else "Odd"
print(check_num(7))

get_result = lambda score: "Super Distinction!!" if 85 <= score <= 100 else ("Distinction!" if 65 <= score < 85 else "Pass" )
print(get_result(60))
print(get_result(75))
print(get_result(90))

'''
TODO: 
- Anonymous (i.e. no explicit name identifier).
- Contains single expression; not loops, multiple lines or complex statements. Best for short, quick, one-off operations
- Designed to be thrown away or used as arguments for higher-order functions.
- Doesn't use return
'''