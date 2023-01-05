import random
word_list = ["ouija","frame","graze","windy","paint","gourd","swing","vapes","happy","teams","goofy","among"]
answer_list = []
guess_list = []
green = 0 
yellow = 0
word = random.choice(word_list)
def guessing(): 
  guess = input("input a 5 letter word: ")
  for i in range (0,5): 
    temp1 = (word[i:i+1])
    temp2 = (guess[i:i+1])
    answer_list.append(temp1)
    guess_list.append(temp2) 
for i in range (0,5): 
  guessing()
  for i in range (0,5): 
    if answer_list[i] == guess_list[i]: 
      green = green + 1
      print("Correct: ",answer_list[i])
    if answer_list[i] in guess_list: 
      if answer_list[i] != guess_list[i]: 
        yellow = yellow + 1
        print("Half: ",answer_list[i])
    else: 
      yellow = yellow
  print("Correct: ",green)
  print("Half: ",yellow-green)
  green = 0
  yellow = 0
  answer_list = []
  guess_list = []
if green == 5: 
  print("You guessed the word",word,"congrats!")
print(answer_list)
print(guess_list)
