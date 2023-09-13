'''main to handle the entry point and user inputs and will orchestrates the execution flow
 and coordinates interactions between different commponents '''

from game.deck import deal
dollars = ""

print("Let's play Black Jack!!")
input = ("Press 1 to play or 2 to quit")
print(f"You have {dollars} in the bank. How much do you wish to bet: \n")

# Call the deal() function
user_hand = deal(2)
dealer_hand = deal(2)


if __name__ == '__main__':   
    deal()