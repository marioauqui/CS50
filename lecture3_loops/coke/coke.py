

current_price = 50
print("Amount due: ", current_price)




while current_price > 0:
    amount_paid = int(input("Insert Coin: "))
    if amount_paid in [5, 25, 50]:
        current_price = current_price - amount_paid
        print("Amount due: ", current_price)
        
    else:
        print("We only accept 5, 25, or 50 cents")
        print("Amount due: ", current_price)


print("Change Owed: " , current_price * -1)
