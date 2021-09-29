bill=float(input("enter your billing amount: "))
tip=int(input("what percentage tip would you like to give? 10, 12 or 15?  "))
people=int(input("how many people to split the bill: "))

#12/100 - 0.12 - 1+0.12 - 1.12 

tip= 1+tip/100

bill_gen=bill/people*tip
#two decimal place - ("{:.2f}".format(variable name))
total_bill=("{:.2f}".format(bill_gen))

print(f"Each person should pay {total_bill}")

