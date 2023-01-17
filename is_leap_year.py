#!/usr/bin/env python

# check if a year is leap year or no
# https://stackoverflow.com/questions/11621740/how-to-determine-whether-a-year-is-a-leap-year

import calendar
year = int(input("Enter the year to check for leap year: "))
if calendar.isleap(year):
    print(f"{year} is a leap year!")
else:
    print("Nope not a leap year")

# note: use error exception handling here