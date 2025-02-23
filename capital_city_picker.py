import tkinter as tk
from tkinter import ttk

def on_check():
    # Retrieve all selected countries and display their capitals
    selected_capitals = [countries[country] for country, var in check_vars.items() if var.get()]
    label.config(text=", ".join(selected_capitals) if selected_capitals else "No selected countries")

# Main window
root = tk.Tk()
root.title("Country Selector")
root.geometry("300x250")
root.configure(bg="lightgray")

# Dictionary of countries and their capitals
countries = {
    "Croatia": "Zagreb",
    "Spain": "Madrid",
    "Italy": "Rome",
    "England": "London",
    "Norway": "Oslo"
}

# Container for checkboxes
frame = ttk.LabelFrame(root, text="Select Countries", padding=10)
frame.pack(padx=10, pady=10, fill="both", expand=True)

# Dictionary to store checkbutton variables
check_vars = {}

# Create checkbuttons for each country
for country in countries:
    var = tk.IntVar()
    check_vars[country] = var
    ttk.Checkbutton(frame, text=country, variable=var, command=on_check).pack(anchor="w")

# Label to display selected capitals
label = ttk.Label(root, text="No selected countries", background="lightgray", font=("Arial", 12, "bold"))
label.pack(pady=10)

# Run application
root.mainloop()
