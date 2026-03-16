def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    
     
    # rule one: check to see if it's 2 - 6 the length (inclusive)
    
    if len(s) < 2 or len(s) > 6:
        return False
    
    # rule two: must start with at least two letter
    
    if not s[0:2].isalpha():
        return False
    
    # rule three: must be number or letter (nothing else)
    
    if not s.isalnum():
        return False
    
    # rule four: Numbers must be at the end and first number can't be 0
    
    for i in range(len(s)):
        # Check if the current character (at position i) is a digit (0-9)
        if s[i].isdigit():
            # We found the FIRST number in the plate at position i
            # Rule: The first number cannot be '0'
            if s[i] == "0":
                return False
            
            #ALL remaining characters must also be numbers (no letters allowed after numbers start)
            if not s[i:].isdigit():
                return False
            break 
    
    return True
                

main()