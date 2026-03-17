# Dictionary to convert month names to numbers
months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12,
}

while True:
    try:
        # Get input from user
        date = input("Date: ").strip()
        
        # Check if format has slashes (MM/DD/YYYY)
        if "/" in date:
            # Split the string by "/" into a list
            parts = date.split("/")
            
            # Assign each part to variables and convert to integers
            month = int(parts[0])
            day = int(parts[1])
            year = int(parts[2])
            
        # Check if format has comma (Month Day, Year)
        elif "," in date:
            # First, remove the comma by replacing it with nothing
            date_no_comma = date.replace(",", "")
            
            # Split by space into parts
            parts = date_no_comma.split(" ")
            
            # First part is month name, second is day, third is year
            month_name = parts[0].capitalize()
            day = int(parts[1])
            year = int(parts[2])
            
            # Convert month name to number using dictionary
            month = months[month_name]
            
        else:
            # If neither format, prompt again
            print("Invalid format. Please use MM/DD/YYYY or Month Day, Year")
            continue
        
        # Validate that month and day are within range
        if month < 1 or month > 12:
            print("Month must be between 1-12")
            continue
            
        if day < 1 or day > 31:
            print("Day must be between 1-31")
            continue
        
        # Print in YYYY-MM-DD format with leading zeros
        # :02d means "format as integer with at least 2 digits, pad with zeros"
        print(f"{year}-{month:02d}-{day:02d}")
        break  # Exit loop after successful conversion
        
    except ( KeyError):
        # KeyError: if month name not in dictionary
        print("Invalid date. Please try again.")
        continue