# Exercise 10: Is it even?
"""Write a program that tests if a value is even or odd. Follow the instructions
outlined below:"""
#Instructions:
"""• The program should ask the user for a number from within the main
function.
• The entered number should be passed to a function that determines if the
value is even or odd.
• The function should return a message indicating whether the number is
even or odd.
• The message returned by the function should be printed from within the
main function."""

# Answer
def even_or_odd():
# Separating even number and odd number
    if Number % 2 == 0:
        print("The entered Number is even.")
    else:
        print("The entered Number is odd.")
# Asking the user to write a number
Number = int(input("Enter a Number: "))
# The output will show the numbe which given by the user is even or odd
even_or_odd()
