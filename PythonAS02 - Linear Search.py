Item = int(input("Please input item number: "))
MyArray= [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
def search(Item,MyArray): 
  Position = 0   
  Found = False 
  for Position in range (0, len(MyArray)): 
     if MyArray[Position] == Item: 
       Found = True 
       print("Found it at position", Position)
       return Position
  if Found == False: 
    print("Item not found in list")
    return Position 
print(search(Item, MyArray))
  
