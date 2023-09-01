import tkinter

master=tkinter.Tk()



button1=tkinter.Button(master, text="button1")
button2=tkinter.Button(master, text="button2")
button3=tkinter.Button(master, text="button3")
button4=tkinter.Button(master, text="button4")

button1.grid(row=0,column=1)
button2.grid(row=1,column=0)
button3.grid(row=1,column=2)
button4.grid(row=2,column=1)
master.mainloop()