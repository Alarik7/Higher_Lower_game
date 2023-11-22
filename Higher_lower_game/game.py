from art import logo,vs
from game_data import data
#from replit import clear
import random

print(logo)

account_a = random.choice(data)
account_b = random.choice(data)
if account_a == account_b:
    account_b = random.choice(data)

def fun_account_a(account_a):
  account_name_a = account_a["name"]
  account_description_a = account_a["description"]
  account_country_a = account_a["country"]
  print(f"Compare A: {account_name_a}, a {account_description_a}, from {account_country_a}")

def fun_account_b(account_b):
  account_name_b = account_b["name"]
  account_description_b = account_b["description"]
  account_country_b = account_b["country"]
  print(f"Against B: {account_name_b}, a {account_description_b}, from {account_country_b}")


fun_account_a(account_a)
print(vs)
fun_account_b(account_b)


score = 0
answer = True


while answer == True:
  user_folllowers = input("Who has more followers? Type 'A' or 'B': ")
  if user_folllowers == 'A':
    if account_a["follower_count"] > account_b["follower_count"]:
      score += 1
      answer = True
      #clear()
      print(logo)
      print(f"You're right! Current score: {score}.")
      fun_account_a(account_b)
      print(vs)
      account_b = random.choice(data)
      fun_account_b(account_b)
      
    else:
      print(f"Sorry that's wrong. Final score: {score}")
      answer = False
      break
  if user_folllowers == 'B':
    if account_b["follower_count"] > account_a["follower_count"]:
      score += 1
      answer = True
      #clear()
      print(logo)
      print(f"You're right! Current score: {score}.")
      fun_account_a(account_b)
      print(vs)
      account_b = random.choice(data)
      fun_account_b(account_b)
    else:
      print(f"Sorry that's wrong. Final score: {score}")
      answer = False
      break
    
      