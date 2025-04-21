import tkinter as tk
import random

# Create window
root = tk.Tk()
root.title("Bad Phone Dialer")
root.geometry("300x400")

# Dialed number string
dialed_number = tk.StringVar()

# Display (readonly disable key input)
display = tk.Entry(root, textvariable=dialed_number, font=("Helvetica", 24),
                   justify="right", bd=5, state="readonly")
display.grid(row=0, column=0, columnspan=3, padx=10, pady=20, sticky="nsew")

# Button labels
buttons = [
    '1', '2', '3',
    '4', '5', '6',
    '7', '8', '9',
    '*', '0', '#'
]

# Press function that ignores keyboard input and inserts a random number
def press(_=None):
    display.config(state="normal")
    current = dialed_number.get()
    random_digit = str(random.randint(0, 9))
    dialed_number.set(current + random_digit)
    display.config(state="readonly")

# Clear function to erase the whole input
def clear():
    display.config(state="normal")
    dialed_number.set("")
    display.config(state="readonly")

# Create Clear button (spans full width)
clear_button = tk.Button(root, text="Clear", font=("Helvetica", 20),
                         command=clear)
clear_button.grid(row=1, column=0, columnspan=3, sticky="nsew", padx=5, pady=5)

# Create all buttons that insert random numbers
for index, label in enumerate(buttons):
    row = (index // 3) + 2  # Button grid starts from row 2
    col = index % 3
    button = tk.Button(root, text=label, font=("Helvetica", 20),
                       command=press)
    button.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

# Make the grid expandable
for i in range(6):  # display + clear + 4 rows of buttons
    root.rowconfigure(i, weight=1)
for i in range(3):
    root.columnconfigure(i, weight=1)

# Run the app
root.mainloop()
