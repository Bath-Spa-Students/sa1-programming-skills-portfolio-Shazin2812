# Exercise 4: Advanced Primitive Quiz
# The Question
"""Ignore Capitalization: Modify your program to accept answers regardless of
the capitalization (e.g., “paris”, “Paris”, and “PaRis” should all be considered
correct). Multiple Questions: Extend the program into a quiz that asks for the
capitals of 10 European countries. Provide feedback for each question."""
# 10 European countries and their capitals
Countries_capital = "France,Paris,Switzerland,Bern,Austria,Vienna,Spain,Madrid,Finland,Helsinki,Iceland,Reykjavik,Poland,Warsaw,Norway,Oslo,Germany,Berlin,Italy,Rome"
list = Countries_capital.split(',')
# Using for in range satement
for i in range(0, len(list), 2):
    Countries=list[i]
# Giving the countries a short name as i
    Capital=list[i + 1]
# Ans making the countries and capital together 
    Answer=input(f"What is the capital of {Countries}? ").lower()
# Checking if the answer is correct
    if Answer==Capital.lower():
        print("The answer is Correct.")
# Checking if the answer is wrong 
    else:
        print("The answer is wrong.")
