import tkinter as tk
from tkinter.constants import LEFT, N, RIGHT, X
import sqlite3
from tkinter import ttk, Scrollbar, filedialog, messagebox
from db_utils import *
logged_in = {}

DB = sqlite3.connect("./data.db")
create_tables(DB)


class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.shared_data = {}

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        Frames = [CandidateLogin, CandidateMenuPage, AdminLogin, TestsPage,
                  TestsPage, AdminMenuPage, AddCoursePage, AddUserPage]
        for F in Frames:
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")
        for sub in get_subjects(DB):
            page_name = sub[1]+"Page"
            frame = ExamPage(subject=sub, parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")
        print(self.frames)
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
        self.user_var = tk.StringVar()

        username_entry = tk.Entry(
            self, textvariable=self.user_var, font=('orbitron', 12), width=22)
        username_entry.focus_set()
        username_entry.pack(ipady=7)

        password_label = tk.Label(self, text='Enter your password', font=(
            'orbitron', 13), bg='#3d3d5c', fg='white')
        password_label.pack(pady=10)

        self.password_var = tk.StringVar()
        self.password_entry_box = tk.Entry(
            self, textvariable=self.password_var, font=('orbitron', 12), width=22)
        self.password_entry_box.pack(ipady=7)

        self.password_entry_box.bind('<FocusIn>', self.handle_focus_in)
        self.incorrect_password_label = tk.Label(self, text='', font=(
            'orbitron', ), fg='white', bg='#3d3d5c', anchor='n')
        self.incorrect_password_label.pack(fill='x', pady=2)

        enter_button = tk.Button(self, text='Candidate Login', command=self.verify,
                                 relief='raised', borderwidth=3, width=40, height=3)
        enter_button.pack(pady=10)

        admin_login_button = tk.Button(self, text='Admin Login', command=lambda: self.controller.show_frame(
            "AdminLogin"), relief='raised', borderwidth=3, width=40, height=3)
        admin_login_button.pack(pady=10, side=RIGHT)

    def verify(self):
        print("verifying")
        self.controller.show_frame("CandidateMenuPage")
        # if check_user(DB, self.user_var.get(), self.password_var.get()):
        # else:
        #     self.incorrect_password_label['text'] = 'Incorrect Password'

    def handle_focus_in(self, _):
        self.password_entry_box.configure(fg='black', show='*')


class AdminLogin(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#3d3d5c')
        self.controller = controller

        self.controller.title('Mock Test Gui')
        self.controller.state('zoomed')

        heading_label = tk.Label(self, text='Admin Login', font=(
            'orbitron', 45, 'bold'), foreground='#ffffff', background='#3d3d5c')
        heading_label.pack(pady=25)

        space_label = tk.Label(self, height=4, bg='#3d3d5c')
        space_label.pack()

        username_label = tk.Label(self, text='Enter your Username', font=(
            'orbitron', 13), bg='#3d3d5c', fg='white')
        username_label.pack(pady=10)
        self.username_var = tk.StringVar()

        username_entry = tk.Entry(
            self, textvariable=self.username_var, font=('orbitron', 12), width=22)
        username_entry.focus_set()
        username_entry.pack(ipady=7)

        password_label = tk.Label(self, text='Enter your password', font=(
            'orbitron', 13), bg='#3d3d5c', fg='white')
        password_label.pack(pady=10)

        self.password_var = tk.StringVar()
        self.password_entry_box = tk.Entry(
            self, textvariable=self.password_var, font=('orbitron', 12), width=22)
        self.password_entry_box.pack(ipady=7)

        self.password_entry_box.bind('<FocusIn>', self.handle_focus_in)

        self.incorrect_password_label = tk.Label(self, text='', font=(
            'orbitron', 13), fg='white', bg='#3d3d5c', anchor='n')
        self.incorrect_password_label.pack(fill='x', pady=2)

        admin_login_button = tk.Button(
            self, text='Admin Login', command=self.verify, relief='raised', borderwidth=3, width=40, height=3)
        admin_login_button.pack(pady=10)
        candidate_login_button = tk.Button(
            self, text='Candidate Login', command=lambda: self.controller.show_frame("CandidateLogin"), relief='raised', borderwidth=3, width=40, height=3)
        candidate_login_button.pack(pady=10, side=RIGHT)

        # bottom_frame = tk.Frame(self, relief='raised', borderwidth=3)
        # bottom_frame.pack(fill='x', side='bottom')

    def handle_focus_in(self, _):
        self.password_entry_box.configure(fg='black', show='*')

    def verify(self):
        print("verifying")
        self.controller.show_frame("AdminMenuPage")
        if check_user(DB, self.username_var.get(), self.password_var.get()):
            if get_user(DB, username=self.username_var.get())[-1] == 1:
                self.controller.show_frame("AdminMenuPage")
            else:
                self.incorrect_password_label['text'] = 'You are a Candidate!'
        else:
            self.incorrect_password_label['text'] = 'Incorrect Username or Password'


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


class AdminMenuPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#3d3d5c')
        self.controller = controller

        button_frame = tk.Frame(self, bg='#3d3d5c')
        button_frame.pack(expand=True, anchor=N, pady=20)

        tests_btn = tk.Button(button_frame, text='Add Courses', command=lambda: self.controller.show_frame(
            "AddCoursePage"), relief='raised', borderwidth=3, width=50, height=5)
        tests_btn.grid(row=0, column=0, pady=5)

        tests_btn = tk.Button(button_frame, text='Add Questions', command=lambda: self.controller.show_frame(
            "QuestionAddPage"), relief='raised', borderwidth=3, width=50, height=5)
        tests_btn.grid(row=3, column=0, pady=5)

        tests_btn = tk.Button(button_frame, text='Results', command=lambda: self.controller.show_frame(
            "ResultsPage"), relief='raised', borderwidth=3, width=50, height=5)
        tests_btn.grid(row=6, column=0, pady=5)

        tests_btn = tk.Button(button_frame, text='Manage Users', command=lambda: self.controller.show_frame(
            "AddUserPage"), relief='raised', borderwidth=3, width=50, height=5)
        tests_btn.grid(row=9, column=0, pady=5)

        log_out_btn = tk.Button(button_frame, text='Log Out', command=lambda: self.controller.show_frame(
            "AdminLogin"), relief='raised', borderwidth=3, width=50, height=5)
        log_out_btn.grid(row=12, column=0, pady=5)


class TestsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#3d3d5c')
        self.controller = controller
        # retrieved from database
        # names here
        subjects = {}

        heading_label = tk.Label(self, text='Mock Test Portal', font=(
            'orbitron', 45, 'bold'), foreground='#ffffff', background='#3d3d5c')
        heading_label.pack(pady=25)

        choose_sub_label = tk.Label(self, text='Choose the Subject', font=(
            'orbitron', 13), fg='white', bg='#3d3d5c')
        choose_sub_label.pack()
        button_frame = tk.Frame(self, bg='#3d3d5c')
        button_frame.pack(fill='both', expand=True)
        myscrollbar = Scrollbar(button_frame, orient="vertical")
        myscrollbar.pack(side="right", fill="y")

        for sub in get_subjects(DB):
            page_name = sub[1]+"Page"
            subjects[sub[1]] = tk.Button(button_frame, text=sub[1], command=lambda: self.controller.show_frame(page_name),
                                         relief='raised', borderwidth=3, width=50, height=5)

        for sub in subjects.keys():
            subjects[sub].pack(padx=5, pady=5)
        bottom_frame = tk.Frame(self, relief='raised', borderwidth=3)
        bottom_frame.pack(fill='x', side='bottom')

        back_button = tk.Button(self, text='Go Back', command=lambda: self.controller.show_frame(
            "CandidateMenuPage"), relief='raised', borderwidth=3, width=50, height=5)
        back_button.pack(pady=5)


class AddCoursePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#3d3d5c')
        self.controller = controller
        CN_label = tk.Label(self, text='Enter Course Name', font=(
            'orbitron', 13), bg='#3d3d5c', fg='white')
        CN_label.pack(pady=10)
        self.my_coursename = tk.StringVar()

        CN_entry = tk.Entry(
            self, textvariable=self.my_coursename, font=('orbitron', 12), width=22)
        CN_entry.focus_set()
        CN_entry.pack(ipady=7)

        sub_btn = tk.Button(self, text="Choose Question file",
                            command=self.open_file, pady=10, padx=20)
        sub_btn.pack(ipady=10)

        ac_button = tk.Button(self, text='Add Course', command=self.add_subject,
                              relief='raised', borderwidth=3, width=40, height=3)
        ac_button.pack(pady=10)

        goback_button = tk.Button(self, text='Go Back', command=lambda: self.controller.show_frame("AdminMenuPage"),
                                  relief='raised', borderwidth=3, width=40, height=3)
        goback_button.pack(pady=10, side=RIGHT)

    def open_file(self):
        file_opened = filedialog.askopenfile(initialdir="./")
        self.sub_file = file_opened.name
        print(self.sub_file)
        file_opened.close()

    def add_subject(self):
        print("adding sub")
        add_subject(DB, self.my_coursename.get(), self.sub_file)
        messagebox.showinfo(
            "ADDED SUBJECT", f"subject {self.my_coursename.get()} has been added and question file is {self.sub_file}")
        self.my_coursename.set("")


class ExamPage(tk.Frame):
    def __init__(self, subject, parent, controller):
        tk.Frame.__init__(self, parent, bg='#3d3d5c')
        self.controller = controller
        self.subject = subject
        question_file = subject[2]
        print(subject)
        heading_label = tk.Label(self, text=subject[1]+" Test Page", font=(
            'orbitron', 45, 'bold'), foreground='#ffffff', background='#3d3d5c')
        heading_label.pack(pady=25)

        wrap = tk.LabelFrame(self, height=5)

        canvas = tk.Canvas(wrap, bg='#111', height=5,
                           scrollregion=(0, 0, 1000, 1000))
        canvas.pack(fill="both", expand=True)
        myscrollbar = ttk.Scrollbar(
            wrap, orient="vertical", command=canvas.yview)

        canvas.configure(yscrollcommand=myscrollbar.set)
        question_frame = tk.Frame(canvas, bg='#3d3d5c')
        question_dict = {}
        with open(question_file) as fd:
            data = fd.read()
        questions = data.split('\n\n')
        for question in questions:
            split_data = question.split('\n')
            question_data = split_data[0]
            option1 = tk.Radiobutton(question_frame, text=split_data[1])
            option2 = tk.Radiobutton(question_frame, text=split_data[2])
            option3 = tk.Radiobutton(question_frame, text=split_data[3])
            option4 = tk.Radiobutton(question_frame, text=split_data[4])
            answer = split_data[5]
            question_label = tk.Label(question_frame, text=question_data, font=(
                'orbitron', 13), fg='white', bg='#3d3d5c')
            question_label.pack()
            option1.pack()
            option2.pack()
            option3.pack()
            option4.pack()
        canvas.create_window((0, 0), window=question_frame, anchor="nw")
        myscrollbar.pack(side="right", fill="y")
        question_frame.pack()
        wrap.pack(fill='both', expand=True, padx=20, pady=20)

        # for sub in get_subjects(DB):

        back_button = tk.Button(self, text='Go Back', command=lambda: self.controller.show_frame(
            "CandidateMenuPage"), relief='raised', borderwidth=3, width=50, height=5)
        back_button.pack(pady=5)

    def get_questions(self):
        pass


class AddUserPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#3d3d5c')
        self.controller = controller
        heading_label = tk.Label(self, text='Manage Users', font=(
            'orbitron', 45, 'bold'), foreground='#ffffff', background='#3d3d5c')
        heading_label.pack(pady=25)
        heading_label = tk.Label(self, text='Add Users', font=(
            'orbitron', 25, 'bold'), foreground='#ffffff', background='#3d3d5c')
        heading_label.pack(pady=5)
        newusername_label = tk.Label(self, text='Enter a Username', font=(
            'orbitron', 13), bg='#3d3d5c', fg='white')
        newusername_label.pack(pady=10)
        self.username = tk.StringVar()

        newusername_entry = tk.Entry(
            self, textvariable=self.username, font=('orbitron', 12), width=22)
        newusername_entry.focus_set()
        newusername_entry.pack(ipady=7)

        password_label = tk.Label(self, text="Choose Password", font=(
            'orbitron', 13), bg='#3d3d5c', fg='white')
        password_label.pack(pady=10)
        self.password = tk.StringVar()

        self.password_entry = tk.Entry(
            self, textvariable=self.password, font=('orbitron', 12), width=22)
        self.password_entry.focus_set()
        self.password_entry.bind('<FocusIn>', self.handle_focus_in)
        self.password_entry.pack(ipady=7)
        self.admin = tk.BooleanVar()
        admin_check = tk.Checkbutton(
            self, text="Admin", variable=self.admin, bg="#3d3d5c")
        admin_check.pack(ipadx=8)

        add_user_btn = tk.Button(self, text='Add User', command=self.add,
                                 relief='raised', borderwidth=3, width=40, height=3)
        add_user_btn.pack(pady=10)

        heading_label = tk.Label(self, text='Remove Users', font=(
            'orbitron', 25, 'bold'), foreground='#ffffff', background='#3d3d5c')
        heading_label.pack(pady=5)
        self.remove_user = tk.StringVar()
        newusername_label = tk.Label(self, text='Enter a Username', font=(
            'orbitron', 13), bg='#3d3d5c', fg='white')
        newusername_label.pack(pady=10)
        remove_user_entry = tk.Entry(
            self, textvariable=self.remove_user, font=('orbitron', 12), width=22)

        remove_user_entry.pack(ipady=7)

        remove_user_btn = tk.Button(self, text='Remove User', command=self.remove,
                                    relief='raised', borderwidth=3, width=40, height=3)
        remove_user_btn.pack(pady=20)

        back_btn = tk.Button(self, text='Go Back', command=lambda: self.controller.show_frame("AdminMenuPage"),
                             relief='raised', borderwidth=3, width=40, height=3)
        back_btn.pack(pady=10, side=RIGHT)

    def handle_focus_in(self, _):
        self.password_entry.configure(fg='black', show='*')

    def add(self):
        print("adding user")
        add_user(DB, self.username.get(),
                 self.password.get(), self.admin.get())

    def remove(self):
        print("Removing User!")
        remove_user(DB, self.remove_user.get())


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
