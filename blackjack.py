import random

class Card:
    SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    RANKS = {
        '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, 
        '7': 7, '8': 8, '9': 9, '10': 10, 
        'J': 10, 'Q': 10, 'K': 10, 'A': 11
    }

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = self.RANKS[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self, num_decks=1):
        self.num_decks = num_decks
        self.cards = []
        self.build()

    def build(self):
        self.cards = [
            Card(rank, suit) 
            for _ in range(self.num_decks)
            for suit in Card.SUITS 
            for rank in Card.RANKS.keys()
        ]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        if len(self.cards) == 0:
            self.build() # Reshuffle if empty
        return self.cards.pop()

class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        value = 0
        aces = 0
        
        for card in self.cards:
            value += card.value
            if card.rank == 'A':
                aces += 1
                
        # Adjust for Aces if total exceeds 21
        while value > 21 and aces > 0:
            value -= 10
            aces -= 1
            
        return value

    def is_blackjack(self):
        return len(self.cards) == 2 and self.get_value() == 21

    def is_bust(self):
        return self.get_value() > 21

    def __str__(self):
        return ", ".join([str(card) for card in self.cards])