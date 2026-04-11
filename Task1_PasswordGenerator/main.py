import tkinter as tk
from tkinter import messagebox
import random
import string
def generate_password():
    try:
        length = int(entry_length.get())

        characters = ""

        if var_upper.get():
            characters += string.ascii_uppercase
        if var_lower.get():
            characters += string.ascii_lowercase
        if var_digits.get():
            characters += string.digits
        if var_symbols.get():
            characters += string.punctuation

        if characters == "":
            messagebox.showerror("Error", "Select at least one character type!")
            return

        password = ''.join(random.choice(characters) for _ in range(length))
        result_var.set(password)

        if length < 6:
            strength = "Weak"
        elif length < 10:
            strength = "Medium"
        else:
            strength = "Strong"

        strength_var.set("Strength: " + strength)

    except ValueError:
        messagebox.showerror("Error", "Enter a valid number!")

def copy_password():
    password = result_var.get()
    if password == "":
        messagebox.showwarning("Warning", "Generate a password first!")
        return

    root.clipboard_clear()
    root.clipboard_append(password)
    root.update()
    messagebox.showinfo("Copied", "Password copied to clipboard!")


root = tk.Tk()
root.title("Password Generator")
root.geometry("400x400")
root.config(bg="#1e1e1e")

tk.Label(root, text="Password Generator", font=("Arial", 16, "bold"),
         fg="white", bg="#1e1e1e").pack(pady=10)

tk.Label(root, text="Password Length:", fg="white", bg="#1e1e1e").pack()
entry_length = tk.Entry(root)
entry_length.pack(pady=5)

var_upper = tk.BooleanVar()
var_lower = tk.BooleanVar()
var_digits = tk.BooleanVar()
var_symbols = tk.BooleanVar()

tk.Checkbutton(root, text="Uppercase (A-Z)", variable=var_upper,
               bg="#1e1e1e", fg="white", selectcolor="#333").pack(anchor='w', padx=50)

tk.Checkbutton(root, text="Lowercase (a-z)", variable=var_lower,
               bg="#1e1e1e", fg="white", selectcolor="#333").pack(anchor='w', padx=50)

tk.Checkbutton(root, text="Digits (0-9)", variable=var_digits,
               bg="#1e1e1e", fg="white", selectcolor="#333").pack(anchor='w', padx=50)

tk.Checkbutton(root, text="Symbols (!@#$)", variable=var_symbols,
               bg="#1e1e1e", fg="white", selectcolor="#333").pack(anchor='w', padx=50)

tk.Button(root, text="Generate Password", command=generate_password,
          bg="#4CAF50", fg="white").pack(pady=10)

result_var = tk.StringVar()
tk.Entry(root, textvariable=result_var, width=30, font=("Arial", 12)).pack(pady=5)

strength_var = tk.StringVar()
tk.Label(root, textvariable=strength_var, fg="yellow", bg="#1e1e1e",
         font=("Arial", 10, "bold")).pack(pady=5)

tk.Button(root, text="Copy to Clipboard", command=copy_password,
          bg="#2196F3", fg="white").pack(pady=10)

root.mainloop()
