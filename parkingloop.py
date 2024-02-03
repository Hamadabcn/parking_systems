# Define the prices per minute for different time intervals

price_1 = 0.15 # for 1 to 20 minutes
price_2 = 0.15 # for 21 to 60 minutes
price_3 = 72 # for a day
price_4 = 0.15 # for 61 to 180 minutes
price_5 = 0.15 # for 181 to 420 minutes

# Loop the whole program until the user decides to stop
while True:

    # Ask the user to enter the number of minutes they parked
    minutes = int(input("How many minutes did you park? "))

    # Calculate the total cost based on the number of minutes
    if minutes <= 0:
        print("Invalid input. Please enter a positive number.")
    elif minutes <= 20:
        cost = minutes * price_1
    elif minutes <= 60:
        cost = 20 * price_1 + (minutes - 20) * price_2
    else:
    # Assume that a day is 24 hours or 1440 minutes
        
        days = minutes // 1440 # get the number of full days
        
        remainder = minutes % 1440 # get the remaining minutes
        if remainder < 20:
            cost = days * price_3 + remainder * price_1
        elif remainder < 60:
            cost = days * price_3 + 20 * price_1 + (remainder - 20) * price_2
        elif remainder < 180:
            cost = days * price_3 + 20 * price_1 + 40 * price_2 + (remainder - 60) * price_4
        elif remainder <= 454:
            cost = days * price_3 + 20 * price_1 + 40 * price_2 + 120 * price_4 + (remainder - 180) * price_5
        elif remainder < 1440:
            cost = (days + 1) * price_3
            
    # If the remaining minutes are more than seven hours, round up to the next day

    # Import datetime module to get the current date and time
    import datetime

    # Get the current date and time as a string
    now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    # Format the receipt as a string with line breaks and placeholders
    receipt = f"""
    Parking Receipt
    Date: {now}
    Minutes parked: {minutes}
    Total cost: ${cost:.2f}
    Thank you for using parkingapp.com
    """

    # Print the receipt
    print(receipt)

    # Ask the user if they want to save the receipt as a text file
    answer = input("Do you want to save the receipt as a text file? (y/n) ")
    if answer.lower() == "y":
        # Ask the user to enter a file name
        file_name = input("Enter a file name: ")
        # Add .txt extension if not already present
        if not file_name.endswith(".txt"):
            file_name += ".txt"
        # Open a new file with write mode
        with open(file_name, "w") as file:
            # Write the receipt to the file
            file.write(receipt)
        # Print a confirmation message
        print(f"Receipt saved as {file_name}")
    
    # Ask the user if they want to continue using the program or stop
    answer = input("Do you want to continue using the program? (y/n) ")
    
    # If the user enters "n" or "N", break out of the loop and end the program
    if answer.lower() == "n":
        print("Thank you using parkingapp.com")
        break
