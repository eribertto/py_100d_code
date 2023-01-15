# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = round(weight/(height**2), 2)
#print(f"Your BMI is {bmi}")


'''
Weight table class
Under 18.5 they are underweight
Over 18.5 but below 25 they have a normal weight
Over 25 but below 30 they are slightly overweight
Over 30 but below 35 they are obese
Above 35 they are clinically obese.
'''

if bmi <= 18.5:
    underweight = "You are underweight"
    bold_under = "\033[1m" + underweight + "\033[0m"
    print(f"Your BMI is {bmi}, {bold_under}")
elif bmi >= 18.5 and bmi < 25:
    normal = "You are normal weight"
    bold_normal = "\033[1m" + normal + "\033[0m"
    print(f"Your BMI is {bmi}, {bold_normal}")
elif bmi >= 25 and bmi < 35:
    overweight = "You are slightly overweight"
    bold_overw = "\033[1m" + overweight + "\033[0m"
    print(f"Your BMI is {bmi}, {bold_overw}")
else:
    obese = "You are clinically obese"
    bold_obese = "\033[1m" + obese + "\033[0m"
    print(f"Your BMI is {bmi}, {bold_obese}")