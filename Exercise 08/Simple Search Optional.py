# Simple Search Optional
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
