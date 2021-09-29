#leap year have 366 days
#to find leap year ,leap year divisible by 4.
year=int(input("what is the year? "))

#condition to check the leap year
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("It's a leap year")
        else:
            print("Not a leap year")
    else:
        print("It's a leap year")
else:
    print("Not a leap year")