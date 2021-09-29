#calculating the prize on the age.
print("welcome to rollercoaster!")
height=int(input("what is your height in cm "))
#condition check
if height > 120:
    print("enjoy your ride")
    age=int (input("what is you age "))
    if age<=12:
        print("pay $5")
    elif age<18:
        print("pay $7")
    else:
        print("pay $12")
else:
    print("sorry,you can't ride")