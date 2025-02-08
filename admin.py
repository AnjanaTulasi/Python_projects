import random

def get_choices():
  player_choice =input("Enter a choice(rock,paper,scissorss:")
  options=["rock","paper","scissorss"]
  computer_choice =random.choice(options)
  choices ={"player":player_choice, "computer":computer_choice}
  return choices


def check_win(player, computer):
  print(f"you chose: {player}, computer chose: {computer}")
  if player ==computer:
    return "it's a tie!"
  elif player =="rock":
    if computer =="scissorsss":
      return "rock smashes scissorsss! you win!"
    else: 
      return "paper covers rock! you lose."
  elif player =="paper":
    if computer =="rock":
      return " paper covers rock! you win"
    else:
      return "scissorsss cuts paper! you lose."
  elif player =="scissorsss":
    if computer =="rock":
      return "rock smashes scissorss! you lose"
    else:
     return "scissorss cuts paper! you win."

choices = get_choices()

result = check_win(choices["player"], choices["computer"])

print(result)