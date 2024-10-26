# Exercise 4: Primitive Quiz standard
"""In this exercise, you’ll create a simple program that asks the user a question,
evaluates their answer, and provides feedback."""
# Steps:
"""1. Write a program that asks the user “What is the capital of France?” and
waits for their response.
2. If the user’s answer is correct (i.e., “Paris”), the program should print a
message saying the answer is correct.
3. If the answer is incorrect, the program should print a message saying the
answer is wrong."""
# Asking the users to write the Capital of France
Capital = input("What is the Capital of France: ") 
# Checking the Capital given by the user is corrent or not, By the if statement
if Capital== "Paris":
    print("The answer is correct.")
else:
    print("The answer is wrong.")
