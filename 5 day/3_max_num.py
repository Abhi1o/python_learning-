scores=input("enter the number").split( )
#convert the num into integer
print(scores)
for n in range(0, len(scores)):
    scores[n]=int(scores[n])
print(scores)
#check the max number
marks=0
for score in scores:
    if score>marks:
        marks=score

print(f"the highest score in the class is {marks}")
