#!/usr/bin/env python

'''
using nested if elif statements to check the height and age limit of the user

'''

ask_user = int(input("Please enter your height in cm: "))
if ask_user >= 120:
    print("Yup you can ride the rollercoaster")
    get_age = int(input("What is your age? "))
    if get_age < 12:
        print("Please pay $5.")
    elif get_age <= 18:
        print("Please pay $7.")
    elif get_age >= 45 and get_age <= 55:
        print("Your age bracket is entitled to a free ride its on the house lol!")
    else:
        print("Please pay $12.")
else:
    print("Sorry, you have to grow taller before you can ride.")