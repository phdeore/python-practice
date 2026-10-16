def add_item(item, items=[]):
    items.append(item)
    return items

items = add_item(1)
items = add_item(2)
items = add_item(3)
items = add_item(1)

print(items)

def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

items = add_item(1)
items = add_item(2)
items = add_item(3)
items = add_item(1)

print(items)