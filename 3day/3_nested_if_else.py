print("welcome to rollercoaster!")
height=int(input("what is your height in cm "))
age=int (input("what is you age "))
#condition check
if height != 120:
    print("enjoy your ride")
    if age<=18:
        print("pay $7")
    else:
        print("pay $12")
else:
    print("sorry,you can't ride")