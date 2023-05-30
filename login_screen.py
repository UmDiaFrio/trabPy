import tkinter as tk
from tkinter import messagebox
import database
import produto_screen

# definindo  login
class LoginScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("LOGIN")
        self.root.geometry("400x200")
        self.root.configure(bg="khaki3")
        self.root
#label // entry
        self.label_username = tk.Label(self.root, text="Username:", bg = "light cyan3", relief="groove",font= ("Helvetica", 10, "bold"))
        self.label_username.pack(pady=2)
        self.entry_username = tk.Entry(self.root,bg= "gray70", relief="solid", borderwidth=1)
        self.entry_username.pack(pady=5)

        self.label_password = tk.Label(self.root, text="Password:", bg="light cyan3", relief="groove",font= ("Helvetica", 10, "bold") )
        self.label_password.pack(pady=2)
        self.entry_password = tk.Entry(self.root, show="*", bg="gray70",relief="solid", borderwidth=1)
        self.entry_password.pack(pady=5)

        self.button_login = tk.Button(self.root, text="Login", command=self.login, bg= "OliveDrab4", font= ("Arial", 10, "bold"))
        self.button_login.pack(pady= 3)

        self.button_register = tk.Button(self.root, text="Register", command=self.register, bg="sea green", font= ("Arial", 10, "bold"))
        self.button_register.pack(pady=3,padx= 20 , side="left" )

# funcoes de login e registros
    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if database.authenticate_user(username, password):
            self.root.destroy()
            produto_screen.open_product_screen()
        else:
            messagebox.showerror("Error", "Invalid username or password")

    def register(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        if len(password) <= 8 and password.isdigit():

            if username and password:
                if database.register_user(username, password):
                    messagebox.showinfo("Registration", "User registered successfully!")
                else:
                    messagebox.showerror("Registration", "Username already exists!")
            else:
                messagebox.showerror("Registration", "Please enter a username and password")
        else:
            messagebox.showerror("Registration","Minimo de 8 numeros / Somente numeros ")


        

def open_login_screen():
    root = tk.Tk()
    login_screen = LoginScreen(root)
    root.mainloop()


if __name__ == "__main__":
    database.create_tables()
    open_login_screen()