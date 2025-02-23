import tkinter as tk

# Glavna aplikacija
root = tk.Tk()
root.title("Crtanje slobodnom rukom s promjenom boje i brisanjem")

# Kreiranje platna s dimenzijama 500x400 i bijelom pozadinom
canvas = tk.Canvas(root, width=500, height=400, bg="white")
canvas.pack()

# Varijabla za pohranu odabrane boje
color_var = tk.StringVar(value="black")  # Zadana boja je crna

# Funkcija koja crta liniju s odabranom bojom
def draw(event):
    canvas.create_line(event.x, event.y, event.x+1, event.y+1, fill=color_var.get(), width=2)

# Povezivanje događaja za povlačenje miša (lijevi klik)
canvas.bind("<B1-Motion>", draw)

# Funkcija koja postavlja boju na crvenu
def set_red():
    color_var.set("red")

# Funkcija koja postavlja boju na plavu
def set_blue():
    color_var.set("blue")

# Funkcija koja briše sve elemente na platnu
def clear_canvas():
    canvas.delete("all")

# Kreiranje okvira za Radiobuttonove
color_frame = tk.Frame(root)
color_frame.pack(pady=10)

# Dodavanje Radiobuttonova za promjenu boje (samo crvena i plava)
red_button = tk.Radiobutton(color_frame, text="Crvena", variable=color_var, value="red", command=set_red)
red_button.pack(side=tk.LEFT, padx=5)

blue_button = tk.Radiobutton(color_frame, text="Plava", variable=color_var, value="blue", command=set_blue)
blue_button.pack(side=tk.LEFT, padx=5)

# Dodavanje gumba za brisanje platna
clear_button = tk.Button(root, text="Obriši", command=clear_canvas)
clear_button.pack(pady=10)

# Pokretanje glavne petlje
root.mainloop()
