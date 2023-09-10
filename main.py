import json
# read the contens of the data.json file
with open('data/data.json') as file:
  data = json.load(file)
import banking.player_account
import banking.dealer_account

dollars = ""

print("Let's play Black Jack!!")
print(f"You have {dollars} in the bank. How much do you wish to bet: n/")
