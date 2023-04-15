NumbersArray = [] 
digits = int(input("Input number of digits you want to sort: "))
for i in range (0, digits): 
  digit = int(input("Input digit: "))
  NumbersArray.append(digit)
print(NumbersArray)
NumbersArray.append()
print(NumbersArray)

NoSwaps = True
boundary = digits 
while NoSwaps == True: 
  NoSwaps = True 
  for j in range (0,boundary): 
    FirstID = NumbersArray[j]
    SecondID = NumbersArray[j+1]
    if FirstID > SecondID: 
      temp = NumbersArray[j] 
      NumbersArray[j] = NumbersArray[j+1] 
      NumbersArray[j+1] = temp 
      NoSwaps = False   
    boundary = boundary - 1 
  print(NumbersArray)
