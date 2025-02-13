import tkinter as tk
import random

# Inicijalne vrijednosti za statistiku
tocni_odgovori = 0
ukupno_pokusaja = 0
trenutno_rjesenje = 0  # Čuva točan rezultat izraza

def generiraj_izraz():
    """Generira novi matematički izraz i postavlja ga u labelu."""
    global trenutno_rjesenje, ukupno_pokusaja
    
    operator = random.choice(["+", "-", "*"])  # Nasumično bira operator
    
    if operator in ["+", "-"]:
        broj1 = random.randint(1, 99)
        broj2 = random.randint(1, 99)
    else:  # Ako je množenje (*), koristimo brojeve od 1 do 20
        broj1 = random.randint(1, 20)
        broj2 = random.randint(1, 20)
    
    trenutno_rjesenje = eval(f"{broj1} {operator} {broj2}")  # Računa točno rješenje
    label_izraz.config(text=f"{broj1} {operator} {broj2}")  # Postavlja izraz u label
    
    entry_rjesenje.delete(0, tk.END)  # Briše prethodni unos
    ukupno_pokusaja += 1  # Povećava ukupan broj izraza
    azuriraj_statistiku()  # Ažurira prikaz statistike

def provjeri_rjesenje():
    """Provjerava je li  korisnikov unos točan."""
    global tocni_odgovori
    
    try:
        unos = int(entry_rjesenje.get())  # Uzima broj iz Entry polja
        if unos == trenutno_rjesenje:
            tocni_odgovori += 1  # Povećava broj točnih odgovora
            label_rezultat.config(text="✅ Točno!", fg="green")
        else:
            label_rezultat.config(text=f"❌ Netočno! Točno: {trenutno_rjesenje}", fg="red")
    except ValueError:
        label_rezultat.config(text="⚠ Unesi broj!", fg="orange")
    
    azuriraj_statistiku()  # Ažurira statistiku
    generiraj_izraz()  # Automatski generira novi izraz

def azuriraj_statistiku():
    """Ažurira label koji prikazuje statistiku (tačno / ukupno)."""
    label_statistika.config(text=f"{tocni_odgovori} / {ukupno_pokusaja}")

def zatvori_aplikaciju():
    """Zatvara Tkinter prozor."""
    root.destroy()

# Kreiranje Tkinter prozora
root = tk.Tk()
root.title("Matematički kviz")
root.geometry("400x250")

frame = tk.Frame(root)
frame.pack(pady=20)

# Label za prikaz izraza
label_izraz = tk.Label(frame, text="Klikni 'Generiraj'", font=("Arial", 20))
label_izraz.grid(row=0, column=0, padx=10)

# Entry polje za unos rješenja
entry_rjesenje = tk.Entry(frame, font=("Arial", 16), width=5)
entry_rjesenje.grid(row=0, column=1, padx=10)

# Dugme za provjeru rješenja
button_provjeri = tk.Button(frame, text="Provjeri", font=("Arial", 14), command=provjeri_rjesenje)
button_provjeri.grid(row=0, column=2, padx=10)

# Label za ispis rezultata (točno/netočno)
label_rezultat = tk.Label(root, text="", font=("Arial", 14))
label_rezultat.pack(pady=5)

# Label za statistiku (broj tačnih / ukupnih izraza)
label_statistika = tk.Label(root, text="0 / 0", font=("Arial", 14))
label_statistika.pack()

# Dugme za završetak igre
button_kraj = tk.Button(root, text="Kraj", font=("Arial", 14), command=zatvori_aplikaciju)
button_kraj.pack(pady=10)

# Generiše prvi izraz kada se program pokrene
generiraj_izraz()

# Pokretanje Tkinter aplikacije
root.mainloop()
