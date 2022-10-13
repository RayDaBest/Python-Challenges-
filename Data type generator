import random
from random import randint 
import datetime 
def create_int(): 
  return str(randint(48,57))
def create_real(): 
  return random.uniform(0.1,9.9)
def create_char(): 
  return chr(randint(48,126))
def create_str(): 
  return chr(randint(48,126))

data_type = int(input(" Input from 1 to 6 of which data type you would like to see\n(1 Integer, 2 Real, 3 Char, 4 String, 5 Boolean, \n6 Date): "))
while data_type > 6 or data_type < 1: 
  data_type = int(input("Input number again: "))
print(data_type)

if data_type == 1: 
  myint = create_int()
  print("Integer: ", myint)
if data_type == 2: 
  myreal = create_real()
  print("Real: ", myreal)
if data_type == 3: 
  mychar = create_char()
  print("Character:", mychar)
if data_type == 4: 
  mystr1 = create_str()
  mystr2 = create_str()
  print("String: ", mystr1,mystr2,sep="")
if data_type == 5: 
  myboolean = random.choice(["True","False"])
  print("Boolean: ", myboolean)
if data_type == 6: 
  year = int(input("Input year: "))
  month = int(input("Input month: "))
  day = int(input("Input day: "))
  mydate = datetime.date(year, month, day)
  print("Date: ", mydate)
