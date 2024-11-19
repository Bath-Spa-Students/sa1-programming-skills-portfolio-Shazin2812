#  Nested if and else statements
salary = int (input("Enter your salary :"))
if salary >= 30000:
    years_on_job = float(input("Enter the years of job: "))
# Checking if the user have experience of 2 or more than 2  
    if years_on_job >= 2:
        print("you qualify for your job ")
    else : 
        print ("experience is less than 2")
else:
    print("your earn atleast 30 k to qualify ")
