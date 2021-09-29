#pizza order machine 
print("Welcome to python pizza Delivery")
size=input("what size pizza do you want?S, M or L: ")
size=size.upper()
pepperoni=input("Do you want some pepperoni? Y or N: ")
pepperoni=pepperoni.upper()
cheese=input("Do you some more extra cheese? Y or N: ")
cheese=cheese.upper()
bill=0

#condition on Size
if size=="S":
    bill+=15
elif size=="M":
    bill+=20
else:
    bill+=25

#condition on pepperoni
if pepperoni=="Y":
    if size=="S":
        bill+=2
    else:
        bill+=3
#condition on cheese
if cheese=="Y":
    bill+=1

print(f"your total bill is ${bill}")




