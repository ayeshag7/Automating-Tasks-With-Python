import tkinter as tk
import random
import string

# Function to generate a random password
def generate_password():
    password_length = length_entry.get()
    
    if not password_length.isdigit():
        result_label.config(text="Password length must be a positive integer")
        return

    password_length = int(password_length)

    if password_length <= 0:
        result_label.config(text="Password length must be greater than 0")
    else:
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(password_length))
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
        result_label.config(text="Generated Password")

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Set the window size
root.geometry("400x200")  # Width x Height

# Label and entry for password length
length_label = tk.Label(root, text="Password Length:", font=("Helvetica", 14))
length_label.pack()
length_entry = tk.Entry(root)
length_entry.pack()

# Button to generate password
generate_button = tk.Button(root, text="Generate Password", command=generate_password, font=("Helvetica", 12, "bold"))
generate_button.pack()

# Label to display the generated password
result_label = tk.Label(root, text="", font=("Helvetica", 14, "bold"))
result_label.pack()

# Entry to display the generated password
password_entry = tk.Entry(root, font=("Helvetica", 10))
password_entry.pack()

# Run the GUI
root.mainloop()
