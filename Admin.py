import tkinter as tk

class AdminView(tk.Frame):
    def __init__(self, master, controller, *args, **kwargs):
        super().__init__(master=master, *args, **kwargs)
        # internal widgets
        self.controller = controller
        self.controller.title("Admin Login")
        self.controller.state('zoomed')

        banner_label = tk.Label(text="ADMIN PANEL")
        banner_label.pack(pady=25)

        self.username = tk.Entry()
        self.username.pack()
        