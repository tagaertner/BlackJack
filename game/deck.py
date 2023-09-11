import random


# Define ranks and suits of cards
ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
cards =[]

# Create a deck of cards
def deck_cards():
    for rank in ranks:
        for suit in suits:
          cards.append([rank, suit])
          
  #assign number value to face cards
    if "Ace" == 11:
      value = 11
    elif "Jack"== 10 or "Quenn"== 10 or "King"== 10:
      value = 10
    else:
      value = rank 
        
#deck = [(rank, suit) for rank in ranks for suit in suits]
# Shuffle the deck
    random.shuffle(cards)

# Print the shuffled deck
    for card in cards:
        print(f"{card[0]} of {card[1]}")

def deal_cards():

  deal_cards()