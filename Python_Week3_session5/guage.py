import tkinter as tk
import math

def draw_gauge(canvas, value):
    canvas.delete("all")  # Clear the canvas

    center_x = canvas.winfo_width() / 2  # Calculate center based on canvas size
    center_y = canvas.winfo_height() / 2
    radius = 100

    

    # Draw the gauge arc with indicator lines
    start_angle = 135
    end_angle = 45
    angle_range = end_angle - start_angle
    value_angle = start_angle + (angle_range * value / 100)

    if value <= 50:
        color = "green"
    elif value <= 75:
        color = "yellow"
    else:
        color = "red"

    canvas.create_arc(center_x - radius, center_y - radius, center_x + radius, center_y + radius,
                      start=start_angle, extent=angle_range, style=tk.ARC, outline=color, width=10)

    

    # Draw the main indicator line
    indicator_length = radius - 10
    indicator_x = center_x + indicator_length * math.cos(math.radians(value_angle))
    indicator_y = center_y - indicator_length * math.sin(math.radians(value_angle))
    canvas.create_line(center_x, center_y, indicator_x, indicator_y, fill="black", width=3)

    # Draw the header
    canvas.create_text(center_x, center_y - radius - 40, text="Humidity",
                       font=("Arial", 20, "italic bold"), fill="black")

    # Draw the live percentage display
    canvas.create_text(center_x, center_y, text=f"{value}%",
                       font=("Arial", 20), fill="black")

def update_gauge(value):
    value_var.set(value)
    draw_gauge(canvas, value)

def on_scale_change(event):
    value = int(scale.get())
    update_gauge(value)

# Create a GUI window
root = tk.Tk()
root.title("Humidity Gauge")

# Create a canvas for the gauge
canvas = tk.Canvas(root, width=300, height=300)
# Create a scale to adjust the value
value_var = tk.StringVar()
scale = tk.Scale(root, from_=0, to=100, variable=value_var, orient=tk.HORIZONTAL, command=on_scale_change)
# Center the gauge

canvas.bind("<Configure>", lambda event: draw_gauge(canvas, int(value_var.get())))
canvas.pack()
scale.pack()
# Draw the initial gauge
draw_gauge(canvas, 0)

# Start the GUI event loop
root.mainloop()
