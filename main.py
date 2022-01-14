from random import choice
from art import *
from game_data import data
from os import system, name

current_score = 0
winning = True

def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def you_lose(score):
  print(f"{logo}\n Sorry, that's wrong. Final score: {score}")
  if input("Would you like to play again? (Type 'y' or 'n')") == 'y':
    higher_lower()
  else:
    return "Thanks for playing!"
    

def get_comp():
  comp = choice(data)
  return {"name": comp["name"],
          "followers": comp["follower_count"],
          "description": comp["description"],
          "country": comp["country"]
          }

def most_followers(compA, compB):
  if compA["followers"] > compB["followers"]:
    return "A"
  else:
    return "B"

# print(data.index(compA))
def higher_lower(comp={}, score=0):
  if comp == {}:
    compA = get_comp()
    compA_name = compA["name"]
    compA_desc = compA["description"]
    compA_country = compA["country"]
  else:
    compA = comp
    compA_name = compA["name"]
    compA_desc = compA["description"]
    compA_country = compA["country"]
  compB = get_comp()
  while compB == compA:
    compB = get_comp()
  compB_name = compB["name"]
  compB_desc = compB["description"]
  compB_country = compB["country"]
  
  if score == 0:
    print(f"{logo}\nCompare A: {compA_name}, {compA_desc}, {compA_country}\n{vs}\nCompare B: {compB_name}, {compB_desc}, {compB_country}")
  else:
    print(f"{logo}\nYou're right! Current score: {score}\nCompare A: {compA_name}, {compA_desc}, {compA_country}\n{vs}\nCompare B: {compB_name}, {compB_desc}, {compB_country}")
  player_answer = input("Who has more followers? Type 'A' or 'B': ").upper()
  
  if player_answer == most_followers(compA, compB):
    print("BBQ")

    if player_answer == "A":
      score += 1
      clear()
      higher_lower(compA, score)
    else:
      score += 1
      clear()
      higher_lower(compB, score)
  else:
    clear()
    print(you_lose(score))

higher_lower()
