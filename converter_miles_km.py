import tkinter as tk
from tkinter import StringVar

def convert():
    try:
        value = float(entry.get())
        if conversion_var.get() == "km_to_miles":
            result.set(f"{value} km = {value * 0.621371:.4f} miles")
        else:
            result.set(f"{value} miles = {value / 0.621371:.4f} km")
        result_label.config(bg="white")  
    except ValueError:
        result.set("Please enter a valid number!")
        result_label.config(bg="blue")  

# Create main window
root = tk.Tk()
root.title("KM <-> Miles Converter")
root.geometry("300x200")
root.configure(bg="blue")

# Variables
conversion_var = StringVar(value="km_to_miles")
result = StringVar()

# Input field
entry = tk.Entry(root)
entry.pack(pady=10)

# Radio buttons
frame = tk.Frame(root, bg="blue")
kmtom_rb = tk.Radiobutton(frame, text="km -> miles", variable=conversion_var, value="km_to_miles", bg="white", font=("Arial",12,"bold"))
mtokm_rb = tk.Radiobutton(frame, text="miles -> km", variable=conversion_var, value="miles_to_km", bg="white", font=("Arial",12,"bold"))
kmtom_rb.pack(side=tk.LEFT)
mtokm_rb.pack(side=tk.RIGHT)
frame.pack(padx=10)

# Convert button
convert_button = tk.Button(root, text="Convert", command=convert, bg="black", fg="green")
convert_button.pack(pady=10)

# Display result
result_label = tk.Label(root, textvariable=result, font=("Arial",12,"bold"), bg="blue")
result_label.pack()

# Run application
root.mainloop()
