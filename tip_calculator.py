#!/usr/bin/env python

# tip calculator exercise, final assignment/project of Day 2
# https://www.udemy.com/course/100-days-of-code/learn/lecture/17841394#overview

#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
welcome_msg = "Welcome to the Tip Calculator"
print(welcome_msg, "\n")
ask_total_bill = float(input("What is the total bill? $"))
tip_to_give = int(input("What percent tip you like to give? 10, 12 or 15? "))
no_of_people = input("How many people to split the bill? ")

#bill = 150
bill = ask_total_bill
tip_prcnt = tip_to_give/100 # float
bill_with_tip = round((bill * (1 + tip_prcnt)), 2) # needs formatting here
#bill_with_tip = (bill * (1 + tip_prcnt))
group = int(no_of_people)
per_person_amount = (bill * 1+tip_prcnt) / group
print(f'per person amount is {per_person_amount}')
# format to 2 decimal places
formatted_amount = "{:.2f}".format(per_person_amount)
print(f"The total bill ${bill} with {tip_to_give}% tip is ${bill_with_tip}")
msg = "Each person should pay: "
print(f"{msg} ${formatted_amount}")