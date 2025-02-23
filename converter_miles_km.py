import tkinter as tk
from tkinter import StringVar

def convert():
    try:
        value = float(entry.get())
        if conversion_var.get() == "km_to_milje":
            result.set(f"{value} km = {value * 0.621371:.4f} milja")
        else:
            result.set(f"{value} milja = {value / 0.621371:.4f} km")
    except ValueError:
        result.set("Unesite valjani broj!")

# Kreiranje glavnog prozora
root = tk.Tk()
root.title("Konverter km <-> milje")
root.geometry("300x200")
root.configure(bg="blue")

# Varijable
conversion_var = StringVar(value="km_to_milje")
result = StringVar()

# Unos vrijednosti
entry = tk.Entry(root)
entry.pack(pady=10)

# Radio gumbi
frame = tk.Frame(root, bg="blue")
kmtom_rb = tk.Radiobutton(frame, text="km -> milje", variable=conversion_var, value="km_to_milje", bg="white", font=("Arial",12,"bold"))
mtokm_rb = tk.Radiobutton(frame, text="milje -> km", variable=conversion_var, value="milje_to_km", bg="white",font=("Arial",12,"bold"))
kmtom_rb.pack(side=tk.LEFT)
mtokm_rb.pack(side=tk.RIGHT)
frame.pack(padx=10)

# Gumb za pretvaranje
convert_button = tk.Button(root, text="Pretvori", command=convert, bg="black", fg="green")
convert_button.pack(pady=10)

# Prikaz rezultata
result_label = tk.Label(root, textvariable=result,font=("Arial",12,"bold"))
result_label.pack()

# Pokretanje aplikacije
root.mainloop()
