# Elif 
a = 200
b = 20
# Checking if b is greater than a
if b > a :
    print("b is greater than a")
# Checking if a and b are equal
elif a == b: 
    print("a and b are equal")
# Checking if a is greater than b
else:
    print("a is greater than b")
    
# The elif Statement
# Trying the flowchart
# Asking the person to put their score
score = int(input("Enter your score : "))
# Checking the person score is A grade or not
if score >= 90:
    print ("Your grade is A.")
# Checking the person score is B grade or not
elif score >= 80:
    print ("Your grade is B.")   
# Checking the person score is C grade or not
elif score >= 70:
    print ("Your grade is C.")
# Checking the person score is D grade or not
elif score >= 60:
    print ("Your grade is D.")
# Checking the person score is F grade or not
else:
    print ("Your grade is F.") 
