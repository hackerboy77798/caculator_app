import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Entry field for displaying the input and result
entry = tk.Entry(root, width=20, font=('Arial', 20))
entry.grid(row=0, column=0, columnspan=4)

# Define the calculator buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row_val = 1
col_val = 0

for button_text in buttons:
    if button_text == "=":
        tk.Button(root, text=button_text, padx=20, pady=20, font=('Arial', 20), command=calculate).grid(row=row_val, column=col_val)
    elif button_text == "C":
        tk.Button(root, text=button_text, padx=20, pady=20, font=('Arial', 20), command=clear).grid(row=row_val, column=col_val)
    else:
        tk.Button(root, text=button_text, padx=20, pady=20, font=('Arial', 20), command=lambda text=button_text: button_click(text)).grid(row=row_val, column=col_val)
    
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()
