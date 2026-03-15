#Make a function called convert that takes an str as input and turns it into an emoji.
#all other text remains unchanged

def convert(emoticon):

   emoticon = emoticon.replace(":)", "🙂")

   emoticon = emoticon.replace(":(", "🙁")


   #print(emoticon, "test")

   return emoticon



#Implement a function called main, that asks the user for input, calls convert on that input, and prints the results
def main():

   user_input = convert(input("Please type in an emoticon "))

   print(user_input)



#Don't forget to call the main function

main()

