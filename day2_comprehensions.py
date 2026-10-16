# List comprehension — single pass, C-level loop internally
squares = [x**2 for x in range(1000)]

# Dict comprehension
word_len = {word: len(word) for word in ["apple", "fig", "mango"]}
# {'apple': 5, 'fig': 3, 'mango': 5}
print(word_len)

# Set comprehension — automatic deduplication
unique_lengths = {len(word) for word in ["apple", "fig", "mango", "grape"]}
print(unique_lengths)
# {3, 5}

non_unique_lengths = (len(word) for word in ["apple", "fig", "mango", "grape"])
print("generator1: ", next(non_unique_lengths))
print("generator2: ", next(non_unique_lengths))
print("generator3: ", next(non_unique_lengths))

# Nested comprehension — matrix transpose
matrix = [[1,2,3],[4,5,6],[7,8,9]]
transposed = [[row[i] for row in matrix] for i in range(3)]
# Read inside-out: for each i, for each row, take row[i]
print(transposed)

# Filtering with condition
evens = [x for x in range(20) if x % 2 == 0]
print(evens)

odds = [x for x in range(20) if x % 2 != 0]
print(odds)

