# this will create an infinite loop

while True: 


# Define the prices per minute for different time intervals

    price_1 = 0.125 # for 1 to 20 minutes
    price_2 = 0.0625 # for 21 to 60 minutes
    price_3 = 36 # for a day
    price_4 = 0.0784 # for 61 to 180 minutes
    price_5 = 0.0784 # for 181 to 420 minutes

# Ask the user to enter the number of minutes they parked
    minutes = int(input("How many minutes did you park? "))

# Calculate the total cost based on the number of minutes
    if minutes < 0:
        print("Invalid input. Please enter a positive number.")
    elif minutes < 20:
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

# Print the total cost with two decimal places
    print(f"The total cost is ${cost:.2f}")
    
    # Print a farewell message
    print("Thank you for using parking app.com")

    answer = input("Do you want to continue? (y/n) ") 
# this will ask the user if they want to continue

    if answer.lower() == "n": 
# this will check if the user entered "n" or "N"

        break 
# this will exit the loop
