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


# Optional Requirements:
"""1. Allow the user to input the search term instead of using a predefined value.
   2. Implement the search functionality based on user input."""  

# Output.  
# Asking the user to write the name 
people = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]
# Asking the user to wrtie the name from or out of the list
Name =input("Enter the person name to search in the list: ")
# Checking the name is there in list or not
if Name in people:
    print("The name you input is there in the list.")
else:
    print("The name you input is not there in the list.")
