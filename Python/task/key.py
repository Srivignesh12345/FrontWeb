import tkinter as tk

def key_press(event):
    """Handle key press events"""
    key = event.keysym
    print(f"Key pressed: {key}")

def create_button(frame, text, row, column):
    """Create a button on the virtual keyboard"""
    button = tk.Button(frame, text=text, width=8, height=3)
    button.grid(row=row, column=column, padx=5, pady=5)
    button.bind('<Button-1>', key_press)

# Create the main window
window = tk.Tk()
window.title("Virtual Keyboard")

# Create the function keys
function_keys = [
    'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12'
]
for i, key in enumerate(function_keys):
    create_button(window, key, 0, i)

# Create the number keys
for i in range(10):
    create_button(window, str(i), 1, i)

# Run the main event loop
window.mainloop()
