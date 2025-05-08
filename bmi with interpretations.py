weight = 85
height = 1.85

bmi = weight / (height ** 2)

#adding if else statement for interpretation of bmi
if bmi < 18.5 :
    print("underweight")
elif bmi >= 18.5 and bmi < 25 :
    print("normal weight")
else:
    print("overweight")