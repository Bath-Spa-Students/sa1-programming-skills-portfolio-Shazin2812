# Exercise 6: Brute Force Attack optional
# The Question
# Optional Requirements:
"""Modify the program to include a maximum of 5 password attempts. If the
user enters the wrong password, inform them of the remaining attempts. If the
maximum number of attempts is reached, inform the user that the authorities
have been alerted."""
# Setting a correct password
Password = "01234567"
# Setting the maximum number of attempts a user can try
max_attempts = 5
# Initialize attempt counter
attempts = 0
# Use a while loop to repeatedly ask the user to write the password
while attempts < max_attempts:
# Asking the user to write the password
    entered_password = input("Enter the Password: ")
    # Checking if the written password is correct or incorrect
    if entered_password == Password:
        print("Correct Password.")
        break
    else:
# counting the attempt that user tried
        attempts += 1
# Checking if maximum attempts reached or not
    if attempts < max_attempts:
        print(f"The password you wrote is Incorrect. You have {max_attempts - attempts} attempts left.")
    else:
            print("Your maximum attempts have reached. The authorities have been alerted.")
