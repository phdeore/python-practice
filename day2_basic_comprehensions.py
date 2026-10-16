
'''
Python comprehensions offer a shorter syntax to create new collections 
(lists, dictionaries, sets, or generators) based on existing iterables.
'''

squares = []
for x in range(5):
    squares.append(x**2)

print(squares)

# Comprehension equivalent
squares = [x **2 for x in range(5)]
print(squares)

# With an if condition (Filtering)
even_squares = [ x**2 for x in range(20) if x % 2 == 0]
print(even_squares)

# With an if-else statement (Transformation)
labels = ["Even" if x % 2 == 0 else "Odd" for x in range(10)]
print(labels)

#Flattening a 2D Matrix (Nested Loops)
matrix = [[1,2],[3,4]]

# Without comprehension
for row in matrix:
    for num in row:
        print(num)

# With comprehension
flat = [num for row in matrix for num in row]
print(flat)

# Dictionary Comprehensions
square_dict = {x : x ** 2 for x in range(1, 5)}
print(square_dict)

prices = {'apple': 1.50, 'banana': 0.75, 'mango': 2.50}
expensive_fruits = {k : v for k, v in prices.items() if v > 1.0}
print(expensive_fruits)

#Set Comprehensions
words = ["apple", "Apple", "Kiwi", 'banana']
unique_lengths = {len(w.lower()) for w in words}
print(unique_lengths)