import tkinter as tk
import time
from tkinter.constants import LEFT, N, RIGHT

logged_in = {}


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.shared_data = {}

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (CandidateLogin, CandidateMenuPage, AdminLogin, TestsPage, TestsPage, AdminPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("CandidateLogin")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class CandidateLogin(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#3d3d5c')
        self.controller = controller

        self.controller.title('Mock Test Gui')
        self.controller.state('zoomed')

        heading_label = tk.Label(self, text='Candidate Login', font=(
            'orbitron', 45, 'bold'), foreground='#ffffff', background='#3d3d5c')
        heading_label.pack(pady=25)

        space_label = tk.Label(self, height=4, bg='#3d3d5c')
        space_label.pack()

        username_label = tk.Label(self, text='Enter your Username', font=(
            'orbitron', 13), bg='#3d3d5c', fg='white')
        username_label.pack(pady=10)
        my_username = tk.StringVar()

        username_entry = tk.Entry(
            self, textvariable=my_username, font=('orbitron', 12), width=22)
        username_entry.focus_set()
        username_entry.pack(ipady=7)

        password_label = tk.Label(self, text='Enter your password', font=(
            'orbitron', 13), bg='#3d3d5c', fg='white')
        password_label.pack(pady=10)

        self.my_password = tk.StringVar()
        self.password_entry_box = tk.Entry(
            self, textvariable=self.my_password, font=('orbitron', 12), width=22)
        self.password_entry_box.pack(ipady=7)

        self.password_entry_box.bind('<FocusIn>', self.handle_focus_in)
        self.incorrect_password_label = tk.Label(self, text='', font=(
            'orbitron', ), fg='white', bg='#3d3d5c', anchor='n')
        self.incorrect_password_label.pack(fill='x', pady=2)

        enter_button = tk.Button(self, text='Candidate Login', command=self.check_password,
                                 relief='raised', borderwidth=3, width=40, height=3)
        enter_button.pack(pady=10)

        admin_login_button = tk.Button(self, text='Admin Login', command=lambda: self.controller.show_frame(
            "AdminLogin"), relief='raised', borderwidth=3, width=40, height=3)
        admin_login_button.pack(pady=10, side=RIGHT)

        # bottom_frame = tk.Frame(self, relief='raised', borderwidth=3)
        # bottom_frame.pack(fill='x', side='bottom')

    def handle_focus_in(self, _):
        self.password_entry_box.configure(fg='black', show='*')

    def check_password(self):
        self.controller.show_frame('CandidateMenuPage')
        if self.my_password.get() == '123':
            self.my_password.set('')
            self.incorrect_password_label['text'] = ''
        else:
            self.incorrect_password_label['text'] = 'Incorrect Password'


class AdminLogin(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#3d3d5c')
        self.controller = controller

        self.controller.title('Mock Test Gui')
        self.controller.state('zoomed')
        #self.controller.iconphoto(False,tk.PhotoImage(file='C:/Users/urban boutique/Documents/atm tutorial/atm.png'))

        heading_label = tk.Label(self, text='Admin Login', font=(
            'orbitron', 45, 'bold'), foreground='#ffffff', background='#3d3d5c')
        heading_label.pack(pady=25)

        space_label = tk.Label(self, height=4, bg='#3d3d5c')
        space_label.pack()

        username_label = tk.Label(self, text='Enter your Username', font=(
            'orbitron', 13), bg='#3d3d5c', fg='white')
        username_label.pack(pady=10)
        my_username = tk.StringVar()

        username_entry = tk.Entry(
            self, textvariable=my_username, font=('orbitron', 12), width=22)
        username_entry.focus_set()
        username_entry.pack(ipady=7)

        password_label = tk.Label(self, text='Enter your password', font=(
            'orbitron', 13), bg='#3d3d5c', fg='white')
        password_label.pack(pady=10)

        self.my_password = tk.StringVar()
        self.password_entry_box = tk.Entry(
            self, textvariable=self.my_password, font=('orbitron', 12), width=22)
        self.password_entry_box.pack(ipady=7)

        self.password_entry_box.bind('<FocusIn>', self.handle_focus_in)

        self.incorrect_password_label = tk.Label(self, text='', font=(
            'orbitron', 13), fg='white', bg='#3d3d5c', anchor='n')
        self.incorrect_password_label.pack(fill='x', pady=2)

        admin_login_button = tk.Button(self, text='Admin Login', command=lambda: self.controller.show_frame(
            "AdminPage"), relief='raised', borderwidth=3, width=40, height=3)
        admin_login_button.pack(pady=10)
        candidate_login_button = tk.Button(self, text='Candidate Login', command=lambda: self.controller.show_frame(
            "CandidateLogin"), relief='raised', borderwidth=3, width=40, height=3)
        candidate_login_button.pack(pady=10, side=RIGHT)

        # bottom_frame = tk.Frame(self, relief='raised', borderwidth=3)
        # bottom_frame.pack(fill='x', side='bottom')

    def handle_focus_in(self, _):
        self.password_entry_box.configure(fg='black', show='*')

    def check_password(self):
        self.controller.show_frame('MenuPage')
        if self.my_password.get() == '123':
            self.my_password.set('')
            self.incorrect_password_label['text'] = ''
        else:
            self.incorrect_password_label['text'] = 'Incorrect Password'


class CandidateMenuPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#3d3d5c')
        self.controller = controller

        heading_label = tk.Label(self, text='Candidate Menu', font=(
            'orbitron', 45, 'bold'), foreground='#ffffff', background='#3d3d5c')
        heading_label.pack(pady=25)

        main_menu_label = tk.Label(self, text='Main Menu', font=(
            'orbitron', 13), fg='white', bg='#3d3d5c')
        main_menu_label.pack()

        selection_label = tk.Label(self, text='Please make a selection', font=(
            'orbitron', 13), fg='white', bg='#3d3d5c', anchor='w')
        selection_label.pack()

        button_frame = tk.Frame(self, bg='#3d3d5c')
        button_frame.pack(expand=True, anchor=N, pady=20)

        tests_btn = tk.Button(button_frame, text='Give Test', command=lambda: self.controller.show_frame(
            "TestsPage"), relief='raised', borderwidth=3, width=50, height=5)
        tests_btn.grid(row=0, column=0, pady=5)

        log_out_btn = tk.Button(button_frame, text='Log Out', command=lambda: self.controller.show_frame(
            "CandidateLogin"), relief='raised', borderwidth=3, width=50, height=5)
        log_out_btn.grid(row=3, column=0, pady=5)


class AdminPage(tk.Frame):
    '''
    
    '''
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#3d3d5c')
        self.controller = controller


class TestsPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#3d3d5c')
        self.controller = controller
        # retrieved from database
        # names here
        # subjects = []

        heading_label = tk.Label(self,
                                 text='Mock Test Portal',
                                 font=('orbitron', 45, 'bold'),
                                 foreground='#ffffff',
                                 background='#3d3d5c')
        heading_label.pack(pady=25)

        choose_amount_label = tk.Label(self,
                                       text='Choose the Subject',
                                       font=('orbitron', 13),
                                       fg='white',
                                       bg='#3d3d5c')
        choose_amount_label.pack()

        button_frame = tk.Frame(self, bg='#3d3d5c')
        button_frame.pack(fill='both', expand=True)

        maths_button = tk.Button(button_frame,
                                 text='Mathematics',
                                 # command=lambda: pass,
                                 relief='raised',
                                 borderwidth=3,
                                 width=50,
                                 height=5)
        maths_button.grid(row=0, column=0, pady=5)

        english_btn = tk.Button(button_frame,
                                text='English',
                                # command=lambda: pass,
                                relief='raised',
                                borderwidth=3,
                                width=50,
                                height=5)
        english_btn.grid(row=1, column=0, pady=5)

        geography_button = tk.Button(button_frame,
                                     text='Geography',
                                     # command=lambda: pass,
                                     relief='raised',
                                     borderwidth=3,
                                     width=50,
                                     height=5)
        geography_button.grid(row=2, column=0, pady=5)

        cs_button = tk.Button(button_frame,
                              text='Computer Sciences',
                              # command=lambda: pass,
                              relief='raised',
                              borderwidth=3,
                              width=50,
                              height=5)
        cs_button.grid(row=3, column=0, pady=5)

        physics_button = tk.Button(button_frame,
                                   text='Physics',
                                   # command=lambda: pass,
                                   relief='raised',
                                   borderwidth=3,
                                   width=50,
                                   height=5)
        physics_button.grid(row=0, column=1, pady=5, padx=555)

        chemistry_button = tk.Button(button_frame,
                                     text='Chemistry',
                                     # command=lambda: pass,
                                     relief='raised',
                                     borderwidth=3,
                                     width=50,
                                     height=5)
        chemistry_button.grid(row=1, column=1, pady=5)

        back_button = tk.Button(button_frame,
                                text='Go Back',
                                command=lambda: self.controller.show_frame(
                                    "MenuPage"),
                                relief='raised',
                                borderwidth=3,
                                width=50,
                                height=5)
        back_button.grid(row=2, column=1, pady=5)

        bottom_frame = tk.Frame(self, relief='raised', borderwidth=3)
        bottom_frame.pack(fill='x', side='bottom')


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
