#ride picture taking prize calculator
print("welcome to rollercoaster!")
height=int(input("what is your height in cm "))
#condition check
if height >= 120:
    print("enjoy your ride")
    age=int (input("what is you age "))
    #$5 for under 12 years child
    if age <= 12:
        bill=5
        print("pay $5")
    #$7 for under 18 years 
    elif age <= 18:
        bill=7
        print("pay $7")
    #$12 for above 18 years adult
    else:
        bill=12
        print("pay $12")
    photo=input("Do you want to take photos? Y or N ")
    if photo == "y":
        bill += 3
    print(f"you have to pay ${bill}")

else:
    print("sorry,you can't ride")