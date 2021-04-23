import tkinter as tk

class RegisterView(tk.Frame):
    def __init__(self, master, controller, *args, **kwargs):
        super().__init__(master=master, *args, **kwargs)
        # internal widgets
        self.controller = controller
        