# Import datetime module to get the current date and time
import datetime

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
        # Generate a unique ticket number by using an f-string
        self.ticket_number = f"{slot_number}_{datetime.datetime.now().timestamp()}"
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

    # Define a method that prints a receipt for the customer
    def print_receipt(self):
        # Check if the exit time is set
        if self.exit_time is not None:
            # Print a header with the name of the parking lot and the date and time of exit
            print("Parking App.com")
            print(self.exit_time.strftime("%d/%m/%Y %H:%M"))
            # Print a line with the ticket number and the slot number
            print(f"Ticket No: {self.ticket_number} | Slot No: {self.slot_number}")
            # Print a line with the registration number and the color of the car
            print(f"Registration No: {self.registration_number} | Color: {self.color}")
            # Print a line with the entry time and the exit time
            print(f"Entry Time: {self.entry_time.strftime('%d/%m/%Y %H:%M')}")
            print(f"Exit Time: {self.exit_time.strftime('%d/%m/%Y %H:%M')}")
            # Print a line with the total fee
            print(f"Total Fee: ${self.calculate_fee()}")
        else:
            # Raise an exception if the exit time is not set
            raise ValueError("Exit time is not set")