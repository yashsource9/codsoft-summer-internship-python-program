import tkinter as tk
from tkinter import messagebox
import random
import string


# Function to generate password
def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError("Length must be greater than 0")

        # Characters to use in the password
        characters = string.ascii_letters + string.digits + string.punctuation

        # Generate password
        password = ''.join(random.choice(characters) for _ in range(length))

        # Display password
        password_display.config(text=f"Generated Password: {password}")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number greater than 0.")


# Create GUI window
window = tk.Tk()
window.title("Password Generator")
window.geometry("400x200")

# Label and Entry for length
tk.Label(window, text="Enter password length:").pack(pady=5)
length_entry = tk.Entry(window)
length_entry.pack(pady=5)

# Button to generate password
generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

# Label to display the password
password_display = tk.Label(window, text="Generated Password: ", wraplength=380)
password_display.pack(pady=10)

# Run the GUI loop
window.mainloop()
