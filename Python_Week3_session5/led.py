import tkinter as tk

def led_on():
    label_text='LED is on'
    my_canvas.itemconfig(my_oval, fill="red")  # Fill the circle with RED
    label_var.set(label_text)  # Updating the label

def led_off():
    label_text='LED is off'
    my_canvas.itemconfig(my_oval, fill="white") # Fill the circle with White
    label_var.set(label_text)  # Updating the label


root = tk.Tk()  # Set Tk instance
my_canvas = tk.Canvas(root, width=200, height=200)  # Create 200x200 Canvas widget
my_oval = my_canvas.create_oval(50, 50, 100, 100)  # Create a circle on the Canvas
label_var = tk.StringVar()  # Set the string variable for Label widget
my_label = tk.Label(root, textvariable=label_var)  # Set the LAbel widget
my_button = tk.Button(root, text="LED ON", command=led_on)  # Set a "LED ON buttom". The "led_on" function is a call-back.
my_button2 = tk.Button(root, text="LED OFF", command=led_off)# Set a "LED OFF buttom". The "led_off" function is a call-back.

my_canvas.pack()
my_label.pack()
my_button.pack()
my_button2.pack()

root.mainloop()