
'''
Demonstrate the list-default trap from Concept 2, then fix it.
Show the same conceptual bug appearing with a mutable class attribute used as an instance default:
'''

class ShoppingCart:
    def __init__(self, city = "Pune", items=None):   # same trap, different syntax
        if items is None:
            self.items = []
        else:
            self.items = items
        self.city = city
        

cart1 = ShoppingCart()
cart1.items.append("apple")
cart2 = ShoppingCart("Delhi")
cart2.city = "Bangalore"
#print(cart1, cart1.city, cart1.items)
#print(cart2, cart2.city, cart2.items)   # what do you expect? what do you get? fix it.


class ShoppingCartBuggy:
    def __init__(self, items=[]):   # same shared list for every instance
        self.items = items

buggy_cart1 = ShoppingCartBuggy()
buggy_cart1.items.append("apple")

buggy_cart2 = ShoppingCartBuggy()
print(buggy_cart2.items)   # ['apple'] — cart2 never had anything added to it!