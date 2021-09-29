student_height=input("enter the name of the student ").split()

#convert list into int variable
for n in range(0,len(student_height)):
    student_height[n]=int(student_height[n])
print(student_height)

#sum of the height of student
add=0 
for height in student_height:
    add+=height
print(add)
# number of students
no_student=0
for student in student_height:
    no_student+=1
print(no_student)
#average height
average=round(add/no_student)
print(average)
