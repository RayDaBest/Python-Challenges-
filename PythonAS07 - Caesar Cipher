phrase = input("Input the phrase to be encrypted: ")
k = int(input("Input the number of shifts: "))
encrypted = ""

for i in range (0,len(phrase)): 
  x = ord(phrase[i:i+1])
  if x == 32: 
    encrypted = encrypted + " "
  else: 
    total = x+k
    y = chr(total)
    encrypted = encrypted + y
print("Encrypted: ",encrypted)
print("Decrypted: ",phrase)
