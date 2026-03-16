

word = input("Input a word/text: ").lower()

twt_word = ""

for i in word:
    if i in ["a","e","i","o", "u"]:
        twt_word += ""
    else:
        twt_word += i
    
print(twt_word)
    
    
    