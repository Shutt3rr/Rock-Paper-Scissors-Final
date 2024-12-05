import os
import random

scores = [0, 0, 0, 0]

def get_user_choice():
  while True:
    try:
      choice = input("Choose Rock Paper or Scissors: ").lower().strip()
      if choice not in ["rock", "paper", "scissors"]:
        raise ValueError
    except ValueError:
      print("Invalid entry.")
      print("You must choose rock, paper, or scissors")
    else:
      return choice


def get_computer_choice():
  options = ["rock", "paper", "scissors"]
  computer_choice = random.choice(options)
  return computer_choice

def determine_winner(user_choice, computer_choice, scores):
  if user_choice == computer_choice:
    print("It's a tie!")
    scores[3] += 1

  elif (user_choice == "scissors" and computer_choice == "paper") or \
  (user_choice == "rock" and computer_choice == "scissors") or \
  (user_choice == "paper" and computer_choice == "rock"): 
    print("You won!")
    scores[1] +=1

  else:
    print("The computer won!")
    scores[2] += 1




def scoreboard(scores):
  print()
  print("==SCOREBOARD==")
  print(f"Player wins: {scores[1]}")
  print(f"CPU Wins: {scores[2]}")
  print(f"Tie games: {scores[3]}")
  print(f"Games played: {scores[0]}")
  win_percentage = round(((scores[1]/scores[0])*100), 2)
  print(f"Win percentage: {win_percentage}%")

def play_game(scores):
  while True:
    user_choice = get_user_choice()
    scores[0] +=1
    computer_choice = get_computer_choice()
    print(f"You chose: {user_choice}")
    print(f"The computer chose: {computer_choice}")
    determine_winner(user_choice, computer_choice, scores)
    scoreboard(scores)
    choice = input("Would you like to play again (y/n)?: ").lower().strip()
    os.system("clear")
    if choice == "y":
      continue
    else:
      break


play_game(scores)
