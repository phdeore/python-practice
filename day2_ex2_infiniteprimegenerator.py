import itertools

'''
My code

def primes():
    nums = [x for x in range(2, N)]
    
    i = 0
    while i < N:
        yield nums[i]
        nums[:] = (x for x in nums if x == nums[i] or x % nums[i] != 0)
        i += 1

Bounded by N = 10000
Ask for the 1300th prime (there are only 1229 primes below 10,000) and it throws IndexError.
Ask is for unbounded sieve.
A true infinite generator must be able to produce the 10,000th prime, the millionth, etc., 
growing its search space as needed rather than pre-allocating a fixed range.

'''

def primes():
    found = []
    candidate = 2
    while True:
        # Only need to test divisibility by primes upto sqrt(candidate)
        if all(candidate % p != 0 for p in found if p * p <= candidate):
            found.append(candidate)
            yield candidate
        candidate += 1


gen = primes()
print(list(itertools.islice(gen, 20)))
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]

'''
TODO: Revise primality test

Breakdown:
all(candidate % p != 0 for p in found if p * p <= candidate)
│   │                  │   │       │
│   │                  │   │       └── only primes p where p² ≤ candidate
│   │                  │   └── list of primes found so far [2, 3, 5, 7, ...]
│   │                  └── loop over those primes
│   └── for each p: candidate is NOT divisible by p
└── True only if EVERY test passes → candidate is prime

Flow in context:
candidate = 2 → no primes in found yet → `all(...)` over empty → True → yield 2
candidate = 3 → test p=2: 3%2≠0 → True → yield 3
candidate = 4 → test p=2: 4%2==0 → False → skip
candidate = 5 → test p=2, p=3 → both pass → yield 5

Explanation for 1st iteration in the loop.

found1 = []
if all(x for x in found1):
    print('all true')
else:
    print('all false')

'''