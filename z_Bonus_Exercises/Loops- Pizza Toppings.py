# Loops- Pizza Toppings :
"""Write a loop that prompts the user to enter a series of pizza toppings until they enter a
'quit' value. As they enter each topping,
Print a message saying you’ll add that topping to their pizza."""
# Output
# using while true for series of pizza toppings
while True:
    Series=input("Writing a pizza topping and enter 'quit' to finish it: ")
    
    if Series.lower()=='quit':
        break
    else:
        print(Series,"is added to the pizza.") 
