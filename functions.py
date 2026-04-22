def calculate_bmi(weight, height):
    bmi = round(weight / (height * height), 1)
    return bmi


result = calculate_bmi(70, 1.75)
print("Your BMI is", result)

if result < 18.5:
    print("Underweight")
elif result < 25:
    print("Healthy weight")
elif result < 30:
    print("Overweight")
else:
    print("Obese")
