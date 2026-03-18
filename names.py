name = input("What's your name? ") 


# "a" means to append
#file = open("names.txt", "a")
#file.write(f"{name}\n")
#file.close() 


#or you can use with 
# which does the same thing as the lines above
#however, this way you won't forget to close the file  

with open("names.txt", "a") as file:
    file.write(f"{name}\n")