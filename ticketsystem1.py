# Define an initializer method that takes the registration number, color, and slot number of the car
def __init__(self, registration_number, color, slot_number):
    # Assign the parameters to instance variables
    self.registration_number = registration_number
    self.color = color
    self.slot_number = slot_number
    # Generate a unique ticket number by concatenating the slot number and the current timestamp
    self.ticket_number = str(slot_number) + "_" + str(datetime.datetime.now().timestamp())
    # Record the entry time as the current time
    self.entry_time = datetime.datetime.now()

# Define a method that calculates the total fee based on the exit time
def calculate_fee(self, exit_time):
    # Calculate the duration in minutes by subtracting the entry time from the exit time
    duration = (exit_time - self.entry_time).total_seconds() / 60
    # Calculate the total fee by multiplying the duration by the base fee
    total_fee = duration * self.base_fee
    # Return the total fee rounded to two decimal places
    return round(total_fee, 2)

# Define a method that prints a receipt for the customer
def print_receipt(self, exit_time):
    # Print a header with the name of the parking lot and the date and time of exit
    print("Parking App.com")
    print(exit_time.strftime("%d/%m/%Y %H:%M"))
    # Print a line with the ticket number and the slot number
    print(f"Ticket No: {self.ticket_number} | Slot No: {self.slot_number}")
    # Print a line with the registration number and the color of the car
    print(f"Registration No: {self.registration_number} | Color: {self.color}")
    # Print a line with the entry time and the exit time
    print(f"Entry Time: {self.entry_time.strftime('%H:%M')} | Exit Time: {exit_time.strftime('%H:%M')}")
    # Print a line with the total fee for the customer
    print(f"Total Fee: ${self.calculate_fee(exit_time)}")