import tkinter as tk
import string
import random

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        self.length_label = tk.Label(root, text="Password Length:")
        self.length_label.pack()

        self.length_entry = tk.Entry(root)
        self.length_entry.pack()

        self.complexity_label = tk.Label(root, text="Password Complexity:")
        self.complexity_label.pack()

        self.complexity_var = tk.StringVar()
        self.complexity_var.set("Easy")
        self.complexity_menu = tk.OptionMenu(root, self.complexity_var, "Easy", "Medium", "Hard")
        self.complexity_menu.pack()

        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.pack()

        self.password_label = tk.Label(root, text="")
        self.password_label.pack()

    def generate_password(self):
        password_length = int(self.length_entry.get())
        complexity = self.complexity_var.get()

        if complexity == "Easy":
            characters = string.ascii_letters + string.digits
        elif complexity == "Medium":
            characters = string.ascii_letters + string.digits + string.punctuation
        elif complexity == "Hard":
            characters = string.ascii_letters + string.digits + string.punctuation

        generated_password = ''.join(random.choice(characters) for _ in range(password_length))
        self.password_label.config(text="Generated Password: " + generated_password)

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
