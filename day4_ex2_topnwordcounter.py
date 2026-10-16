import re
from collections import Counter, defaultdict

def top_n_words_counter(text, n):
    words = re.findall(r"[a-z']+", text.lower())
    return(Counter(words).most_common(n))

def top_n_words_dict(text, n):
    words_count = {}
    words = re.findall(r"[a-z']+", text.lower())
    for word in words:
        if word in words_count:
            words_count[word] += 1
        else:
            words_count[word] = 1
    
    sorted_words_count = list(sorted(words_count.items(), key=lambda item: -item[1]))
    return sorted_words_count[:n]

def top_n_words_defaultdict(text, n):
    words_count = defaultdict(int)
    words = re.findall(r"[a-z']+", text.lower())
    for word in words:
        words_count[word] += 1
    
    sorted_words_count = sorted(words_count.items(), key=lambda item: -item[1])
    return sorted_words_count[:n]



text = """To be or not to be that is the question don"t don"t don"t don"t
          Whether tis nobler in the mind to suffer"""
print(top_n_words_counter(text, 3))   # [('to', 3), ('be', 2), ('the', 2)]  (order of ties may vary)
print(top_n_words_dict(text, 3))   # [('to', 3), ('be', 2), ('the', 2)]  (order of ties may vary)
print(top_n_words_defaultdict(text, 3))   # [('to', 3), ('be', 2), ('the', 2)]  (order of ties may vary)

'''
Then compare this approach to doing it with a plain dict + defaultdict — 
show all three implementations, time them with timeit (correctly this time) on a large text.
'''