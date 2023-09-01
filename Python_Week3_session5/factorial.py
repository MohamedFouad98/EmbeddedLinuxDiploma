import tkinter as tk


def calculate_factorial():
    try:
        n = int(entry.get())
        if n < 0:
            raise ValueError("Please enter a non-negative integer.")
        
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        
        result_label.config(text=f"The factorial of {n} is{n}!= {factorial}")
    except ValueError as e:
        tk.messagebox.showerror("Error", str(e))
    

# Create a GUI window
root = tk.Tk()
#root.geometry("262x90+350+600")
root.resizable(False,False)
root.title("Factorial Calculator")

# Create and place widgets in the window
label = tk.Label(root, text="Enter Value of integer N:")
result_label = tk.Label(root, text="")
entry = tk.Entry(root)
calculate_button = tk.Button(root, text="Validate", command=calculate_factorial,width=20)


label.grid(row=0)
entry.grid(row=0, column=1)
result_label.grid(row=2, column=1)
calculate_button.grid(row=3, column=1)

# Start the GUI event loop
root.mainloop()
