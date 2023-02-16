count1 = 0 
count2 = 0 
word = "if" or "If"

with open("ifpoem.txt","r") as whole_file:
   for line in whole_file:
     if word in line.lower(): 
       count1 = count1 + 1
     print(line,end="")

with open("ifpoem.txt","a") as existing_file:
  for i in range (38,39): 
    write = str("If count: ") + str(count1)
    existing_file.write(write)

print("\n")
with open("ifmam.txt","r") as whole_file:
   for line in whole_file:
     if word in line.lower(): 
       count2 = count2 + 1
     print(line,end="")

with open("ifmam.txt","a") as existing_file:
  for i in range (37,38): 
    write = str("If count: ") + str(count2)
    existing_file.write(write)

print("\n")
if count1 > count2: 
  print("IF has more ifs than mam by: ",count1-count2)
else:
  print("Mam has more ifs than IF by: ",count2-count1)
   
