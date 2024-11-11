# Exercise 3: Biography avdanced
# The Question
# Advanced Requirements:
"""Have the user input their name, hometown, and age instead of hardcoding the
values. Try giving both your first and second name when asked for your name.
What happens? How can you handle multiple words in Python? Test the
program by entering a string value for age (e.g., “twenty”). What happens?
How can you prevent this issue?"""

# Asking the user to input and store it in a dictionary
person_information = {}

# Asking the user to give their first and second name 
person_information["first_name"] = input("Enter your first name: ")
person_information["second_name"] = input("Enter your second name: ")

# Asking the user to give their hometown 
person_information["hometown"] = input("Enter your hometown: ")

# Asking the user to give their age, as number only if it is not a number then it will show 'Invalid input. Please enter a numeric age.'
while True:
    Age = input("Enter your age: ")
    if Age.isdigit():  
        person_information["age"] = int(Age) 
        break
    else:
        print("Invalid input. Please enter a numeric age.")

# Print the values on separate lines 
print(f"\nName: {person_information['first_name']} {person_information['second_name']}\nHometown: {person_information['hometown']}\nAge: {person_information['age']}")
