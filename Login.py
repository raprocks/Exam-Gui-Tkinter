import tkinter as tk
from tkinter.constants import BOTTOM, E, W
import bcrypt


class LoginView(tk.Frame):
    def __init__(self, master, controller, *args, **kwargs):
        super().__init__(master=master, *args, **kwargs)
        # internal widgets
        self.controller = controller
        # username
        self.username_label = tk.Label(text="Username")
        self.username_label.pack(side='left')
        self.username = tk.Entry()
        self.username.pack(side='right')
        # password
        self.password_label = tk.Label(text="Password")
        self.password_label.pack(side='left')
        self.password = tk.Entry()
        self.password.pack(side='right')
        self.btn_login = tk.Button(text="Login", command=self.login)
        self.btn_login.pack(side='bottom', padx=30)

    def login(self) -> None:
        self.controller.show_frame("AdminView")
        username = self.username.get()
        password = self.password.get()
        print(username, password)
        # password_hash_db = self.get_pass_hash(username)
        # salt = bcrypt.gensalt(rounds=4)
        # pass_hash = bcrypt.hashpw(password, salt)

    def get_pass_hash(self, username: str):
        GET_PASS_HASH_TABLE = f"""SELECT password from USERS
        WHERE username LIKE '{username}'"""

        # get pass hash here from db
