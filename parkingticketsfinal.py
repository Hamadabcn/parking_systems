import datetime
import uuid
import pytz
# Define a dictionary to store the parking_dict per minute for different time intervals
parking_dict = {
    "price_1": 0.15,  # for 1 to 20 minutes
    "price_2": 0.15,  # for 21 to 60 minutes
    "price_3": 72,  # for a day
    "price_4": 0.15,  # for 61 to 180 minutes
    "price_5": 0.15,  # for 181 to 420 minutes
}

# Ask the user to enter the mode: "entry" or "exit"
mode = input("Enter the mode: entry or exit? ")

# If the mode is "entry", generate a unique ticket number using uuid.uuid4() and store it in a variable
if mode == "entry":
    ticket_number = uuid.uuid4()

    # Get the current date and time as a string and store it in a variable
    entry_time = datetime.datetime.now(pytz.timezone(
        'Europe/Madrid')).strftime("%d/%m/%Y %H:%M:%S")

    # Add the ticket number and the entry time as a key-value pair to the parking_dict dictionary
    parking_dict[ticket_number] = entry_time

    # Print a message with the ticket number and the entry time
    print(f"Your ticket number is {ticket_number}. You entered at {entry_time}.")

# If the mode is "exit", ask the user to enter the ticket number
elif mode == "exit":
    ticket_number = input("Enter your ticket number: ")

    # Check if the ticket number is in the parking_dict dictionary
    if ticket_number in parking_dict:

        # Get the entry time from the parking_dict dictionary by the ticket number
        entry_time = parking_dict[ticket_number]

        # Convert the entry time from a string to a datetime object
        entry_time = datetime.datetime.strptime(
            entry_time, "%d/%m/%Y %H:%M:%S")

        # Get the current date and time as a datetime object
        exit_time = datetime.datetime.now(pytz.timezone('Europe/Madrid'))