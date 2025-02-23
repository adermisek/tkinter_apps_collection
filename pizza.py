import tkinter as tk

# Funkcija za izračun cijene
def calculate_price():
    total_price = 0

    # Petlja kroz sve odabrane pizze
    for pizza in pizza_listbox.curselection():
        pizza_type = pizza_listbox.get(pizza)
        
        # Cijene za pizze
        pizza_prices = {
            "Vesuvio": (7.50, 10.00, 12.00),
            "Picante": (7.50, 10.00, 12.00),
            "Mexicana": (7.50, 10.00, 12.00),
            "Slavonska": (7.50, 10.00, 12.00),
            "Zagorska": (7.50, 10.00, 12.00),
            "Vege": (7.50, 10.00, 12.00)
        }

        # Dohvaćanje cijene pizze na temelju vrste i veličine
        pizza_size = pizza_size_var.get()  # Dohvaćanje odabrane veličine pizze
        if pizza_size == "Mala":
            pizza_price = pizza_prices[pizza_type][0]
        elif pizza_size == "Srednja":
            pizza_price = pizza_prices[pizza_type][1]
        elif pizza_size == "Velika":
            pizza_price = pizza_prices[pizza_type][2]

        # Dodaci
        add_ons = 0
        if eggs_var.get():
            add_ons += 0.50
        if cream_var.get():
            add_ons += 0.50
        if olives_var.get():
            add_ons += 0.50
        if peppers_var.get():
            add_ons += 0.50
        if cheese_var.get():
            add_ons += 0.50

        # Ukupna cijena za tu pizzu s dodacima
        total_price += pizza_price + add_ons
    # Ispis ukupne cijene
        price_label.config(text=f"Ukupna cijena: €{total_price:.2f}")

# Glavni prozor
root = tk.Tk()
root.title("Pizza narudžba")

# Varijabla za odabir veličine pizze
pizza_size_var = tk.StringVar()
pizza_size_var.set("Mala")  # Zadana veličina

# Varijable za dodatke (CheckButton)
eggs_var = tk.BooleanVar()
cream_var = tk.BooleanVar()
olives_var = tk.BooleanVar()
peppers_var = tk.BooleanVar()
cheese_var = tk.BooleanVar()

# Naslov za vrste pizza
tk.Label(root, text="Odaberite vrste pizze:").pack()

# Lista za višestruki odabir vrsta pizze
pizza_listbox = tk.Listbox(root, height=6, selectmode="single")
pizza_types = ["Vesuvio", "Picante", "Mexicana", "Slavonska", "Zagorska", "Vege"]
for pizza in pizza_types:
    pizza_listbox.insert(tk.END, pizza)
pizza_listbox.pack()

# Naslov za veličinu pizze
tk.Label(root, text="Odaberite veličinu pizze:").pack()

# RadioButton za veličinu pizze
tk.Radiobutton(root, text="Mala", variable=pizza_size_var, value="Mala").pack()
tk.Radiobutton(root, text="Srednja", variable=pizza_size_var, value="Srednja").pack()
tk.Radiobutton(root, text="Velika", variable=pizza_size_var, value="Velika").pack()

# Naslov za dodatke
tk.Label(root, text="Odaberite dodatke (0.50€ svaki):").pack()

# CheckButton za dodatke
tk.Checkbutton(root, text="Jaja", variable=eggs_var).pack()
tk.Checkbutton(root, text="Vrhnje", variable=cream_var).pack()
tk.Checkbutton(root, text="Masline", variable=olives_var).pack()
tk.Checkbutton(root, text="Feferoni", variable=peppers_var).pack()
tk.Checkbutton(root, text="Sir", variable=cheese_var).pack()

# Gumb za izračun cijene
calculate_button = tk.Button(root, text="Izračunaj cijenu", command=calculate_price)
calculate_button.pack()

# Labela za ispis cijene
price_label = tk.Label(root, text="Ukupna cijena: €0.00")
price_label.pack()

# Pokretanje glavne petlje
root.mainloop()
