import tkinter as tk

def on_check():
    # Dohvati sve označene države i prikaži njihove glavne gradove
    for grad, var in check_vars.items():
        print("Grad:",grad, "var:",var,"var value:",var.get())
    odabrani_gradovi = [drzave[grad] for grad, var in check_vars.items() if var.get()]
    label.config(text=", ".join(odabrani_gradovi) if odabrani_gradovi else "Nema odabranih država")

# Glavni prozor
root = tk.Tk()
root.title("Odabir država")

# Rječnik država i njihovih glavnih gradova
drzave = {
    "Hrvatska": "Zagreb",
    "Španjolska": "Madrid",
    "Italija": "Rim",
    "Engleska": "London",
    "Norveška": "Oslo"
}

# Spremnik varijabli za Checkbutton
check_vars = {}

# Kreiraj Checkbutton za svaku državu
for drzava in drzave:
    print(drzava)
    var = tk.IntVar()
    check_vars[drzava] = var
    tk.Checkbutton(root, text=drzava, variable=var, command=on_check).pack(anchor="w")

# Labela za prikaz odabranih gradova
label = tk.Label(root, text="Nema odabranih država")
label.pack()

root.mainloop()
