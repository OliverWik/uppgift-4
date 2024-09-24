#skapa en kortlek med hjälp av objektorienterad programmering, använd klasser

import os

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    #vanlig metod i en klass
    def show(self):
        return f"{self.suit} {self.value}"

    def __str__(self):
        return f"{self.suit} {self.value}"
    
    def __repr__(self):
        return f"{self.suit} {self.value}"
    



def create_deck():
    cards = []
    
    suits = ["♠", "♥", "♣", "♦"]
    values = ["Ess", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q" "K"]
    

    for suit in suits:
        for value in values:
            cards.append(Card(suit, value))

    breakpoint
    return cards 

    

os.system("cls")


cards = create_deck()
print(cards)

for cards in cards:
     print(cards)
     
    