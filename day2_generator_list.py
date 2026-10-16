import tracemalloc

tracemalloc.start()

N = 100000000

# List — allocates ALL at once
squares = [x**2 for x in range(N)]
# Memory: O(N)

# Generator — one value at a time
#squares = (x**2 for x in range(N))
# Memory: O(1) — always ~200 bytes

# Both usable the same way:
#total = sum(squares)
# But generator can only be iterated ONCE

# 2. Get current and peak memory usage
current, peak = tracemalloc.get_traced_memory()

print(f"Current memory usage: {current / 1024 / 1024:.2f} MB")
print(f"Peak memory usage:    {peak / 1024 / 1024:.2f} MB")

# 3. Stop tracking
tracemalloc.stop()

#print(total)