#Exercise 5: Days of the Month standard
"""Write a program that tells a user how many days there are in a specific month.
Use a dictionary to map the month numbers (1-12) to the number of days in
each month."""

#Instructions:
"""1. Create a Dictionary: Define a dictionary where the keys are month numbers and the values are the number of days in those months.
2. Input Handling: Ask the user to input the month number.
3. Check and Output: Use an if-else statement to check if the input is valid and print the number of days in the corresponding month."""

# Creating a dictionary putting Month Numbers to the Number of Days it has
Days_in_a_Month = {
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}

# Asking the user to input the Month Number
Month = int(input("Enter the Month Num (1-12): "))

# Checking if the input of Number of Month is correct, if it is correct thne it will show how many Days are there in a Month
if Month in Days_in_a_Month:
    print(f"The Number of Days in Month {Month} is {Days_in_a_Month[Month]}")
# If it is wrong it will ask to rewrite the Number of Month again
else:
    print("Invalid Month Number. Please enter a Number between 1 and 12.")
