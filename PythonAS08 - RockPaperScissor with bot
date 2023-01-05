import random
choices = ["R","P","S"]
ROUND = 0
count1 = 0
count2 = 0
player1wins = 0
player2wins = 0
rockwins = 0
scissorwins = 0
paperwins = 0
entry_list_1 = []
entry_list_2 = []
while count2 <=5:
  ROUND = ROUND + 1
  print("Round:",ROUND)
  choice1 = input("Please input Rock / Paper / Scissors (RPS) in caps Player1: ")
  if choice1.upper() not in ["R","P","S"]:
    print("Please enter R P or S. Data Invalid ")
  else:
    entry_list_1.append(choice1)
    count1 = count1 + 1
  choice2 = random.choice(choices)
  entry_list_2.append(choice2)
  count2 = count2 + 1
  if choice1 == choice2:
    print("Tie! No one wins")
  elif choice1 in ["r","R"]:
    if choice2 in ["p","P"]:
      print("Player2 wins! Because paper beats rock")
      player2wins = player2wins + 1
      paperwins = paperwins + 1
    elif choice2 in ["s","S"]:
      print("Player1 wins! Because rock beats scissors")
      player1wins = player1wins + 1
      rockwins = rockwins + 1
    else:
     print("Somethings wrong with your input. ")
     count1 = count1 - 1
     count2 = count2 - 1
     ROUND = ROUND - 1
  elif choice1 in ["p","P"]:
    if choice2 in ["r","R"]:
      print("Player1 wins! Because paper beats rock")
      player1wins = player1wins + 1
      paperwins = paperwins + 1
    elif choice2 in ["s","S"]:
      print("Player2 wins! Because scissors beat paper")
      player2wins = player2wins + 1
      scissorwins = scissorwins + 1
    else:
     print("Somethings wrong with your input. ")
     count1 = count1 - 1
     count2 = count2 - 1
     ROUND = ROUND - 1
  elif choice1 in ["s","S"]:
    if choice2 in ["r","R"]:
      print("Player2 wins! Because rock beat scissors")
      player2wins = player2wins + 1
      rockwins = rockwins + 1
    elif choice2 in ["p","P"]:
      print("Player1 wins! Because scissors beat paper")
      player1wins = player1wins + 1
      scissorwins = scissorwins + 1
    else:
     print("Somethings wrong with your input. ")
     count1 = count1 - 1
     count2 = count2 - 1
     ROUND = ROUND - 1
  else:
    print("Somethings wrong with your input. ")
    count1 = count1 - 1
    count2 = count2 - 1
    ROUND = ROUND - 1
print("PLayer1 inputs: ",entry_list_1)
print("PLayer2 inputs: ",entry_list_2)
print("Player1 wins: ", player1wins)
print("Player2 wins: ", player2wins)
print("Ties: ", count2-player1wins-player2wins)
print("Rock wins: ",rockwins)
print("Paper wins: ",paperwins)
print("Scissor wins: ", scissorwins)
