from collections import deque, Counter, defaultdict, OrderedDict, namedtuple

# deque — O(1) at BOTH ends (list is O(n) at left end)
dq = deque([1, 2, 3])
dq.appendleft(0)   # O(1)
dq.append(10)
dq.popleft()       # O(1)
#dq = deque(maxlen=3)   # fixed-size sliding window — auto-evicts oldest
print(dq)

print('-' * 40)
# Counter — dict subclass for counting
words = "the cat sat on the mat the cat tree".split()
c = Counter(words)
print(c)
print(c.most_common(2))    # [('the', 3), ('cat', 2)]
print(c["the"])            # 3
print(c["missing"])        # 0 — never KeyError, unlike plain dict

print('-' * 40)
# defaultdict — auto-creates missing keys
groups = defaultdict(list)
for word in words:
    groups[word[0]].append(word)   # groups first letter → words
print(groups)
print(words)
# No KeyError on missing key — creates [] automatically

print('-' * 40)
# namedtuple — lightweight struct, tuple with named fields
Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
print(p)
print(p.x, p[0])        # 3  (also p[0])
print(p._asdict())   # OrderedDict([('x', 3), ('y', 4)])
