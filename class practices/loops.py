# loops
i = 1
while i < 11:
  print(i)
# i =i+1 
  i += 1   

  count = 1
while count <= 7:
    print("Count is:", count)
    count += 1

# Infinite Loop With Break Statement 
s = 1
while s < 7:
  print(s)
  if s == 3:
    break
  # s=s+1  Both are same 
  s += 1   

  # For loop 
fruits = ["apple", "banana", "mango"]
for z in fruits:
  print(z)


  # Using the range Function with the for Loop
  for x in range(0,19):
      print (x)
for x in range(12):
     print (x)

# To improve readibility 
for x in range(0,18):
      print (x, end=",")
  
# Normaly step count (1 increment ) 
# To count +2 
for x in range (0,21,2):   
   print(x ,end=",")
# To count +5
for x in range (0,55,5):
      print(x,end=",")

# Getting input from user - User Controlled Loop 
w= int (input("Enter the max number for range :"))
for x in range (0,w):
      print(x,end=",")
