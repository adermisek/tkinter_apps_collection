from tkinter import Tk, Canvas, Radiobutton, IntVar

# Function to draw a circle
def draw_circle(event):
    x, y = event.x, event.y
    canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill='blue', outline='black')

# Function to draw a rectangle
def draw_rectangle(event):
    x, y = event.x, event.y
    canvas.create_rectangle(x - 30, y - 20, x + 30, y + 20, fill='green', outline='black')

# Function that calls the appropriate drawing function based on the selected shape
def on_click(event):
    if shape_var.get() == 1:  # If "Circle" is selected
        draw_circle(event)
    elif shape_var.get() == 2:  # If "Rectangle" is selected
        draw_rectangle(event)

# Create main window
root = Tk()
root.title("Shape Drawing")

# Variable to store the selected shape
shape_var = IntVar()
shape_var.set(1)  # Default selection is "Circle"

# Create radio buttons for shape selection
radio_circle = Radiobutton(root, text="Circle", variable=shape_var, value=1)
radio_circle.pack()
radio_rectangle = Radiobutton(root, text="Rectangle", variable=shape_var, value=2)
radio_rectangle.pack()

# Create canvas for drawing
canvas = Canvas(root, width=400, height=400, bg='white')
canvas.pack()

# Bind left mouse click to on_click function
canvas.bind("<Button-1>", on_click)

# Run the application
root.mainloop()
