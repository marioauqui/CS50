#Ask user to input a variable name in camelCase
#Assume that it is in camelCase


camelCase = input("Enter a variable name in camelCase: ")

snake_case = ""


for i in camelCase:
    #checks to see if the character is an uppercase letter
    #if it is, it adds an underscore before that letter and then makes the letter lowercase
    if i.isupper():
        snake_case += "_" + i.lower()
    #if the letter is not uppercase, it simply adds it to snake_case
    else:
        snake_case += i;

#Then transform the variable into snake_case
print("snake_case: " , snake_case)

