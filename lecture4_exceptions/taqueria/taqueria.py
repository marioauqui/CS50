

menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total_price = 0

while True:
    try:
        food_item = input("Item: ").title()
        if not food_item in menu:
            continue
    
        total_price += menu[food_item] 
        print(f"Total: ${total_price:.2f} (press cntrl + d when order is complete)")
    except EOFError:
        print("Thank you for shopping with us, come again soon")
        break
    
    
    
    

#Track all of the orders that the customer places and show the price added up together 

#If an item is not on the menu ignore it 

