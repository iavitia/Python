height = float(input("enter your height in inches: "))
weight = float(input("enter your weight in pounds: "))

bmi = round((weight * 703) / (height**2), 2)

if bmi < 16:
    category = 'severly underweight'
elif bmi < 18.4:
    category = 'underweight'
elif bmi < 24.9:
    category = 'normal'
elif bmi < 29.9:
    category = 'overweight'
elif bmi < 354.9:
    category = 'moderately obese'
elif bmi < 39.9:
    category = 'severly obese'
else:
    category = 'morbidly obese'

print(f'Your BMI of {bmi} makes you {category}')