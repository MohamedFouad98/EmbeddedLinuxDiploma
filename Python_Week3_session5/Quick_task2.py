import tkinter as tk
result=0
def add():
    global result
    num1 = float(num1_entry.get())
    num2 = float(num2_entry.get())
    addition=num1 + num2
    result = f'the add is : {num1} + {num2} = {addition}'
    
def sub():
    global result
    
    num1 = float(num1_entry.get())
    num2 = float(num2_entry.get())
    subtraction=num1 - num2
    result = f'the sub is : {num1} - {num2} = {subtraction}'
    
def show():
    global result
    result_label.config(text=result)
# create the main window
root = tk.Tk()

 
# create the widgets
num1_label = tk.Label(root, text="Number 1:")
num1_entry = tk.Entry(root)
num2_label = tk.Label(root, text="Number 2:")
num2_entry = tk.Entry(root)
add_button = tk.Button(root, text="Add", command=add)
sub_button = tk.Button(root, text="Sub", command=sub)
button = tk.Button(root, text="Validate", command=show)
result_label = tk.Label(root, text="Result:")
 
# layout the widgets
num1_label.grid(row=0, column=0, sticky="e")
num1_entry.grid(row=0, column=1)
num2_label.grid(row=1, column=0, sticky="e")
num2_entry.grid(row=1, column=1)
result_label.grid(row=2, column=1, columnspan=2,pady=10)
add_button.grid(row=2, column=0)
sub_button.grid(row=3, column=0)
button.grid(row=3, column=1, columnspan=2, pady=10)
 
# run the main loop
root.mainloop()