import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                messagebox.showerror("Math Error", "Cannot divide by zero!")
                return
            result = num1 / num2
        else:
            messagebox.showwarning("Invalid", "Please select a valid operation.")
            return

        result_label.config(text=f"Result: {result}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

# Create main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x350")
root.config(bg="white")

# Heading
tk.Label(root, text="Simple Calculator", font=("Arial", 16, "bold"), bg="white").pack(pady=10)

# Entry for number 1
tk.Label(root, text="Enter First Number:", bg="white").pack()
entry1 = tk.Entry(root, font=("Arial", 12))
entry1.pack(pady=5)

# Entry for number 2
tk.Label(root, text="Enter Second Number:", bg="white").pack()
entry2 = tk.Entry(root, font=("Arial", 12))
entry2.pack(pady=5)

# Operation selection
tk.Label(root, text="Choose Operation:", bg="white").pack()
operation_var = tk.StringVar(root)
operation_var.set("+")  # default value

operations_menu = tk.OptionMenu(root, operation_var, "+", "-", "*", "/")
operations_menu.pack(pady=5)

# Calculate button
tk.Button(root, text="Calculate", command=calculate, bg="#28a745", fg="white", font=("Arial", 12)).pack(pady=10)

# Result label
result_label = tk.Label(root, text="Result:", font=("Arial", 14), bg="white")
result_label.pack(pady=10)

# Run the app
root.mainloop()
