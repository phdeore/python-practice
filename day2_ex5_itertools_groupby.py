import itertools

logs = [
    {"level": "INFO",    "msg": "Server started"},
    {"level": "INFO",    "msg": "Request received"},
    {"level": "WARNING", "msg": "Slow query detected"},
    {"level": "ERROR",   "msg": "DB connection failed"},
    {"level": "ERROR",   "msg": "Retry failed"},
    {"level": "INFO",    "msg": "Recovered"},
]

LEVEL_ORDER = {"INFO": 0, "ERROR": 1, "WARNING": 2}
logs_sorted = sorted(logs, key=lambda log: LEVEL_ORDER[log["level"]])

target_dict = {}

'''
-- My code --

for level, msg in itertools.groupby(logs_sorted, key=lambda d: d["level"]):
    _iter = iter(msg)
    count = 0
    child_dict = {}
    messages = []
    while True:
        try:
            items = next(_iter)      # calls _iter.__next__()
            messages.append(items.get("msg"))
            count += 1
        except StopIteration:
            break

    child_dict['count'] = count
    child_dict['messages'] = messages
    target_dict[level] = child_dict
'''

# TODO: Revise
# Production code
for level, group in itertools.groupby(logs_sorted, key=lambda d: d["level"]):
    messages = [item["msg"] for item in group]
    target_dict[level] = {"count" : len(messages), "messages": messages}

print(target_dict)