#Advance BMI calculator
height=float(input("enter your height in m: "))
weight=int(input("enter your weight in kg: "))
#BMI formula
bmi=round(weight/height**2)
#round of the output
#condition to check 18.5 underweight, 25 normalweight, 30 overweight,35 obese, 35 above clinically obese.
if bmi<18.5:
    print(f"your BMI is {bmi}, you are underweight")
elif bmi<25:
    print(f"your BMI is {bmi}, you are normalweight")
elif bmi<30:
    print(f"your BMI is {bmi}, you are slightely overweight")
elif bmi<35:
    print(f"your BMI is {bmi}, you are obese")
else:
    print(f"your BMI is {bmi}, you are clinically obese")



