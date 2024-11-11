# Exercise 5: Days of the Month avdanced
# The Question
# Advanced Requirement:
"""Leap Year Adjustment: Modify the program to account for leap years. For
February, ask the user if the year is a leap year and adjust the number of days
accordingly."""

# Creating a dictionary putting month Numbers to the Number of Days
Days_in_a_Month = {
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}

# Asking the user to write the Month Number
Month = int(input("Enter the month number (1-12): "))

# Checking if the written Month Number is valid
if Month in Days_in_a_Month:
# Checking for leap Year, if the Month is February
    if Month == 2:
# Asking if it's a leap Year
        is_leap_year = input("Is it a leap year? (yes/no): ").strip().lower()
        if is_leap_year == "yes":
            print("The number of days in February is 29")
        else:
            print("The number of days in February is 28")
    else:
        print(f"The number of days in month {Month} is {Days_in_a_Month[Month]}")
else:
    print("Invalid month number. Please enter a number between 1 and 12.")
