# Both must be generators (use yield). Don't use zip or enumerate inside your implementation.
def my_zip(*iterables):
    iterators = [iter(it) for it in iterables]      # one iterator per input
    while True:
        result = []
        for it in iterators:
            try:
                result.append(next(it))
            except StopIteration:
                return      # any exhausted iterable ends the whole zip
            print(result)
        yield tuple(result)


def my_enumerate(iterable, start=0):
    _iter = iter(iterable)
    while True:
        try:
            item = next(_iter)
            yield start, item
            start += 1
        except StopIteration:
            break

# Tests:
print(list(my_zip([1,2,3], "abc", [True, False, True])))
# [(1, 'a', True), (2, 'b', False), (3, 'c', True)]
print(list(my_zip([1,2,3,4], "abcd", [True, False, True, True])))
print(list(my_zip([1,2,3], "abc", [True, False, True], ['hi', 'there', 'whatsup'])))
print(list(my_zip([1,2,3], "ab", [True, False, True], ['hi', 'there', 'whatsup'])))

print(list(my_enumerate("abc", start=1)))
# [(1, 'a'), (2, 'b'), (3, 'c')]


# TODO: Revise logic