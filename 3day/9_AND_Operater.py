print("welcome to rollercoaster!")
height=int(input("what is your height in cm "))
bill=0
#condition check
if height > 120:
    print("enjoy your ride")
    age=int (input("what is you age "))
    if age<=12:
        bill+=5
        print("child ticket are $5")
    elif age<18:
        bill+=7
        print("youth ticket are $7")
#AND operation on mid-life age (45-55)
    elif age>=45 and age<=55:
        bill+=0
        print("every thing will be ok, enjoy the free ride on us")
    else:
        bill+=12
        print("adult ticket are $12")

#condition on taking photos
    photo=input("Do you want to take photo? Y or N")
    photo.upper()
    if photo == "Y":
        bill+=3

else:
    print("sorry,you can't ride")

print(f"your total bill is ${bill}")
"abhishek".upper()