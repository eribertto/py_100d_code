#!/usr/bin/env python

# check if a year is leap year or no

year = int(input("Enter the year to check for leap year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year")
        else:
            print(f"{year} is NOT a leap year")
    else:
        print(f"{year} is a leap year")
else:
    print(f"{year} is NOT leap year")
