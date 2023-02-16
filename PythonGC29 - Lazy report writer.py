import random 
comments_array = []
student_names = []
num_students = int(input("Input the number of students to comment on: "))
for i in range (num_students): 
  comment = input("Input a generic comment: ")
  comments_array.append(comment)
  student = input("Input student name: ")
  student_names.append(student)

print(random.choice(student_names),"is a", random.choice(comments_array))
