# What a for loop ACTUALLY does under the hood:
def demo_iterate(collection):
    for item in collection:
        process(item)

# Is exactly equivalent to:
def demo_iterate_exp(collection):
    _iter = iter(collection)        # calls collection.__iter__()
    while True:
        try:
            item = next(_iter)      # calls _iter.__next__()
            process(item)
        except StopIteration:
            break

def process(item):
    print(item)

collection = [1, 2, 3, 4]
#demo_iterate(collection)
#demo_iterate_exp(collection)


# Proof — manually walk a list:
nums = [10, 20, 30]
it = iter(nums)

print(next(it))   # 10
print(next(it))   # 20
print(next(it))   # 30
print(next(it))   # StopIteration — the loop would stop here