from tkinter import *

startingWin = Tk()

canvas = Canvas(startingWin, height=600)
canvas.grid(row=0, column=0, sticky="nsew")
canvasFrame = Frame(canvas)
canvas.create_window(0, 0, window=canvasFrame, anchor='nw')

canvasFrame.bind("<Configure>", lambda event: canvas.configure(
    scrollregion=canvas.bbox("all")))
for i in range(70):
    element = Button(canvasFrame, text='Button %s ' % i)
    element.grid(row=i, column=0)

yscrollbar = Scrollbar(startingWin, orient=VERTICAL)
yscrollbar.config(command=canvas.yview)
canvas.config(yscrollcommand=yscrollbar.set)
yscrollbar.grid(row=0, column=1, sticky="ns")


canvas.yview_moveto(0.5)

startingWin.mainloop()
