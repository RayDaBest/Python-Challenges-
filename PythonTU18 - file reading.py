line = 0 
poem = int(input("Which poem will you want to read? (1 for If.poem, 2 for Mam.poem): "))
if poem == 1: 
  with open("ifpoem.txt","r") as whole_file:
   for line in whole_file:
     choice = int(input("Do you want to move to the next line? 1/0: "))
     if choice == 1: 
        print(line,end="")
     else: 
        print("Line skipped")
elif poem == 2: 
  with open("ifmam.txt","r") as whole2_file: 
    for line in whole2_file: 
     choice = int(input("Do you want to move to the next line? 1/0: "))
     if choice == 1: 
        print(line,end="")
     else: 
        print("Line skipped")
else: 
  print("Invalid poem")
  
