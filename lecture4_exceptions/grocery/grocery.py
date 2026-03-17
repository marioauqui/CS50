grocery_list = {}


while True:
    try:
        item = input("Item (cntrl d when finished): ").strip()
        
        if item in grocery_list:
            grocery_list[item] += 1
            
        
        else:
            grocery_list[item] = 1
            
        
    except EOFError:
        break

    
print("Grocery list: ")
                #sorts the list in alphabetical order
for item in sorted(grocery_list.keys()):
    print(f"{grocery_list[item]} {item.upper()}")
        
        #{grocery_list[item]} gives you how many of that item ; Values = The counts (how many you're buying)
        #{item} gives you what the item is ; Keys = The item names (what you're buying)
       
        

