import tkinter as tk
import time

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
        for F in (StartPage, MenuPage, TestsPage, TestsPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#3d3d5c')
        self.controller = controller

        self.controller.title('Mock Test Gui')
        self.controller.state('zoomed')
        #self.controller.iconphoto(False,tk.PhotoImage(file='C:/Users/urban boutique/Documents/atm tutorial/atm.png'))

        heading_label = tk.Label(self,
                                 text='MOCK TEST',
                                 font=('orbitron', 45, 'bold'),
                                 foreground='#ffffff',
                                 background='#3d3d5c')
        heading_label.pack(pady=25)

        space_label = tk.Label(self, height=4, bg='#3d3d5c')
        space_label.pack()

        username_label = tk.Label(self,
                                  text='Enter your Username',
                                  font=('orbitron', 13),
                                  bg='#3d3d5c',
                                  fg='white')
        username_label.pack(pady=10)
        my_username = tk.StringVar()

        username_entry = tk.Entry(self,
                                  textvariable=my_username,
                                  font=('orbitron', 12),
                                  width=22)
        username_entry.focus_set()
        username_entry.pack(ipady=7)

        password_label = tk.Label(self,
                                  text='Enter your password',
                                  font=('orbitron', 13),
                                  bg='#3d3d5c',
                                  fg='white')
        password_label.pack(pady=10)

        my_password = tk.StringVar()
        password_entry_box = tk.Entry(self,
                                      textvariable=my_password,
                                      font=('orbitron', 12),
                                      width=22)
        password_entry_box.pack(ipady=7)

        def handle_focus_in(_):
            password_entry_box.configure(fg='black', show='*')

        password_entry_box.bind('<FocusIn>', handle_focus_in)

        def check_password():
            if my_password.get() == '123':
                my_password.set('')
                incorrect_password_label['text'] = ''
                controller.show_frame('MenuPage')
            else:
                incorrect_password_label['text'] = 'Incorrect Password'

        enter_button = tk.Button(self,
                                 text='Enter',
                                 command=check_password,
                                 relief='raised',
                                 borderwidth=3,
                                 width=40,
                                 height=3)
        enter_button.pack(pady=10)

        incorrect_password_label = tk.Label(self,
                                            text='',
                                            font=('orbitron', 13),
                                            fg='white',
                                            bg='#33334d',
                                            anchor='n')
        incorrect_password_label.pack(fill='both', expand=True)

        # bottom_frame = tk.Frame(self, relief='raised', borderwidth=3)
        # bottom_frame.pack(fill='x', side='bottom')


class MenuPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#3d3d5c')
        self.controller = controller

        heading_label = tk.Label(self,
                                 text='Mock Test Portal',
                                 font=('orbitron', 45, 'bold'),
                                 foreground='#ffffff',
                                 background='#3d3d5c')
        heading_label.pack(pady=25)

        main_menu_label = tk.Label(self,
                                   text='Main Menu',
                                   font=('orbitron', 13),
                                   fg='white',
                                   bg='#3d3d5c')
        main_menu_label.pack()

        selection_label = tk.Label(self,
                                   text='Please make a selection',
                                   font=('orbitron', 13),
                                   fg='white',
                                   bg='#3d3d5c',
                                   anchor='w')
        selection_label.pack(fill='x')

        button_frame = tk.Frame(self, bg='#33334d')
        button_frame.pack(fill='both', expand=True)

        def give_test():
            controller.show_frame('TestsPage')

        tests_btn = tk.Button(button_frame,
                                    text='Give Test',
                                    command=give_test,
                                    relief='raised',
                                    borderwidth=3,
                                    width=50,
                                    height=5)
        tests_btn.grid(row=0, column=0, pady=5)

        def admin_panel():
            controller.show_frame('AdminPage')

        admin_btn = tk.Button(button_frame,
                                   text='Admin Panel',
                                   command=admin_panel,
                                   relief='raised',
                                   borderwidth=3,
                                   width=50,
                                   height=5)
        admin_btn.grid(row=1, column=0, pady=5)

        def exit():
            controller.show_frame('StartPage')

        log_out_btn = tk.Button(button_frame,
                                text='Log Out',
                                command=exit,
                                relief='raised',
                                borderwidth=3,
                                width=50,
                                height=5)
        log_out_btn.grid(row=3, column=0, pady=5)

        bottom_frame = tk.Frame(self, relief='raised', borderwidth=3)
        bottom_frame.pack(fill='x', side='bottom')


class TestsPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#3d3d5c')
        self.controller = controller

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

        button_frame = tk.Frame(self, bg='#33334d')
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

        bottom_frame = tk.Frame(self, relief='raised', borderwidth=3)
        bottom_frame.pack(fill='x', side='bottom')

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
