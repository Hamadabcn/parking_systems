# Import uuid and datetime modules
import uuid
import datetime

# Define the prices per minute for different time intervals

price_1 = 0.15 # for 1 to 20 minutes
price_2 = 0.15 # for 21 to 60 minutes
price_3 = 72 # for a day
price_4 = 0.15 # for 61 to 180 minutes
price_5 = 0.15 # for 181 to 420 minutes

# Define a constant for the IVA tax rate and assign it a value (do not change this value)
iva_rate = 0.21 # 21%

# Loop the whole program until the user decides to stop
while True:

    # Generate a unique ticket number using uuid.uuid4()
    ticket_number = uuid.uuid4()

    # Get the current date and time as a string
    now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

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

    # Print the ticket number and cost first
    print(f"Ticket number: {ticket_number}")
    print(f"Cost: ${cost:.2f}")

    # Calculate the IVA tax amount by multiplying the cost and the IVA_RATE
    iva_tax = cost * iva_rate

    # Add the IVA tax amount to the cost to get the total price
    total_price = cost

    # Ask the user if they need a receipt
    receipt_needed = input("Do you need a receipt? (y/n) ")

    # If the user says yes, ask for the client information and format the receipt
    if receipt_needed.lower() == "y":
        name = input("Enter the name of the client: ")
        id_number = input("Enter the ID number of the client: ")
        car_plate = input("Enter the car plate number of the client: ")
        address = input("Enter the address of the client: ")

        receipt = f"Ticket number: {ticket_number}\n"
        receipt += f"Date and time: {now}\n"
        receipt += f"Name: {name}\n"
        receipt += f"ID number: {id_number}\n"
        receipt += f"Car plate number: {car_plate}\n"
        receipt += f"Address: {address}\n"
        receipt += f"Minutes parked: {minutes}\n"
        receipt += f"Cost: ${cost:.2f}\n"
        receipt += f"IVA tax: ${iva_tax:.2f}\n"
        receipt += f"Total price: ${total_price:.2f}\n"
        
        # Save the receipt as a txt file using the ticket number as file name
        file_name = str(ticket_number) + ".txt"
        file = open(file_name, "w")
        file.write(receipt)
        file.close()
        
        # Ask the user if they want to continue or stop
        answer = input("Do you want to continue? (y/n) ")
        if answer.lower() == "n":
            break
        