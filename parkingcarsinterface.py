# Import your code as a module or copy and paste it here
# For example, let's assume your code is in a file called parking.py
# and it has a function called calculate_cost(minutes) that returns the cost

import PySimpleGUI as sg
import parking

# Define the layout
layout = [
    [sg.Text("How many minutes did you park?")],
    [sg.Input(key="-MINUTES-")],
    [sg.Button("OK"), sg.Button("Cancel")],
    [sg.Text(size=(40,1), key="-OUTPUT-")]
]

# Create the window
window = sg.Window("Parking App", layout)

# Create the event loop
while True:
    event, values = window.read()
    # End program if user closes window or presses Cancel
    if event == sg.WINDOW_CLOSED or event == "Cancel":
        break
    # Call your program's function and update the output element with the result
    elif event == "OK":
        try:
            minutes = int(values["-MINUTES-"])
            cost = parking.calculate_cost(minutes)
            window["-OUTPUT-"].update(f"The total cost is ${cost:.2f}")
        except ValueError:
            window["-OUTPUT-"].update("Invalid input. Please enter a positive number.")

# Close the window
window.close()