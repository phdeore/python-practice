from itertools import tee

# A basic generator that can normally only be used once
data_stream = (x * 2 for x in range(3))

# Duplicate into two independent iterators
iter_a, iter_b, iter_c = tee(data_stream, 3)

print(list(iter_a))  # Output: [0, 2, 4]
print(list(iter_b))  # Output: [0, 2, 4] - Still works!
print(list(iter_a))  # Output: [0, 2, 4]
print(list(iter_c))  # Output: [0, 2, 4]