names = ["Alice", "Bob", "Charlie"]
scores = [92, 85, 78]

# enumerate — adds index, replaces Java's for(int i=0; ...)
for i, name in enumerate(names, start=1):
    print(f"{i}. {name}")

# zip — pairs up iterables, stops at shortest
for name, score in zip(names, scores):
    print(f"{name}: {score}")

# zip is lazy in Python 3 — no intermediate list created
# zip_longest from itertools if you need to handle unequal lengths

# map and filter — return lazy iterators, not lists
doubled = list(map(lambda x: x * 2, scores))
print(doubled)
passing = list(filter(lambda x: x >= 85, scores))
print(passing)

# Pythonic preference: comprehensions over map/filter for readability
doubled = [x * 2 for x in scores]
print(doubled)
passing = [x for x in scores if x >= 85]
print(passing)
# map/filter shine when passing an already-named function: map(str, nums)

# TODO: Explore lambda, map/filter and comprehensions