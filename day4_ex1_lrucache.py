from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        print(f'------- get {key}-------')
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        print(self.cache.items())
        return self.cache[key]

    def put(self, key, val):
        print(f'------- put {key} : {val} -------')
        if key in self.cache:
            self.cache.move_to_end(key, last=True)          # existing key — just promote, no eviction
        else:
            if len(self.cache) == self.capacity:
                self.cache.popitem(last=False)              # only evict when adding a NEW key
        self.cache[key] = val


lru = LRUCache(capacity=3)
lru.put(1, "one")
lru.put(2, "two")
lru.put(3, "three")
lru.get(1)             # "one" — moves 1 to most-recently-used
lru.put(4, "four")     # evicts 2 (least recently used)
lru.get(2)             # -1 — was evicted
lru.get(3)             # "three"
lru.get(4)             # "four"
lru.get(1)
lru.put(1, 'one updated')

'''
TODO: Revise
Implement an LRU (Least Recently Used) cache class without using functools.lru_cache. It should:

Support get(key) → returns value or -1 if not found
Support put(key, value) → adds or updates; evicts LRU item if over capacity
Both operations must be O(1)

Hint: OrderedDict supports move_to_end(key) and popitem(last=False).
'''
