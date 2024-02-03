# Import uuid and datetime modules
import uuid
import datetime
import pytz

company_name = "PARKING BENSI" 
company_address = "C/Paris 179-181"
company_NIF = "B66715459"
company_phone = "+34 630 379 484" 
company_email = "mohbcn1@hotmail.com"

# Define a dictionary to store the prices per minute for different time intervals
prices = {
    "price_1": 0.125,  # for 1 to 20 minutes
    "price_2": 0.0625,  # for 21 to 60 minutes
    "price_3": 36,  # for a day
    "price_4": 0.0784,  # for 61 to 180 minutes
    "price_5": 0.0784,  # for 181 to 420 minutes
}

# Define a constant for the iva tax rate and assign it a value (do not change this value)
iva_rate = 0.21  # 21%

# Define a function to calculate the cost based on the number of minutes
def calculate_cost(minutes):
    
    # Assume that a day is 24 hours or 1440 minutes
    days = minutes // 1440  # get the number of full days
    remainder = minutes % 1440  # get the remaining minutes
    if remainder < 20:
        cost = days * prices["price_3"] + remainder * prices["price_1"]
    elif remainder < 60:
        cost = days * prices["price_3"] + \
            (remainder - 20) * prices["price_2"] + \
            (20 * prices["price_1"])
    elif remainder < 180:
        cost = days * prices["price_3"] + \
            (remainder - 60) * prices["price_4"] + \
            (40 * prices["price_2"]) + \
            (20 * prices["price_1"])
    elif remainder <= 454:
        cost = days * prices["price_3"] + \
            (remainder - 180) * prices["price_5"] + \
            (120 * prices["price_4"]) + \
            (40 * prices["price_2"]) + \
            (20 * prices["price_1"])
    # Remove the iva rate from the cost
    cost = cost / (1 + iva_rate)
    return cost

# Loop the whole program until the user decides to stop
while True:

# Generate a unique ticket number using uuid.uuid4()
    ticket_number = uuid.uuid4()

# Get the current date and time as a string
    now = datetime.datetime.now(pytz.timezone(
        'Europe/Madrid')).strftime("%d/%m/%Y %H:%M:%S")
# Ask the user to enter the number of minutes they parked
    minutes = int(input("How many minutes did you park? "))

# Validate the input and calculate the cost
    if minutes <= 0:
        print("Invalid input. Please enter a positive number.")
    else:
        cost = calculate_cost(minutes)
        
# Print the ticket with the formatted output using f-strings
        print(f"{ticket_number}")
        print(f"Date and time: {now}")
        print(f"Minutes parked: {minutes}")
        print(f"Cost: {cost:.2f} €")
        print(f"IVA: {cost * iva_rate:.2f} €")
        print(f"Total: {(cost + cost * iva_rate):.2f} €")
        print(f"{company_name}")
        print(f"{company_address}")
        print(f"NIF: {company_NIF}")
        print(f"Phone: {company_phone}")
        print(f"Email: {company_email}")
# Ask the user if they need a receipt
    receipt_needed = input("Do you need a receipt? (y/n) ")
# If the user says yes, ask for the client information and format the receipt
    if receipt_needed.lower() == "y":
        name = input("Name: ")
        id_number = input("ID: ")
        car_plate = input("plate number: ")
        address = input("address: ")
        receipt = f"Ticket number: {ticket_number}\n"
        receipt += f"      PARKING BENSI\n"
        receipt += f"     C/ Paris 179-181\n"
        receipt += f"      NIF B66715459\n"
        receipt += f"     +34 630 379 484\n" 
        receipt += f"    mohbcn1@hotmail.com\n"
        receipt += f"Date:{now}\n"
        receipt += f"Name: {name}\n"
        receipt += f"ID: {id_number}\n"
        receipt += f"plate: {car_plate}\n"
        receipt += f"Address: {address}\n"
        receipt += f"Minutes: {minutes}\n"
        receipt += f"Cost:€ {cost:.2f}\n"
        receipt += f"IVA:€ {iva_rate * cost:.2f}\n"
        receipt += f"price: {(cost + cost * iva_rate):.2f} €"
        
# Save the receipt as a txt file using the ticket number as file name
        file_name = str(ticket_number) + ".txt"
        file = open(file_name, "w")
        file.write(receipt)
        file.close()
# Ask the user if they want to continue or stop
        answer = input("Do you want to continue? (y/n) ")
        if answer.lower() == "n":
            break
        