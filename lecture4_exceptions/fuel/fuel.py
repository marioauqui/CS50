while True:
    try:
        fraction = input("Fraction: ")
        # break the user input into the dividend(x) and the divisor(y)
        x, y = fraction.split('/')
        
        #turn them into integers
        x = int(x)
        y = int(y)
        
        #x cannont be greater than y 
        if x > y:
            print("X cannot be greater than Y. Please try again.")
            continue
        #  Jumps back to "Fraction: " prompt immediately

        
        percentage = int((x / y) * 100)
        
        if percentage <= 1:           
            print("E")
        elif percentage >= 99:        
            print("F")
        else:
            print(f"{percentage}%")    
            
        break
    
    except ValueError:
        print("Invalid input. Please enter integers in the format X/Y.")
