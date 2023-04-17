NumbersArray = [] 
digits = int(input("Input number of digits you want to sort: "))
for i in range (0, digits): 
  digit = int(input("Input digit: "))
  NumbersArray.append(digit)
print(NumbersArray)

boundary = digits - 1
NoSwaps = True  
while NoSwaps == True: 
  NoSwaps = True
  for j in range (0,boundary): 
    for i in range(0,boundary):
      if NumbersArray[i] > NumbersArray[i+1]: 
        Temp = NumbersArray[i]
        NumbersArray[i] = NumbersArray[i+1]
        NumbersArray[i+1] = Temp
        NoSwaps = False 
    print(NumbersArray)
