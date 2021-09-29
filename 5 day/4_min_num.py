marks=input("enter student marks").split( )

#convert str into integer 
for n in range(0,len(marks)):
    marks[n]=int(marks[n])
print(marks)

score=9999
print(type(score),type(marks))
for m in marks:
    if m<score:
        score=m

print(f"lowest marks in the class is {score}")