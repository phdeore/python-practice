import collections
Card = collections.namedtuple('Card', ['rank', 'suit'])
class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
    def __len__(self):
        return len(self._cards)
    def __getitem__(self, position):
        return self._cards[position]
    
    def __setitem__(self, position, value):
        self._cards[position] = value

beer_card = Card('7', 'diamonds')
print(beer_card)
beer_card == Card('K', 'hearts')
print(beer_card == Card('K', 'hearts')) # Returns False since named tuples are immutable and cannot be changed.

deck = FrenchDeck()
print("deck.ranks:", deck.ranks)


print("Number of cards in deck: ", len(deck))
print("First card in deck: ", deck[0])
print("Last card in deck: ", deck[-1])

print("Some card in deck: ", deck[25])  # 25th card in the deck. Diamonds Ace.

from random import choice
print("Random card from deck: ", choice(deck))
print("Random card from deck: ", choice(deck))

print("--------------------------------")

print("Cards in deck: ", deck._cards)

print(deck[:4])
print(deck[11:14])

print("--------------------------------")

for card in deck:   # doctest: +ELLIPSIS
    print(card)

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    print("Rank value: ", rank_value, ", Items in suit_values:", len(suit_values), ", Suit value: ", suit_values[card.suit])
    print("key:", rank_value * len(suit_values) + suit_values[card.suit])
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key=spades_high):
    print(card) 


