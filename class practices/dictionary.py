# Creation a empty  dictionary 
dictionary = {}
print(dictionary)

# Checking the type of dictionary
dictionary = {}
print(dictionary, type(dictionary))

# Trying a another way to create dictionary -
dictionary = dict()
print(dictionary, type(dictionary))

# Adding keys and value in dictionary 
example = {'color' : 'red '  , 
           'fruit' : 'Banan' ,
           'place' : 'UAE'}
print (example)

# Checking if we want to return one value from a dictionary 

dictionary  = { 'Name' : 'Shazin' , 
                'Roll No ' :  '1228' , 
                'Fathers name ': 'Hussain' } 
print(dictionary["Name"])


# get is use to check if the key or value is there in the dictionary
dictionary  = { 'Name' : 'Shazin' , 
                'Roll No ' :  '1228' , 
                'Fathers name ': 'Hussain' } 
print(dictionary.get("student"))

# To print both the keys and values from the dictionary 
dictionary  = { 'Name' : 'Shazin' , 
                'Roll No ' :  '1228' , 
                'Fathers name ': 'Hussain' } 
print(dictionary.items())
 
# To print only keys from the dictionary 
dictionary  = { 'Name' : 'Shazin' , 
                'Roll No ' :  '1228' , 
                'Fathers name ': 'Hussain' } 
print(dictionary.keys())

# To print only values from the dictionary 
dictionary  = { 'Name' : 'Shazin' , 
                'Roll No ' :  '1228' , 
                'Fathers name ': 'Hussain' } 
print(dictionary.values())


# del is to delet a key or value from the dictionary
dictionary  = { 'Name' : 'Shazin' , 
                'Roll No' :  '1228' , 
                'Fathers name ': 'Hussain' } 
del dictionary ["Roll No"]
print(dictionary.keys())
print(dictionary.values())

# pop items is to remove a items from last value dictionary
dictionary  = { 'Name' : 'Shazin' ,
                'Roll No' :  '1228' , 
                'Fathers name ': 'Hussain' } 
print(dictionary.pop("Name"))
print(dictionary.keys())
print(dictionary.values())
