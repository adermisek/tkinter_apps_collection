import tkinter as tk

# Main application
root = tk.Tk()
root.title("Freehand Drawing with Color Change and Erasing")

# Create a canvas with dimensions 500x400 and a white background
canvas = tk.Canvas(root, width=500, height=400, bg="white")
canvas.pack()

# Variable to store the selected color
color_var = tk.StringVar(value="black")  # Default color is black

# Function to draw a line with the selected color
def draw(event):
    canvas.create_line(event.x, event.y, event.x+1, event.y+1, fill=color_var.get(), width=2)

# Bind mouse drag event (left click) to drawing function
canvas.bind("<B1-Motion>", draw)

# Function to set the color to red
def set_red():
    color_var.set("red")

# Function to set the color to blue
def set_blue():
    color_var.set("blue")

# Function to clear all elements on the canvas
def clear_canvas():
    canvas.delete("all")

# Create a frame for the RadioButtons
color_frame = tk.Frame(root)
color_frame.pack(pady=10)

# Add RadioButtons to change color (only red and blue)
red_button = tk.Radiobutton(color_frame, text="Red", variable=color_var, value="red", command=set_red)
red_button.pack(side=tk.LEFT, padx=5)

blue_button = tk.Radiobutton(color_frame, text="Blue", variable=color_var, value="blue", command=set_blue)
blue_button.pack(side=tk.LEFT, padx=5)

# Add a button to clear the canvas
clear_button = tk.Button(root, text="Clear", command=clear_canvas)
clear_button.pack(pady=10)

# Run the main loop
root.mainloop()
