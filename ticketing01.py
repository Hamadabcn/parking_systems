# Import datetime module to get the current date and time
import datetime
# Import random module to generate random numbers
import random
# Import time module to use the sleep function
import time

# Define a class for tickets
class Ticket:
    # Define a class variable for the base fee per minute
    base_fee = 0.1

    # Define an initializer method that takes the registration number, color, and slot number of the car
    def __init__(self, registration_number, color, slot_number):
        # Assign the parameters to instance variables
        self.registration_number = registration_number
        self.color = color
        self.slot_number = slot_number
        # Generate a unique ticket number by using an f-string and formatting the timestamp as a string
        self.ticket_number = f"{slot_number}_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
        # Record the entry time as the current time
        self.entry_time = datetime.datetime.now()
        # Initialize the exit time to None
        self.exit_time = None

    # Define a method that calculates the total fee based on the exit time
    def calculate_fee(self):
        # Check if the exit time is set
        if self.exit_time is not None:
            # Calculate the duration in minutes by subtracting the entry time from the exit time
            duration = (self.exit_time - self.entry_time).total_seconds() / 60
            # Calculate the total fee by multiplying the duration by the base fee
            total_fee = duration * self.base_fee
            # Return the total fee rounded to two decimal places
            return round(total_fee, 2)
        else:
            # Raise an exception if the exit time is not set
            raise ValueError("Exit time is not set")

    # Define a class method that sets the exit time for a ticket object
    @classmethod
    def set_exit_time(cls, ticket):
        ticket.exit_time = datetime.datetime.now()

# Define a function that asks for a ticket number and prints the fee to charge
def charge_client(tickets):
    # Use a while loop to keep asking for ticket numbers
    while True:
        # Ask for a ticket number from the user and store it in a variable
        ticket_number = input("Enter ticket number or 'q' to quit: ")
        # Check if the user entered 'q' to quit
        if ticket_number == 'q':
            # Break out of the loop
            break
        # Loop through the tickets list and find the matching ticket object
        for ticket in tickets:
            # Check if the ticket number matches with the user input
            if ticket.ticket_number == ticket_number:
                # Print the fee to charge for that ticket object
                print(f"Fee: {ticket.calculate_fee()} euros")
                # Break out of the loop
                break
        else:
            # Print an error message if no matching ticket object is found
            print("Invalid ticket number")

# Create a list of ticket objects for testing purposes
tickets = [
    Ticket("123", "b", 1),
    Ticket("456", "r", 2),
    Ticket("789", "g", 3)
]

# Simulate some time passing by using the sleep function and setting a random exit time for each ticket
for ticket in tickets:
    # Sleep for a random number of seconds between 1 and 10
    time.sleep(random.randint(1, 10))
    # Set the exit time for the ticket object
    Ticket.set_exit_time(ticket)

# Call the charge_client function and pass the tickets list as an argument
charge_client(tickets)