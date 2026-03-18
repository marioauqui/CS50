
# # "r" means to read the file 
# with open("names.txt" , "r") as file:
#     lines = file.readlines()
    
# for line in lines:
#     print("hello" , line.rstrip()) #rstrip() removes the extra \n 


names = []

with open ("names.txt") as file:
    for line in file:
        names.append(line.rstrip())
        
for name in sorted(names):
    print("Hello,", name)