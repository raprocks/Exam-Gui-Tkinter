# This is a Custom widget capabale of containing many frames(Sub custom widgets)
# inside a single scrollable Frame containing a parent canvas
from onefile import ExamPage
from tkinter import *
from tkinter import ttk

win = Tk()

wrap1 = Frame(win, bg="#656")
wrap2 = Frame(win, bg="#000")

can = Canvas(wrap1)

can.pack(side="left", expand=1, fill="both")
scroll = ttk.Scrollbar(wrap1, orient="vertical", command=can.yview)
scroll.pack(side="right", fill="y")

can.configure(yscrollcommand=scroll.set)

can.bind("<Configure>", lambda e: can.configure(scrollregion=can.bbox("all")))

inframe = Frame(can)
can.create_window((0, 0), window=inframe, anchor="center")
inframe.configure()
wrap1.pack(fill="both", expand=1, padx=10, pady=10)
wrap2.pack(fill="both", expand=1, padx=10, pady=10)

with open("./OS.txt") as fd:
    data = fd.read()
questions = data.split('\n\n')
for question in questions:
    split_data = question.split('\n')
    question_data = split_data[0]
    option1 = Checkbutton(inframe, text=split_data[1])
    option2 = Checkbutton(inframe, text=split_data[2])
    option3 = Checkbutton(inframe, text=split_data[3])
    option4 = Checkbutton(inframe, text=split_data[4])
    answer = split_data[5]
    question_label = Label(inframe, text=question_data)
    question_label.pack()
    option1.pack()
    option2.pack()
    option3.pack()
    option4.pack()
can.yview(MOVETO)
win.state("zoomed")
win.mainloop()
