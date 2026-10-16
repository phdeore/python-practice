import itertools

# chain — flatten multiple iterables into one
list(itertools.chain([1,2], [3,4], [5]))       # [1, 2, 3, 4, 5]

# islice — lazy slice of any iterator (no [start:stop] on generators)
gen = (x**2 for x in range(1_000_000))
first_five = list(itertools.islice(gen, 5))    # [0, 1, 4, 9, 16]

# groupby — group CONSECUTIVE elements by a key (must be sorted first!)
data = [{"dept":"eng","name":"Alice"},{"dept":"eng","name":"Bob"},{"dept":"hr","name":"Carol"}]
for dept, members in itertools.groupby(data, key=lambda d: d["dept"]):
    print(dept, list(members))

# product — cartesian product (nested loops as one iterator)
for suit, rank in itertools.product("♠♥♦♣", range(2,15)):
    pass   # 52 combinations

# tee — split one iterator into N independent copies
gen = (x**2 for x in range(10))
a, b = itertools.tee(gen, 2)   # WARNING: memory cost if they diverge
print(a, b)

l1 = [1,2]
l2 = [3,5]
l3 = [7]
lst = list(itertools.chain(l1, l2, l3))
print(lst)
print(list(itertools.islice(lst, 2)))