import heapq

def list_merge_inefficient(lists):
    nums = []
    for items in lists:
        for item in items:
            heapq.heappush(nums, item)
    return [heapq.heappop(nums) for i in range(len(nums))]

def k_way_merge(lists):
    heap = []
    for i, lst in enumerate(lists):
        print(i, lst)
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))

    print("heap: ", heap)
    result = []
    while heap:
        val, i, j = heapq.heappop(heap)
        print(val, i, j)
        result.append(val)
        if j + 1 < len(lists[i]):
            heapq.heappush(heap, (lists[i][j+1], i, j+1))
    return result


lists = [
    [1, 4, 7],
    [2, 5, 8],
    [3, 14, 15],
    [],
    [6, 10, 12, 13]
]
print(list_merge_inefficient(lists))   # [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(k_way_merge(lists))   # [1, 2, 3, 4, 5, 6, 7, 8, 9]



'''

TODO: Revise
Given k sorted lists, merge them into a single sorted list efficiently using heapq.
Must also handle: empty lists in the input, lists of different lengths

Hint: push (value, list_index, element_index) tuples into the heap.

'''