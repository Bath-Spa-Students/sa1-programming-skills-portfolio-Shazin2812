# Exercise 8: Simple Search
# The Question.
"""Write a program that searches for a specific string within a list of strings. The list
is initialized with specific names (“Jake” ,“Zac”, “Ian”, “Ron”, “Sam”, “Dave”).
, and your task is to search for “Sam”."""

# Output.
# Writing the names of the people
people =["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]
# Searching the name Sam in list
person ="Sam"
# Checking the name is there in list
if person in people: 
    print("The name you enter is there in the list.")
else:
    print("The name you enter is not there in the list.")
