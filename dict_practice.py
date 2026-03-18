#The format is "key" , colon (:), "value"
#Having them in this line is better because it is better to read

x = {
    "name" : "David",
    "age" : 10
}

#Why is it called a dictionary???
#Because for each word/key there is a correlated meaning 


#Nested dictionaries 
#We are defining a dictonary inside of a dictionary

x = { 
    "Mario" : {"Math" : 100, "Computer Science" : 80},
    "Dede" : {"Math" : 90, "Computer Science" : 100}     
    
}

#Indexing in dictionaries

print(x["Mario"]["Computer Science"])

#this above prints out mario's grade for computer science 


#how to update a value
#let's say we want to update Dede's math score to 100 

x["Dede"]["Math"] = 100
print(x["Dede"]["Math"])

print(x)


#Suppose we want to add another person to the dictionary

x["Noeliah"] = {"Math" : 85, "Computer Science" : 100}

print(x)

#Another thing to know
#the keys of dictionarys can be of different types 


y = {
    # it can be a string
     "Mario" : {"Math" : 100, "Computer Science" : 80},
    # it can be a touple
    (1,2) : "cat",
    #it can be a number
    2095: "I love pizza"
    
    #it cannot be a list 
    
    
    #The values can also be different 
    #the values can be a list, dictonary, touple, string, etc
    
}


# some methods of dictonaries 

#this is going to print out all of the keys in the dictonary 
print(y.keys())


#this is going to print out all of the values in the dictonary 

print(y.values())


#this one is going to print out/give us the key:value pairs
print("Key value pairs: ")
print(y.items())


#y.clear() will clear everything from the dictonary 


#the dict.get method will get the corresponding value for that key 

print(y.get("Mario"))


#a method to delete something from a dictionary 

y.pop(2095)
print(y)


print(f"Mario's score for Computer Science is {y['Mario']['Computer Science']}")


#the update method can be used to add stuff to a dictionary 