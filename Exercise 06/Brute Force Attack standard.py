# Exercise 6: Brute Force Attack standard
"""Write a program that simulates a password entry system. The correct password
is defined as 12345. The program should keep asking the user to enter the
password until they provide the correct one."""
# Basic Requirements:
"""1. Define the correct password.
2. Use a while loop to repeatedly ask the user for the password until the
correct one is entered.
3. Output an appropriate message when the correct password is entered."""

# Setting a correct password
Password = "01234567"
while True:
# Asking the user to write the password
    entered_password = input("Enter the Password: ")
# Checking if the written password is correct or incorrect
    if entered_password == Password:
        print("Correct Password.")
        break
    else:
        print("Incorrect Password")
