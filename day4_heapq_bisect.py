import heapq, bisect

# heapq — min-heap on top of a plain list
# NOT a class — just functions operating on a list
nums = [5, 1, 8, 2, 9, 3]

heapq.heapify(nums)           # O(n) — converts list to heap in place
heapq.heappush(nums, 4)       # O(log n)
print(nums)
heapq.heappop(nums)           # O(log n) — always pops MINIMUM
heapq.nsmallest(3, nums)      # [1, 2, 3] — O(n log k)
heapq.nlargest(3, nums)       # [9, 8, 5] — O(n log k)
print(nums)

print('-' * 40)
# Max-heap trick — negate values
heapq.heappush(nums, -10)     # push negative to simulate max-heap

# bisect — binary search on a sorted list
# Maintains sorted order without full re-sort
a = [1, 3, 5, 7, 9]
bisect.bisect_left(a, 5)      # 2 — index where 5 belongs (left of existing)
bisect.bisect_right(a, 5)     # 3 — index after existing 5s
bisect.insort(a, 4)           # inserts 4 in sorted position — O(n) for the shift