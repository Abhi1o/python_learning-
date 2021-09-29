#BMI(Body mass index) = weight(kg) / height(h*h)

weight=float(input("enter your weight in (kg) : "))
height=float(input("enter your height in (m) : "))
bmi=weight/height**2
bmiint=int(bmi)

print("\nyour BMI is "+ str(bmiint))

