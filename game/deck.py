import random


# Define ranks and suits
ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
cards =[]

# Create a deck of cards
for rank in ranks:
  for suit in suits:
    cards.append([rank, suit])

 # Assign number value to cards
def get_card_vaule(rank, current_total):
  if rank == "Ace":
    #if adding to 11 does not bust, treat as 11 else treat as 1
      return 11 if current_total + 11 <= 21 else 1 
  elif rank in ["Jack", "Queen", "King"]:
      return 10
  else:
      return int(rank)
    
# Shuffle the deck
random.shuffle(cards)

#dealing the cards
def deal(number):
  dealt_cards =[]
  for card_index in range(number):
    if len(cards) > 0:
      dealt_card = cards.pop()
      dealt_cards.append(dealt_card)
    else:
      print("no more cards in the deck")
  return dealt_cards

# Deal 2 cards
user_hand = deal(2)
dealer_hand = deal(2)

# Print the hands the loop iterates over each card in both hands
print("User's hand:")
user_hand_total = 0
for card in user_hand:
  rank = card[0]
  value = get_card_vaule(rank, user_hand_total)
  user_hand_total += value 
  print(f"{card[0]} of {card[1]}")

print(f"Total vaule: {user_hand_total}")

#dealer's hand 
print("\nDealer's hand:")
dealer_hand_total = 0
print("This card face down")
for card in dealer_hand[1:]: # used the slice method, iterate over each card and exclued the first card
  print(f"{card[0]} of {card[1]}")

