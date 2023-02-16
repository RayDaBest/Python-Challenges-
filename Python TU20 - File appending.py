count = 1
with open("counter.txt","r") as whole_file:
 for line in whole_file:
   count = count + 1 

with open("counter.txt","a") as existing_file:
  existing_file.write("\n")
  for i in range(count,count+10):
    line_to_write = str(i)+"\n"
    existing_file.write(line_to_write)
