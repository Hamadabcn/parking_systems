import PySimpleGUI as sg

# Define the layout
layout = [
    [sg.Text("Enter your name:")],
    [sg.Input(key="-NAME-")],
    [sg.Button("OK"), sg.Button("Cancel")],
    [sg.Text(size=(40,1), key="-OUTPUT-")]
]

# Create the window
window = sg.Window("Hello", layout)

# Create the event loop
while True:
    event, values = window.read()
    # End program if user closes window or presses Cancel
    if event == sg.WINDOW_CLOSED or event == "Cancel":
        break
    # Update the output text element to show a greeting
    elif event == "OK":
        name = values["-NAME-"]
        window["-OUTPUT-"].update(f"Hello, {name}!")

# Close the window
window.close()

