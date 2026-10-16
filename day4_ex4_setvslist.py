import timeit

print(f"{'n':<10} | {'list (s)':<10} | {'set (s)':<10} | {'speedup':<12}")
print("-" * 36)

for n in [10, 100, 1000, 10000, 100000]:
    data_list = list(range(n))
    data_set = set(range(n))
    needle = n - 1

    timeit_list = timeit.timeit(lambda: needle in data_list, number=10000)
    timeit_set = timeit.timeit(lambda: needle in data_set, number=10000)
    speedup = timeit_list / timeit_set
    print(f"{n:<10} | {timeit_list:.6f} | {timeit_set:.6f} | {speedup:.2f}x")

